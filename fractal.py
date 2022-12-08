from PIL import Image
import os


def julia(w=600, h=600, zoom=1, cX= -0.7, cY=0.27015, maxIter=255, moveX=0.0, moveY=0.0):

    # creating the new image in RGB mode
    img = Image.new("RGB", (w, h), "white")

    # Allocating the storage for the image and
    # loading the pixel data.
    pix = img.load()

    for x in range(w):
        for y in range(h):
            zx = 1.5 * (x - w / 2) / (0.5 * zoom * w) + moveX
            zy = 1.0 * (y - h / 2) / (0.5 * zoom * h) + moveY
            i = maxIter
            while zx * zx + zy * zy < 4 and i > 1:
                tmp = zx * zx - zy * zy + cX
                zy, zx = 2.0 * zx * zy + cY, tmp
                i -= 1

            # convert byte to RGB (3 bytes), kinda
            # magic to get nice colors
            pix[x, y] = (i << 21) + (i << 10) + i * 8

    id_ = len(os.listdir('static/fractals'))
    img.save(fp=open(f"static/fractals/{id_}.jpeg", mode='x'))
    return id_
