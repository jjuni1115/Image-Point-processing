from PIL import Image
from matplotlib import pyplot as plot
import numpy as np
import math

im=Image.open("lena_gray_8bit.bmp")  #load image
his=[0 for i in range(256)]
pixel=np.array(im)
for i in range(0,512):
    for j in range(0,512):
        his[pixel[i][j]]+=1          #save pixel in histogram
x=[]
for i in range(0,256):
    x.append(i)
plot.bar(x,his,label="original",color='b')  #make bar graph
plot.legend()
plot.title("histogram")
plot.show()

plot.imshow(pixel,cmap='gray')        #show image
plot.show()
