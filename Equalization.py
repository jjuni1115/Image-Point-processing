from PIL import Image
from matplotlib import pyplot as plot
import numpy as np
import math
im=Image.open("lena_gray_8bit.bmp")   #load image
his=[0 for i in range(256)]        
pixel=np.array(im)
for i in range(0,512):
    for j in range(0,512):
        his[pixel[i][j]]+=1

#Equalization
normalize_sum=[]
sum=0
for i in range(0,256):
    sum+=his[i]
    normalize_sum.append(255*sum/(512*512))
for i in range(0,256):
    normalize_sum[i]=int(normalize_sum[i])

for i in range(0,512):
    for j in range(0,512):
        pixel[i][j]=normalize_sum[pixel[i][j]]
his2=[0 for i in range(256)]
for i in range(0,512):
    for j in range(0,512):
        his2[pixel[i][j]]+=1
x=[]
for i in range(0,256):
    x.append(i)
plot.bar(x,his2,label="Equalization",color='b')
plot.legend()
plot.title("histogram")
plot.show()

plot.imshow(pixel,cmap='gray')
plot.show()
