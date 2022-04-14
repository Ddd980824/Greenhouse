#1.读写图片
from PIL import Image #调用库
im = Image.open('/Users/dell/Desktop/松田阵平.jpg')
im.thumbnail((25,25)) #缩略图的保存格式不能是jpg格式
im.save('/Users/dell/Desktop/test1.png')
#2.图片剪切、粘贴、合并
from PIL import Image
im = Image.open('/Users/dell/Desktop/松田阵平.jpg')
#(box变量是一个四元组（左，上，右，下）用来表示在原始图像中截取的位置坐标
box = (100,100,200,200)  #表示在原始图像中以左上角为坐标原点，截取一个100*100（像素为单位）的图像
region = im.crop(box) #剪切
region = region.transpose(Image.ROTATE_180) #使用.transpose()对图片进行旋转 逆时针旋转180度
im.paste(region,box) #使用.paste（）对图片进行黏贴合并 粘贴box大小的region到原先的图像中
im.save('/Users/dell/Desktop/test2.png')
#使用.rotate(x)对图像进行逆时针旋转x度
#n = region.rotate(180)
#im.paste(n,box)
#im.save('/Users/dell/Desktop/test3.png')
im = Image.open('/Users/dell/Desktop/松田阵平.jpg')
r,g,b = im.split() #分割：split 函数创建一个兔相机和，每个图像包含一个通道
im = Image.merge("RGB",(b,g,r)) #merge函数接受一个颜色模式和一个图像元组，然后将它们合并为一个新的图像
im.save('/Users/dell/Desktop/test4.png')