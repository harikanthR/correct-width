# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 12:07:53 2023

@author: Madhavan
"""
import cv2 
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
img = cv2.imread("spray.png")
type(img)
#plt.imshow(img)
plt.show()
img.shape
img=img[150:1900,:]
#plt.imshow(img)
plt.show()
img.shape
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#plt.imshow(img,cmap='gray')
plt.show()
gray_img.shape
#print(gray_img)
#print(gray_img.max())
#print(gray_img.min())
thresh,img_bin = cv2.threshold(gray_img, 75, 255, cv2.THRESH_BINARY)
#plt.imshow(img_bin,cmap='gray')
plt.show()
thickness = 5
#plt.imshow(img)
#contours, hierarchy = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#plt.imshow(img_contours)
i=0
#x,y=img_bin.shape
result=[]
"""
while (i<1750):
    print(i)
    ls =[]
    j=0
    while j<935:
        if img_bin[i][j]==0:
            ls.append([i,j])
            print(i,j)
            j+=1
    result.append(ls)    
    i+=1
    """
x = 0
y = -1
result = []
for i in tqdm(img_bin):
    ls=[]
    y=0
    for j in i:
        y=y+1
        if j==0:
            ls.append([x,y])            
    x=x+1
    result.append(ls)

ls = []
for m in result:
       ls.append([m[0],m[-1]])
sheet_width = []
for n in ls:
    sheet_width.append(n[1][1]-n[0][1]) 
plt.plot(sheet_width)
plt.show()