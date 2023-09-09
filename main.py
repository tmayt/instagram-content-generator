from PIL import Image, ImageDraw, ImageFont
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
from tkinter import colorchooser,messagebox
import tkinter as tk


def make_lines(string):
    result = ""
    for word in string.split(' '):
        if len(result.split('&&&')[-1]) + len(word) > 54:
            result += f"&&& {word}"
        else:
            result += f'{word} '
    return result.split('&&&')
    
def make_bg(color):
    height, width, channel = 1080, 1080, 3
    arr = np.full((height, width, channel), list(color), dtype=('uint8'))
    plt.imsave('template.png',arr)
    return cv2.imread('template.png')

def draw(title,lines,color_title,color_text,file_name):
    image = Image.open("template.png")

    draw = ImageDraw.Draw(image)

    font_title = ImageFont.truetype("title.otf", 50)
    font_text = ImageFont.truetype("text.ttf", 36)

    position_title = (50, 50)
    position_text = [70, 140]

    draw.text(position_title, title, font=font_title, fill=color_title)
    for text in lines:
        draw.text(tuple(position_text), text, font=font_text, fill=color_text)
        position_text[1] += 50

    fp = os.path.join('dist',file_name)
    image.save(fp)
    return fp

if __name__ == "__main__":

    window = tk.Tk()
    window.title("PythonExamples.org")
    window.geometry("500x500")

    slide = 1

    make_bg(colorchooser.askcolor(title ="bg")[0])
    color_title = colorchooser.askcolor(title ="title")[0]
    color_text = colorchooser.askcolor(title ="text")[0]

    def entered_value():
        global slide
        global color_title
        global color_text

        title = entry1.get("1.0",'end-1c')
        lines = entry2.get("1.0",'end-1c')

        if r"\n" in lines:
            lines = lines.split(r'\n')
        else:
            lines = make_lines(lines)

        file_name = f"post{slide}.png"

        draw(title,lines,color_title,color_text,file_name)

        slide += 1

        messagebox.showinfo(file_name, 'done!')

    label1 = tk.Label(window, text="Title")
    label1.pack()

    entry1 = tk.Text(window, height = 1, width = 38)
    entry1.pack()

    label2 = tk.Label(window, text="Text")
    label2.pack()

    entry2 = tk.Text(window, height = 19, width = 54)
    entry2.pack()

    button = tk.Button(window, text="Submit", command=entered_value)
    button.pack()

    window.mainloop()
