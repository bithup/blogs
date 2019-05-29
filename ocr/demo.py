import pytesseract
from PIL import Image

image = Image.open('C:\\Users\\bithup\\Desktop\\02.jpg')
#Img = image.convert('1')
#Img.save('C:\\Users\\bithup\\Desktop\\03.jpg')

def gettable(threshold):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table

for i in range(130, 230, 10):
    table = gettable(i)
    photo = image.point(table, '1')
    photo.save('C:\\Users\\bithup\\Desktop\\'+str(i)+'.jpg')
 
# 图片二值化
# photo = Img.point(table, '1')
# photo.save('C:\\Users\\bithup\\Desktop\\03.jpg')
# image2 = Image.open('C:\\Users\\bithup\\Desktop\\03.jpg')
# code = pytesseract.image_to_string(image)
# print(code)

# 图片裁剪
#im = Image.open('C:\\Users\\bithup\\Desktop\\01.jpg')
#cropedIm = im.crop((4,80,634,3584))
#cropedIm.save('C:\\Users\\bithup\\Desktop\\02.jpg')
# image4 = Image.open('C:\\Users\\bithup\\Desktop\\01.jpg')
# code = pytesseract.image_to_string(image4)
# print(code)

# 先将图片转化为灰度