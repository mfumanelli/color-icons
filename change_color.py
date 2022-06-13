from PIL import Image
import numpy as np
import tkinter as tk
from tkinter.colorchooser import askcolor
import sys


def getColor():
    """
    Function that creates a color-picker, the selected color is returned
    in RGB and HEX.

    Returns:
        tuple: RGB and HEX code of the selected color.
    """
    win = None
    if not tk._default_root:
        win = tk.Tk()
        win.wm_withdraw()
    color = askcolor()
    if win is not None:
        win.destroy()
    return color


def change_color(input_path, output_path, color):
    """
    Function that given an icon in .png format changes its color and
    saves it to a specified path

    Args:
        input_path: Input icon path.
        output_path: Output path chosen for the colored icon.
        color: Chosen color with which to edit the input icon.

    Returns:
        PIL.Image.Image: Edited icon.
    """
    img = Image.open(input_path)
    img.convert('LA')
    img = img.convert('RGBA')
    image_np = np.array(img)
    red, green, blue, alpha = image_np.T
    mask = (red == 0) & (blue == 0) & (green == 0)
    image_np[..., :-1][mask.T] = color
    edited_image = Image.fromarray(image_np)
    edited_image.save(output_path)
    return edited_image


if __name__ == "__main__":
    img_input_path = sys.argv[1]  # insert path of icone
    img_output_path = sys.argv[2]  # choose output path
    rgb, _ = getColor()
    change_color(input_path=img_input_path, output_path=img_output_path, color=rgb)