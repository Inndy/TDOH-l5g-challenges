import os
import PIL.Image

img_text = PIL.Image.open(open('qr.png', 'rb'))
img_base = PIL.Image.open(open('lig.png', 'rb'))

for x in range(img_text.width):
    for y in range(img_text.height):
        p = (x, y)
        cl = img_base.getpixel(p)
        n = img_text.getpixel((p))
        if n:
            n = 0x03
        cl = tuple((n & 0x3) | (c & 0xfc) for c in cl)
        img_base.putpixel(p, cl)

img_base.save(open('output.png', 'wb'), 'PNG')
os.system('exiftool -comment="extract LSB on this image" output.png')
