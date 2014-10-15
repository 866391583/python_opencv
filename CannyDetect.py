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
import sys
def cannyDetect():
    src=cv.LoadImage("Lena.jpg",0)
    dst=cv.CreateImage(cv.GetSize(src),src.depth,src.nChannels)
    cv.Canny(src,dst,50,150,3)
    cv.NamedWindow("src",1)
    cv.NamedWindow("dst",1)
    """dfhdjf"""
    cv.ShowImage("src",src)
    cv.ShowImage("dst",dst)
    """kdfkdkf"""
    cv.WaitKey(0)
    cv.DestroyWindow("src")
    cv.DestroyWindow("dst")
    sys.exit(0)

def main():
    pass
    cannyDetect()

if __name__ == '__main__':
    main()
