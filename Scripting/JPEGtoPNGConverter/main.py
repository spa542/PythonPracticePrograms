import sys
import os
from os import path
from PIL import Image

# 1. Grab the first and second argument
# 2. Check if new/ exists, if not then create it
# 3. Loop through folder and convert all jpg files into png files
# 4. Save these files

def main():
	if len(sys.argv) != 3:
		print('Amount of args must be 3: (script) (jpegFolder) (folderForPNG)')
		exit();
	else:
		image_Folder = sys.argv[1]
		output_Folder = sys.argv[2]
	
		if not os.path.exists(output_Folder):
			os.makedirs(output_Folder)	
	
		count = 0
		for filename in os.listdir(image_Folder):
			if filename.endswith(".jpg"):
				img = Image.open(f'{image_Folder}{filename}')
				clean_name = os.path.splitext(filename)[0] # We only want filename by itself
				img.save(f'{output_Folder}{clean_name}.png', 'png')
				print('File converted and saved...');
				count += 1
		print(f'{count} files converted')

if __name__ == '__main__':
	main();
