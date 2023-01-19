from PIL import Image
import matplotlib.pyplot as plt

def show_image(img, size=None, scale=1.0, values=False, grid=False):
    if not size:
        size = img.size

    size_in = (scale * size[0] / 100, scale * size[1] / 100)

    fig, ax = plt.subplots(figsize=size_in)
    ax.imshow(img, cmap='gray')

    if values:
        for y in range(img.height):
            for x in range(img.width):
                v = img.getpixel((x, y))
                c = '#FFF' if v < 128 else '#000'
                text = ax.text(x, y, v, ha='center', va='center', color=c)

    if grid:
        ax.minorticks_on()
        ax.grid(which='major', color='#FFFFFF', linewidth=2)
        ax.grid(which='minor', color='#CCCCCC')