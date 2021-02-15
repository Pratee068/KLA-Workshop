from PIL import Image
from numpy import asarray
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import csv
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

img = mpimg.imread('C:/Users/Msi/Downloads/DataFiles/Level_1_data/1.png')     
gray = rgb2gray(img) 
data1 = asarray(gray)

img = mpimg.imread('C:/Users/Msi/Downloads/DataFiles/Level_1_data/2.png')     
gray = rgb2gray(img) 
data2 = asarray(gray)

img = mpimg.imread('C:/Users/Msi/Downloads/DataFiles/Level_1_data/3.png')     
gray = rgb2gray(img) 
data3 = asarray(gray)

img = mpimg.imread('C:/Users/Msi/Downloads/DataFiles/Level_1_data/4.png')     
gray = rgb2gray(img) 
data4 = asarray(gray)

img = mpimg.imread('C:/Users/Msi/Downloads/DataFiles/Level_1_data/5.png')     
gray = rgb2gray(img) 
data5 = asarray(gray)
i=0
w=0
b=0
h=0
j=0
k=0
from csv import writer 
for x in range(0,600):
    w=0
    b=0
    for y in range(0,800):
        if(data1[x][y]>0.7):
            w=w+1
        else:
            b=b+1
        if(data2[x][y]>0.7):
             w=w+1
        else:
            b=b+1
        if(data3[x][y]>0.7):
            w=w+1
        else:
           b=b+1
        if(data4[x][y]>0.7):
            w=w+1
        else:
            b=b+1
            
        if(data5[x][y]>0.7):
             w=w+1
        else:
           b=b+1
        if(w>b):
            for l in range(0,800):
                if(data1[x][l]<0.7):
                    with open('protagonist.csv', 'a') as f_object:
                        List=[1,x,y] 
                        writer_object = writer(f_object) 
                        writer_object.writerow(List) 
                                         
                    #print(1,",",x,",",y)
                if(data2[x][l]<0.7):
                    with open('protagonist.csv', 'a') as f_object:
                        List=[2,x,y] 
                        writer_object = writer(f_object) 
                        writer_object.writerow(List) 
                    #print(2,",",x,",",y)
    
                if(data3[x][l]<0.7):
                    with open('protagonist.csv', 'a') as f_object:
                        List=[3,x,y] 
                        writer_object = writer(f_object) 
                        writer_object.writerow(List) 
                    #print(3,",",x,",",y)
    
                if(data4[x][l]<0.7):
                    with open('protagonist.csv', 'a') as f_object:
                        List=[4,x,y] 
                        writer_object = writer(f_object) 
                        writer_object.writerow(List) 
                    #print(4,",",x,",",y)
                if(data5[x][l]<0.7):
                    with open('protagonist.csv', 'a') as f_object:
                        List=[5,x,y] 
                        writer_object = writer(f_object) 
                        writer_object.writerow(List) 
                    #print(5,",",x,",",y)
        else:
            for l in range(0,800):
                
                if(data1[x][l]>0.7):
                    with open('protagonist.csv', 'a') as f_object:
                        List=[1,x,y] 
                        writer_object = writer(f_object) 
                        writer_object.writerow(List) 
                    #print(1,",",x,",",y)
                if(data2[x][l]>0.7):
                    with open('protagonist.csv', 'a') as f_object:
                        List=[2,x,y] 
                        writer_object = writer(f_object) 
                        writer_object.writerow(List) 
                   # print(2,",",x,",",y)
    
                if(data3[x][l]>0.7):
                    with open('protagonist.csv', 'a') as f_object:
                        List=[3,x,y] 
                        writer_object = writer(f_object) 
                        writer_object.writerow(List) 
                    #print(3,",",x,",",y)
    
                if(data4[x][l]>0.7):
                    with open('protagonist.csv', 'a') as f_object:
                        List=[4,x,y] 
                        writer_object = writer(f_object) 
                        writer_object.writerow(List) 
                    #print(4,",",x,",",y)
                if(data5[x][l]>0.7):
                    with open('protagonist.csv', 'a') as f_object:
                        List=[5,x,y] 
                        writer_object = writer(f_object) 
                        writer_object.writerow(List) 
                    #print(5,",",x,",",y)
              

         