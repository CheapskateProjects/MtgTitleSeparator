"""
This code will read card files from given folder. It will then separate, grayscale and threshold title partion of that image for later ocr process. 
Result image contains only the title part

created   May 2017
by CheapskateProjects

---------------------------
The MIT License (MIT)
Copyright (c) 2017 CheapskateProjects
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import sys
import numpy as np
import cv2
from os import listdir
from os import makedirs
from os import path

# Define title section
y1=60
y2=110
x1=60
x2=580

if not path.isdir("titles"):
    makedirs("titles")
for f in listdir("perspective_fix"):
    print f
    filename="perspective_fix/" + f
    img = cv2.imread(filename)
    # Grayscale to remove color variations
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Take only title part of the image
    title = gray[y1:y2, x1:x2]
    # Threshold to remove background
    flag, thresh = cv2.threshold(title, 100, 255, cv2.THRESH_BINARY)
    filename2="titles/" + f
    cv2.imwrite(filename2, thresh)
