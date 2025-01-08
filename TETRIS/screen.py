from PIL import Image, ImageFilter
import time
import os
import time

def Screen(ImageInput):
    image = Image.open(ImageInput)
    
    new_image = image.resize((200,os.get_terminal_size().lines-1),Image.ANTIALIAS)
    new_image =  new_image.filter(ImageFilter.SHARPEN)
    #new_image.show()
    #f = ImageFilter.UnsharpMask()
    #new_image = new_image.filter(f)
    
    imageData = list(new_image.getdata())
    #print(imageData)
    #
    #new_image.save('resizeimage.jpeg')
    #time.sleep(10)
    #print(imageData)
    #print(new_image.size)
    imagesize = new_image.size
    #print(imagesize[1])
    x = int(imagesize[0])
    #print(imageData)
    content = ''
    width = os.get_terminal_size().columns
    for i in range(imagesize[0]*imagesize[1]):
        rgb = imageData[i]
        if x <=0:
            #print(f"\x1b[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m\u25AA",end ='\n')
            #print(f"\x1b[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m.",end ='\n')
            #print(f"\x1b[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m\u2588",end ='\n')
            
            content = content+(f'\x1b[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m\u2588\n')
            x = int(imagesize[0])
            
        if x > 0:
                
            #print(f"\x1b[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m\u25AA",end ='')
            #print(f"\x1b[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m.",end ='')
            
            #print(f"\x1b[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m\u2588" , end ='')
            if x ==int(imagesize[0]):
                content += ' '*(int(os.get_terminal_size().columns/2)-100)
            content = content+(f'\x1b[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m\u2588')
        x = x-1
    print(content)      
        
        