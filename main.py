from PIL import Image, ImageDraw, ImageFont
import os

def make_lines(string):
    result = ""
    for i, word in enumerate(string.split(' ')):
        if len(result.split('&&&')[-1]) + len(word) > 54:
            result += f"&&& {word}"
        else:
            result += f'{word} '

    return result.split('&&&')

if __name__ == "__main__":
    description = '''
        Title line ==> 38 chars
        text line ==> 54 chars
    '''
    print(description)
    slide = int(input('slide number: '))
    while input('continue (y/n)? ') == 'y':
        print('-'*10)
        # Open the Template
        image = Image.open("template.png")

        # Create a drawing object
        draw = ImageDraw.Draw(image)

        # Define the text to be added
        title = input("Your Title: ")
        lines = input("Your Text: ")
        if "&&&" in lines:
            lines = lines.split('&&&')
        else:
            lines = make_lines(lines)

        # Specify the font and size
        font_title = ImageFont.truetype("title.otf", 50)
        font_text = ImageFont.truetype("text.ttf", 36)

        # Specify the position to place the text
        position_title = (50, 50)
        position_text = [70, 140]

        # Specify the color of the text
        color = (255, 255, 255)  # white color

        # Add the text to the image
        draw.text(position_title, title, font=font_title, fill=color)
        for text in lines:
            draw.text(tuple(position_text), text, font=font_text, fill=color)
            position_text[1] += 50

        # Save the merged image as a new file
        file_name = f"post{slide}.png"
        image.save(os.path.join('dist',file_name))
        image.close()
        slide += 1
        print(f'{file_name} is done.')
