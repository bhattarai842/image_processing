import Image

def image_resize(file_name, width, height):
	img = Image.open(file_name)
	return img.resize((width, height), Image.NEAREST)




