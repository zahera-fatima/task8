from PIL import Image, ImageEnhance, ImageFilter

img1 = Image.open('pic1.jpeg')

#----- save image----
#img1.save('download.png')
#----- sow image---
img1.show()

 #-------sharpness-----
enhancer = ImageEnhance.Sharpness(img1)
enhancer.enhance(6).save('download1.jpg')
#----- color ----
enhancer = ImageEnhance.Color(img1)
enhancer.enhance(6).show('download.jpg')
#------- brightness----- 
enhancer = ImageEnhance.Brightness(img1)
enhancer.enhance(1.5).show('download.jpg')
#------ contrast ------
enhancer = ImageEnhance.Contrast(img1)
enhancer.enhance(1.5).show('download.jpg')
#------ image blur ----
img1.filter(ImageFilter.GaussianBlur(radius=4)).show('download.jpg')
#----resize----
MAX_SIZE = (120,120)
img1.thumbnail(MAX_SIZE)
img1.show('pic1.jpg')