#from scipy import misc
#import imageio
from scipy import ndimage
#import numpy as np
import matplotlib.pyplot as plt

#lion_gray_blurred = ndimage.gaussian_filter(lion_gray, sigma=1.4)
def process_(lion_gray):
    lion_gray_blurred = ndimage.gaussian_filter(lion_gray, sigma=1.4)
    with open("sorted_values.txt","r+") as fp:
        for line in fp:
            #print(line[:-2])
            #print(len(line[:-2]))
            plt.imshow(lion_gray_blurred, cmap = plt.get_cmap(line[:-1]))
            print(plt.show())
