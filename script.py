
import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import measure, color, io


img = cv2.imread("C:\\Users\\eddyt\\Desktop\\dapi\\17.png")
nuclei=img[:,:,0] 
ret1, thresh = cv2.threshold(nuclei, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite("C:\\Users\\eddyt\\Desktop\\dapi\\risultati\\17_thresholded1.png",thresh)
kernel = np.ones((3,3),np.uint8)
apertura = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
cv2.imwrite("C:\\Users\\eddyt\\Desktop\\dapi\\risultati\\17_apertura.png",apertura)
from skimage.segmentation import clear_border
apertura = clear_border(apertura) #Apertura + clean border
cv2.imwrite("C:\\Users\\eddyt\\Desktop\\dapi\\risultati\\17_apertura_clearborder.png",apertura)
#plt.imshow(apertura, cmap='gray')
sure_bg = cv2.dilate(apertura,kernel,iterations=10)
cv2.imwrite("C:\\Users\\eddyt\\Desktop\\dapi\\risultati\\17_surebg.png",sure_bg)
#plt.imshow(sure_bg, cmap='gray')
dist_transform = cv2.distanceTransform(apertura,cv2.DIST_L2,5)
cv2.imwrite("C:\\Users\\eddyt\\Desktop\\dapi\\risultati\\17_dist_transf.png",dist_transform)
#plt.imshow(dist_transform, cmap='gray')
ret2, sure_fg = cv2.threshold(dist_transform,0.6*dist_transform.max(),255,0)
#sure_fg =cv2.erode(apertura,kernel,iterations=10)
#cv2.imwrite("C:\\Users\\eddyt\\Desktop\\dapi\\risultati\\17_surefg_thresh.png",sure_fg)
#plt.imshow(sure_fg, cmap='gray')
sure_fg = np.uint8(sure_fg)
incerte = cv2.subtract(sure_bg,sure_fg)
cv2.imwrite("C:\\Users\\eddyt\\Desktop\\dapi\\risultati\\17_unknown.png",incerte)
#plt.imshow(incerte, cmap='gray')
ret3, markers = cv2.connectedComponents(sure_fg)
cv2.imwrite("C:\\Users\\eddyt\\Desktop\\dapi\\risultati\\17_markers.png",markers)
#plt.imshow(markers)
markers[incerte==255] = 0
#plt.imshow(markers, cmap='jet')
markers = cv2.watershed(img,markers)
img[markers == -1] = [0,255,255]
img2 = color.label2rgb(markers, bg_label=0)



#cv2.imshow('Overlay on original image', img)
cv2.imwrite("C:\\Users\\eddyt\\Desktop\\dapi\\risultati\\17.png",img)
#cv2.imshow('Colored Grains', img2)


io.imsave("C:\\Users\\eddyt\\Desktop\\dapi\\risultati\\17_watershed.png", img2)
#cv2.imwrite("C:\\Users\\eddyt\\Desktop\\dapi\\risultati\\17_watershed.png", img2_img_8bit())
#cv2.waitKey(0)
props = measure.regionprops_table(markers, nuclei, 
                          properties=['label',
                                      'area', 'equivalent_diameter',
                                      'mean_intensity', 'solidity', 'orientation',
                                      'perimeter'])

import pandas as pd
df = pd.DataFrame(props)
#print(df.head())

df = df[df['area'] > 50]
#print(df.head())

#Conversione
pixels_to_um = 0.27
df['area_sq_microns'] = df['area'] * (pixels_to_um**2)
df['equivalent_diameter_microns'] = df['equivalent_diameter'] * (pixels_to_um)
#print(df.head())

df.to_csv('C:\\Users\\eddyt\\Desktop\\dapi\\risultati\misurazioni.csv')
