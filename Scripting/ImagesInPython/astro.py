# Manipulating the astro.jpg file for course

from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
img.thumbnail((400, 400))
img.save('thumbnail.jpg')
# Because the image was so large, doing this, the aspect ratio will be lost
# The image either gets cut off or squished
# use a special method above!

