from PIL import Image, ImageDraw, ImageFont
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
from tkinter import colorchooser,messagebox
import tkinter as tk
from random import randint
from time import sleep

app_path = __file__[:-7]
dist_path = os.path.join(os.getcwd(),'dist')
if not os.path.exists(dist_path):
    dist_path = os.path.join(os.getcwd(),'Desktop','dist')
    if not os.path.exists(dist_path):
        os.makedirs(dist_path)

def make_lines(string):
    result = ""
    for word in string.split(' '):
        if len(result.split('&&&')[-1]) + len(word) > 60:
            result += f"&&&{word} "
        else:
            result += f'{word} '
    return result.split('&&&')
    
def make_bg(color):
    height, width, channel = 1080, 1080, 3
    arr = np.full((height, width, channel), list(color), dtype=('uint8'))
    plt.imsave(os.path.join(app_path,'template.png'),arr)
    return cv2.imread(os.path.join(app_path,'template.png'))

def clean_title(title):
    res = ''
    for word in title.split(' '):
        if len(res) + len(word) < 38:
            res += f'{word} '
    return res

def draw(title,lines,color_title,color_text,file_name):
    image = Image.open(os.path.join(app_path,'template.png'))

    draw = ImageDraw.Draw(image)
    font_title = ImageFont.truetype(os.path.join(app_path,'title.otf'), 50)
    font_text = ImageFont.truetype(os.path.join(app_path,'text.ttf'), 36)

    position_title = (50, 50)
    position_text = [70, 140]

    draw.text(position_title, clean_title(title), font=font_title, fill=color_title)
    for text in lines:
        draw.text(tuple(position_text), text, font=font_text, fill=color_text)
        position_text[1] += 50

    fp = os.path.join(dist_path,file_name)
    image.save(fp)
    return fp

def is_ok(fp,wait):
    image = cv2.imread(os.path.join(app_path,fp))
    image = cv2.resize(image, (700, 700))
    cv2.imshow('bg',image)
    cv2.waitKey(wait)
    cv2.destroyAllWindows()
    return messagebox.askyesno('ICG', 'ok?')

def bg_generator():
    target = False
    while (not target):
        make_bg(colorchooser.askcolor((randint(55,200),randint(55,200),randint(55,200)),title ="bg")[0])
        color_title = colorchooser.askcolor('#000',title ="title")[0]
        color_text = colorchooser.askcolor('#000',title ="text")[0]
        draw('Title',['line1 data for test','line2 data for test','line3 data for test'],color_title,color_text,os.path.join(app_path,'temp.png'))
        target = is_ok('temp.png',3000)

    return color_title, color_text

def entered_value():
    global slide
    global color_title
    global color_text

    title = entry1.get("1.0",'end-1c')
    text = entry2.get("1.0",'end-1c')

    if "\n" in text:
        lines_n = text.split('\n')
        lines = []
        for line in lines_n:
            temp = make_lines(line)
            lines += temp

    else:
        lines = make_lines(text)

    file_name = f"post{slide}.png"
    draw(title,lines,color_title,color_text,file_name)
    fp = os.path.join(dist_path,file_name)
    target = is_ok(fp,10000)
    if target:
        slide += 1
        messagebox.showinfo(file_name, 'done!')
    else:
        os.remove(fp)

if __name__ == "__main__":
    
    color_title, color_text = bg_generator()
    slide = 1

    window = tk.Tk()
    window.title("ICG")
    window.geometry("700x600")

    label1 = tk.Label(window, text="Title")
    label1.pack()

    entry1 = tk.Text(window, height = 1, width = 38)
    entry1.pack()

    label2 = tk.Label(window, text="Text")
    label2.pack()

    entry2 = tk.Text(window, height = 19, width = 65)
    entry2.pack()

    button = tk.Button(window, text="Submit", command=entered_value)
    button.pack()

    window.mainloop()
