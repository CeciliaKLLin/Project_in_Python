from PIL import Image, ImageFilter

img = Image.open('bulbasaur.jpg')

print(img)
print(img.format, img.size, img.mode)
print(dir(img))

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img1 = img.convert('L')
filtered_img.save('blur.png', 'png')
filtered_img1.save('grey.png', 'png')
crooked = filtered_img1.rotate(90)
filtered_img1.show() #open the picture
crooked.save('rotated.png', 'png')
#png support filter, but jpg may occur error

im = Image.open('astro.jpg')
print(im.size)
Resize = im.resize((400,400))
print(Resize)
Resize.save('Resize.png', 'png')



