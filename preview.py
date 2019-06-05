import cv2
import numpy as np
from PIL import Image
from Tkinter import Tk, Label, Button
from pyteser 
from time import sleep
#from espeak import espeak
import os

IMAGE_FILE = 'fonts_test.png'
cam = cv2.VideoCapture(09)
s, img = cam.read()

winName = "Movement Indicator"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)


while True:
    
  #cam = cv2.VideoCapture(0)
  #s, img = cam.read()
  

  s, img = cam.read()
  cv2.imshow( winName,img )

  key = cv2.waitKey(10)
  if key == 27:
      	
  #sleep(4)
  img = Image.open(IMAGE_FILE)
  words = image_to_string(img).strip()
 
  #words = words.replace(' ', '')
  print words
  text_file = open("Output.txt", "w")
  text_file.write(words)
  text_file.close()   
  os.system("espeak Output.txt --stdout | aplay")
  sleep(2)
    
    
    
print "ok"


