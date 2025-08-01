
f = open('files/Example_Image.png', 'rb') # read in Binary if you want to read images

f1 = open('files/png.png', 'wb') #writes in Binary format

for i in f:
    f1.write(i)  # you can find image in files/png.png
