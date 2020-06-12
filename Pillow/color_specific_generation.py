from PIL import Image
 
img = Image.new('RGB', (60, 30), color = 'red')#mode ,size ,color
img.save('pil_color.png')
img.show()
