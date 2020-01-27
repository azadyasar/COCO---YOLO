# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:24:43 2020

@author: u21w97
"""


classes = ["person","bicycle","car","motorcycle","airplane","bus","train",
	   "truck","boat","traffic light","fire hydrant","stop sign","parking meter",
	   "bench","bird","cat","dog","horse","sheep","cow","elephant","bear","zebra",
	   "giraffe","backpack","umbrella","handbag","tie","suitcase","frisbee","skis",
	   "snowboard","sports ball","kite","baseball bat","baseball glove","skateboard",
	   "surfboard","tennis racket","bottle","wine glass","cup","fork","knife","spoon",
	   "bowl","banana","apple","sandwich","orange","broccoli","carrot","hot dog","pizza",
	   "donut","cake","chair","couch","potted plant","bed","dining table","toilet","tv",
	   "laptop","mouse","remote","keyboard","cell phone","microwave","oven","toaster","sink",
	   "refrigerator","book","clock","vase","scissors","teddy bear","hair drier","toothbrush"]

outfile = open('ec2-user/coco.names', 'a+')
for cl in classes:
  outfile.write(cl + '\n')
outfile.close()
print (len(classes))