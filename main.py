# -*- coding: utf-8 -*-
"""
Nika Sert

მხოლოდ ერთი ისიც სერთი"
"""
from PIL import Image
import pytesseract
import csv
import sys
import re
#If you use to GPIO please enalbe this module - dooropen
#import dooropen
from difflib import SequenceMatcher
import time
import os
import shutil
#import necessary modules
import cv2
import sys
import numpy as np
#onemli olmayan
import platform

try:
    #Kulanilan Platforma Gore Tesseracti cagirma.
    if platform.system() == "Windows":
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    else:
        pass
    # importing the cascade classifier for face and eye
    plate_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
    # check for input video if you need use to ip camera please enable Video Source 1
    #Video Source 1
    #cap = cv2.VideoCapture("rtsp://admin:Fener1907@192.168.43.108/H264?ch=1&subtype=0")
    #Video Source 2
    cap = input("Please Input Your source")
    #initialize input head, with source
    video = cv2.VideoCapture(cap)

    # Run an infinite loop, until user quit(press 'q')
    while True:

        # reading frame from the video source
        _, frame = video.read()

        # cinverting frame to Gray scale to pass on classifier
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect faces and return coordinates of rectangle
        # This is the section, where you need to work
        # To get more accurate result, you need to play with this parameters
        plate = plate_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)
        # make a rectangle around face detected
        for (x, y, w, h) in plate:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            platearea = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # extract the rectangle, containing face
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            image_name = roi_color
            text = pytesseract.image_to_string(image_name, lang='eng', config='--psm 12')
            text = re.sub(r"[\n\t\s]*", "", text)
            def similar(a, b):
                return SequenceMatcher(None, a, b).ratio()


            with open("file.csv") as f:
                dataset = f.read()
                albatoba = similar(text, dataset)
                print(albatoba)
                if not text:
                    cv2.imwrite('PlateNumber.jpg', roi_color)
                    os.system('python3 ColorChangePlate.py')
                    image_name = "PlateNumber.jpg"
                    text = pytesseract.image_to_string(image_name, lang='eng', config='--psm 12')
                    text = re.sub(r"[\n\t\s]*", "", text)
                    def similar(a, b):
                        return SequenceMatcher(None, a, b).ratio()
                    with open("file.csv") as f:
                        dataset = f.read()
                        albatoba = similar(text, dataset)
                        print(albatoba)
                        if albatoba > 0.115:
                            print("door open",text)
                            #dooropen.main()
                            time.sleep(5)
                        else:
                            print("car not found",text)

                else:
                    if albatoba > 0.115:
                        print("door open", text)
                        time.sleep(4)
                        #dooropen.main()
                    else:
                        print("Car Not Found", text)
            print(text)





            # As eye without a face doen't make any sense
            # so we search for eye, within the face only
            # this reduces the computational load an also increases accuracy
            # detect eyes and return coordinates of rectangle
            # make a rectangle around face detected

        # show the processed frame
        #cv2.imshow('Output', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            # Release the video object
            video.release()
            # close all open windows
            cv2.destroyAllWindows()
            exit(0)

except:
    pass
    # If 'q' pressed => Quit
