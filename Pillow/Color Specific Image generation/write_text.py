from PIL import Image, ImageDraw
 
img = Image.new('RGB', (100, 30), color = (73, 109, 137))
 
d = ImageDraw.Draw(img)
d.text((10,10), "Hello World",)
 
img.save('pil_text.png')
img.show()
