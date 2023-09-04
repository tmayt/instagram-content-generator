from PIL import Image, ImageDraw, ImageFont
import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

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
    red, green, blue = color
    arr = np.full((height, width, channel), [red, green, blue], dtype=('uint8'))
    plt.imsave('template.png',arr)
    return cv2.imread('template.png')

if __name__ == "__main__":
    description = '''
        Title line ==> 38 chars
        text line ==> 54 chars
    '''
    print(description)

    slide = 1
    bg_color = input('enter bg color (R,G,B) default(255, 255, 255) ==> ').replace('(', '').replace(')', '').split(',')
    bg_color = bg_color if len(bg_color) == 3 else (255, 255, 255)
    bg_color = tuple([int(i) for i in bg_color])
    make_bg(bg_color)

    while input('continue (y/n)? ') == 'y':
        print('-'*20)
        image = Image.open("template.png")

        draw = ImageDraw.Draw(image)

        title = input("Your Title: ")
        lines = input("Your Text: ")

        if "\n" in lines:
            lines = lines.split('\n')
        else:
            lines = make_lines(lines)

        font_title = ImageFont.truetype("title.otf", 50)
        font_text = ImageFont.truetype("text.ttf", 36)

        position_title = (50, 50)
        position_text = [70, 140]

        color_title = input('enter title color (R,G,B) default(0, 0, 0) ==> ').replace('(', '').replace(')', '').split(',')
        color_text = input('enter text color (R,G,B) default(0, 0, 0) ==> ').replace('(', '').replace(')', '').split(',')

        color_title = color_title if len(color_title) == 3 else (0, 0, 0)
        color_text = color_text if len(color_text) == 3 else (0, 0, 0)

        color_title = tuple([int(i) for i in color_title])
        color_text = tuple([int(i) for i in color_text])

        draw.text(position_title, title, font=font_title, fill=color_title)
        for text in lines:
            draw.text(tuple(position_text), text, font=font_text, fill=color_text)
            position_text[1] += 50

        file_name = f"post{slide}.png"
        image.save(os.path.join('dist',file_name))
        image.close()
        slide += 1
        print(f'{file_name} is done.')
