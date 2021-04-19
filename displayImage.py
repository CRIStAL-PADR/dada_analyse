# -*-coding: utf-*-
from PIL import Image
from PIL import ImageDraw
 
img = Image.new('RGB', (1000, 1000), color = (73, 109, 137))
 
d = ImageDraw.Draw(img)
for i in range(100):
    for j in range(100):
        d.text((i*10,j*10), "1",  fill=(200, 255, 0), spacing = 1)
 
img.save('pil_text_font.jpg')