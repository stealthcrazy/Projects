import numpy as np
import matplotlib.pyplot as plt
import datashader as ds
import datashader.transfer_functions as tf



def FFT(a):
    n = len(a)
    if n ==1:
        return a
    Wn = np.exp((2 *np.pi *1j)/n)
   
    Ae = np.array([a[i] for i in range(0,len(a),2)],dtype = "complex")
    Ao = np.array([a[i] for i in range(1,len(a),2)],dtype =  "complex")
    
    ye = np.array(FFT(Ae),dtype = "complex")
    yo = np.array(FFT(Ao),dtype =  "complex")
    y = []

    for i in range(n):
        y.append(0)

   
    for k in range(int(n/2)):
        
        y[k]= ye[k]+(Wn**k)*yo[k]
        y[k + int(n/2)]=  ye[k]-(Wn**k)*yo[k]
        
        
    return np.array(y,dtype =   "complex")
smpl = 256

xs = np.linspace(0,1,smpl)



print(xs)
#ys = 4/np.pi * (np.sin( 2 * np.pi * xs) +(np.sin( 3* 2 * np.pi * xs)/3) +(np.sin( 5* 2 * np.pi * xs)/5)+ +(np.sin( 7* 2 * np.pi * xs)/7))
ys =2 * np.sin( 2 * np.pi * xs) +np.sin( 10* 2 * np.pi * xs)
#ys = np.sin( (440*np.pi)*2 * np.pi * xs) 


fft =  2/smpl * np.abs(FFT(ys))



    

plt.subplot(2, 1, 1)
plt.plot(xs, ys)

plt.subplot(2, 1, 2)



plt.subplot(2, 1, 2)

plt.plot(fft[0:len(fft)//2])

plt.show()