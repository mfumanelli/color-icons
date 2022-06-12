from PIL import Image
import numpy as np
import tkinter as tk
from tkinter.colorchooser import askcolor

def getColor():
    """Choose color.
        Returns tuple of RBG and HEX."""
    win = None
    if not tk._default_root:
        win = tk.Tk()
        win.wm_withdraw()
    color = askcolor()
    if win is not None:
        win.destroy()
    return color

def change_color(input, color):
    img = Image.open(input)
    img.convert('LA')
    img = img.convert('RGBA')
    image_np = np.array(img)
    red, green, blue, alpha = image_np.T
    mask = (red == 0) & (blue == 0) & (green == 0)
    image_np[..., :-1][mask.T] = color
    edited_image = Image.fromarray(image_np)
    edited_image.save("prova_col.png")
    return edited_image

if __name__ == "__main__":
    rgb, _ = getColor()
    change_color("prova.png", color=rgb)