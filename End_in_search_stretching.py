from PIL import Image
from matplotlib import pyplot as plot
import numpy as np
import math
im=Image.open("lena_gray_8bit.bmp")

pixel=np.array(im)
low=50
high=190

#End in search stretching
for i in range(0,512):
    for j in range(0,512):
        if pixel[i][j]<=low:
            pixel[i][j]=0
        elif pixel[i][j]>=high:
             pixel[i][j]=255
        else:
            pixel[i][j]=255*((pixel[i][j]-low)/(high-low))

his=[0 for i in range(256)]
for i in range(0,512):
    for j in range(0,512):
        his[pixel[i][j]]+=1
x=[]
for i in range(0,256):
    x.append(i)
plot.bar(x,his,label="End in search stretching",color='b')
plot.legend()
plot.title("histogram")
plot.show()

plot.imshow(pixel,cmap='gray')
plot.show()
