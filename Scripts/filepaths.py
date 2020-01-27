# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:23:25 2020

@author: u21w97
"""

import glob
filepaths = glob.glob("/home/ec2-user/dataset/coco/images/train2017/*.jpg")

outfile = open('/home/ec2-user/dataset/coco/images/train2017/coco_img.txt', 'a+')
for filepath in filepaths:
  outfile.write(filepath + '\n')
outfile.close()

filepaths = glob.glob("/home/ec2-user/dataset/coco/images/val2017/*.jpg")

outfile = open('/home/ec2-user/dataset/coco/images/val2017/coco_img.txt', 'a+')
for filepath in filepaths:
  outfile.write(filepath + '\n')
outfile.close()