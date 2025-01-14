import numpy as np
from FFT import *
from PIL import Image



def compress(image_path ,size = (128,128),percentage = 80):

    image = Image.open(image_path)
    image = image.convert('RGB')

    vals = list(image.getdata())
    DataL0 = np.array(split(vals , 0)).reshape(size[0],size[1])
    D =FFT2(DataL0,size)
    imageD = Image.new('RGB', size)
    threshold = np.percentile(np.abs(D),percentage)
    D[np.abs(D)<threshold] = 0
    D= shift(D)



    Dm = GSL(D)

    imageD.putdata(Dm)
    imageD.save("./Image Compression using FFT/Compressed.png")
    return D

def uncompress(compressedData ,size = (128,128)):
    imageDD = Image.new('RGB', size)
    

    

    DD = shift(compressedData)
    DD = IFFT2(DD,size).real
    DD = np.array([DD[len(DD)-i-1] for i in range(len(DD))])
    DD = DD.transpose()
    DD = np.array([DD[len(DD)-i-1] for i in range(len(DD))])
    DD= DD.transpose()
    DD = GSL(DD)
    imageDD.putdata(DD)
    imageDD.save(f"./Image Compression using FFT/UnCompressed-.jpg")


def split(vals , layer):
    Layer = []
    for i in vals:
        #print(i[layer])
        Layer.append(i[layer])
    return Layer

def GSL(vals ):
    Layer = []
    for i in vals:
        for j in i:
        #print(i[layer])
            k = (int(j),int(j),int(j))
            #print(type(k))
            Layer.append(k)
    return Layer

def shift(x):
    y = []
    t = []
    k = []
    for i in x:
        temp1 = list(i[:len(i)//2])
        temp2 = list(i[len(i)//2:])
        #temp2 = temp2[-1::-1]
        y.append(temp2+temp1)
    y = np.array(y)
    #print(y)
    #print("\n")
    for j in range(len(y)):
        c = Column(y,j,len(y))
        temp1 = c[:len(c)//2]
        temp2 = c[len(c)//2:]
        t.append(temp2+temp1)
    t = np.array(t)
    #print(t)
    #print("\n")
    
    for j in range(len(t)):
        c = Column(t,j,len(t))
        k.append(c)
    


    return k


D = compress("Image Compression using FFT/winnie_the_pooh.jpg")
uncompress(D)










