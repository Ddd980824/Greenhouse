from PIL import Image
#打开jpg图像文件，注意路径要改成图片的存储路径
im = Image.open('/Users/dell/Desktop/松田阵平.jpg')
# 获得图像的尺寸
w,h = im.size
print(w,h)
#format属性指定了图像文件的格式，如果图像不是从文件中加载的则为None；
# size属性是一个2个元素的元组，包含图像宽度和高度（像素）；
# mode属性定义了像素格式，常用的像素格式为"L"(luminance）-灰度图，”RGB","CMYK";
print(im.format, im.size, im.mode)
#  缩放到50%
im.thumbnail((w//2,h//2))
#把缩放后的图像用jpeg格式保存：
im.save('/Users/dell/Desktop/thumbnail.jpg','jpeg')

from PIL import Image,ImageFilter
im = Image.open('/Users/dell/Desktop/松田阵平.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('/Users/dell/Desktop/blur.jpg','jpeg')