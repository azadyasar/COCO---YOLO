# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:23:25 2020

@author: u21w97
"""

import glob
filepaths = glob.glob("ec2-user/dataset/coco/train2014/*.jpg")

outfile = open('ec2-user/dataset/coco/train2014/coco_img.txt', 'a+')
for filepath in filepaths:
  outfile.write(filepath + '\n')
outfile.close()

filepaths = glob.glob("ec2-user/dataset/coco/val2014/*.jpg")

outfile = open('ec2-user/dataset/coco/val2014/coco_img.txt', 'a+')
for filepath in filepaths:
  outfile.write(filepath + '\n')
outfile.close()