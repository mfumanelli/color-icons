from PIL import Image
import numpy as np
import tkinter as tk
from tkinter.colorchooser import askcolor
import argparse


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
    img = img.convert('LA')
    img = img.convert('RGBA')
    image_np = np.array(img)
    red, green, blue, alpha = image_np.T
    mask = (alpha > 0)
    image_np[..., :-1][mask.T] = color
    edited_image = Image.fromarray(image_np)
    edited_image.save(output_path)
    return edited_image


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, required=True)
    parser.add_argument('--output_path', type=str, required=True)
    args = parser.parse_args()
    rgb, _ = getColor()
    change_color(input_path=args.input_path, output_path=args.output_path, color=rgb)