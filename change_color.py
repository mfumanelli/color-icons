from PIL import Image
import numpy as np

def change_color(input, color=[255, 255, 255]):
    input.convert('LA')
    image = input.convert('RGBA')
    image_np = np.array(image)
    red, green, blue, alpha = image_np.T
    mask = (red == 0) & (blue == 0) & (green == 0)
    image_np[..., :-1][mask.T] = (color[0], color[1], color[2])
    edited_image = Image.fromarray(image_np)
    return edited_image

