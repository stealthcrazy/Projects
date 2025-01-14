import numpy as np


#fft algorithm built from ground up
#Problems with IIFT2 so using numpy IFFT

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

def IFFT(a):
    n = len(a)
    if n ==1:
        return a
    Wn = (np.exp((-2 *np.pi *1j)/n))*(1/n)
   
    Ae = np.array([a[i] for i in range(0,len(a),2)],dtype = "complex")
    Ao = np.array([a[i] for i in range(1,len(a),2)],dtype =  "complex")
    
    ye = np.array(IFFT(Ae),dtype = "complex")
    yo = np.array(IFFT(Ao),dtype =  "complex")
    y = []

    for i in range(n):
        y.append(0)

   
    for k in range(int(n/2)):
        
        y[k]= ye[k]+(Wn**k)*yo[k]
        y[k + int(n/2)]=  ye[k]-(Wn**k)*yo[k]
        
        
    return np.array(y,dtype =   "complex")




def Column(vals, n, s):
    return [vals[i][n] for i in range(s)]
def FFT2(vals,s):
    Dat = []
    Dat2 = []
    Dat3 = []
    for i in range(s[1]):
        #row = list(np.abs(FFT(vals[i]))*2/s[0])
        row = list(FFT(vals[i]))
        for j in row:
            Dat.append(j)
    Dat = np.array(Dat).reshape(s[0],s[1])
    
    for i in range(s[0]):
        #column = list(np.abs(FFT(Column(Dat,i,s[0])   )) )
        column = list(FFT(Column(Dat,i,s[0]))) 
        for j in column:
            Dat2.append(j)
    Dat2 = np.array(Dat2).reshape(s[0],s[1])

    for i in range(s[0]):
        column = Column(Dat2,i,s[0])
        for j in column:
            Dat3.append(j)
        
    
    #print(np.array(Dat).reshape(16,16))
    return np.array(Dat3).reshape(s[0],s[1])
def IFFT2(vals,s):
    Dat = []
    Dat2 = []
    Dat3 = []
    for i in range(s[0]):
        #column = list(np.abs(np.fft.ifft(Column(vals,i,s[0])))*2/s[0])
        column = list(np.fft.ifft(Column(vals,i,s[0])))
        for j in column:
            Dat.append(j)
    Dat = np.array(Dat).reshape(s[0],s[1])

    for i in range(s[0]):
        column = Column(Dat,i,s[0])
        for j in column:
            Dat2.append(j)
    Dat2 = np.array(Dat2).reshape(s[0],s[1])
    for i in range(s[1]):
        #row = list(np.abs(np.fft.ifft(Dat2[i]))*2/s[0])
        row = list(np.fft.ifft(Dat2[i]))
        
        for j in row:
            Dat3.append(j)
    Dat3 = np.array(Dat3).reshape(s[0],s[1])

    
        
    
    #print(np.array(Dat).reshape(16,16))
    return Dat3