'''
Created on Oct 7, 2019

@author: Vincent
'''

import numpy as np
import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(1)
 
# Check if camera opened successfully
if (cap.isOpened() == False): 
    print("Unable to read camera feed")
    
# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

while(True):
    ret, frame = cap.read()
 
    if ret == True: 
 
        # Display the resulting frame    
        cv2.imshow('frame',frame)
 
        # Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
 
    # Break the loop
    else:
        break 
 
# Release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows() 