from PIL import Image, ImageFilter
# Various Image manipulation and functions from the Pillow Library

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
grey_img = img.convert('L')
filtered_img.save("blur.png", 'png')
grey_img.save("grey.png", 'png')
filtered_img.show()

yeet_img = filtered_img.rotate(90)
yeet_img.save("crooked.png", 'png')

resize = filtered_img.resize((300, 300))
resize.save("thumbnail.png", 'png')

box = (100, 100, 400, 400)
cropped = filtered_img.crop(box)
cropped.save("cropped.png", 'png')
