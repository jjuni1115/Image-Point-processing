from PIL import Image
from matplotlib import pyplot as plot
import numpy as np
import math
im=Image.open("lena_gray_8bit.bmp")

pixel=np.array(im)
low=np.min(pixel)
high=np.max(pixel)

#basic stretching
for i in range(0,512):
    for j in range(0,512):
        pixel[i][j]=255*((pixel[i][j]-low)/(high-low))

for i in range(0,512):
    for j in range(0,512):
        pixel[i][j]=int(pixel[i][j])
his=[0 for i in range(256)]
for i in range(0,512):
    for j in range(0,512):
        his[pixel[i][j]]+=1
x=[]
for i in range(0,256):
    x.append(i)
plot.bar(x,his,label="basic stretching",color='b')
plot.legend()
plot.title("histogram")
plot.show()

plot.imshow(pixel,cmap='gray')
plot.show()
