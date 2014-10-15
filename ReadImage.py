#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     15-10-2014
# Copyright:   (c) Administrator 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import cv
def readImage():
    lena=cv.LoadImage("Lena.jpg")
    cv.NamedWindow("lena")
    cv.ShowImage("lena",lena)
    baboon=cv.LoadImage("Baboon.jpg")
    cv.NamedWindow("baboon")
    cv.ShowImage("baboon",baboon)
    cv.WaitKey(0)

def main():
    pass
    readImage()

if __name__ == '__main__':
    main()
