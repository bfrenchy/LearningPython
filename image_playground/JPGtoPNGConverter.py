import sys
import os
from PIL import Image

parse_directory = os.path.join(os.getcwd(), sys.argv[1])
save_directory = os.path.join(os.getcwd(), sys.argv[2])

if os.path.exists(save_directory):
	print('Directory already exists')
else:
	os.mkdir(save_directory)
	print(f'\n{fsave_directory} added as a directory.')

for image in os.listdir(parse_directory):
	if image.endswith('.jpg'):
		img_directory = os.path.join(parse_directory, image)
		file_name = f'{os.path.splitext(image)[0]}.png'
		with Image.open(img_directory) as img:
			png_save_path = os.path.join(save_directory, file_name)
			img.save(png_save_path, 'png')
