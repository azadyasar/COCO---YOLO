# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:23:25 2020

@author: u21w97
"""

import glob
filepaths = glob.glob("/content/gdrive/My Drive/Small_COCO/train2014/*.jpg")

outfile = open('/content/gdrive/My Drive/Small_COCO/train2014/coco_img.txt', 'a+')
for filepath in filepaths:
  outfile.write(filepath + '\n')
outfile.close()

filepaths = glob.glob("/content/gdrive/My Drive/Small_COCO/val2014/*.jpg")

outfile = open('/content/gdrive/My Drive/Small_COCO/val2014/coco_img.txt', 'a+')
for filepath in filepaths:
  outfile.write(filepath + '\n')
outfile.close()