#!/usr/bin/python

###################
# ImageCompare.py #
###################

# This module contains methods to quickly and
# easily compare two images to see how different
# they are.  This was created to be used as
# something of a motion detector.  The idea was
# That a videoconference is working if the image
# being shown changes noticeably.

# Detecting whether an image has changed was
# implemented in two ways:  Using a Histogram
# comparison (HistoCompare) and doing a pixel-
# by-pixel comparison.  It was generally found
# that the histograms of two different images
# are generally more different than a pixel-by-
# pixel comparison, but the difference is small.

from PIL import Image


# Easily the most important feature of this module
# is the fact that it requires the Python Imaging
# Library (PIL) in order to be used.  The PIL can
# be found at:
# http://www.pythonware.com/products/pil/index.htm

################
# HistoCompare #
################

# HistoCompare takes in two histograms (generated
# using PIL) as well as an optional string and
# an optional double.  the histograms are those
# of the images that you want to compare.
# If you pass in "pct" as the mode, HistoCompare
# will return the percentage difference between
# the histograms (out of the total value of the
# most valuable histogram).
# If any other string is passed in as the mode,
# then HistoCompare will return True if the
# percentage difference is less than alpha, and
# False otherwise

def HistoCompare(im1, im2, mode="pct", alpha=.01):
    if im1.size == im2.size and im1.mode == im2.mode:
        h1 = im1.histogram()
        h2 = im2.histogram()
        SumIm1 = 0.0
        SumIm2 = 0.0
        diff = 0.0
        for i in range(len(h1)):
            SumIm1 += h1[i]
            SumIm2 += h2[i]
            diff += abs(h1[i] - h2[i])
        maxSum = max(SumIm1, SumIm2)
        if mode == "pct":
            return diff / (2 * maxSum)
        if diff > alpha * maxSum:
            return False
        return True
    return False


################
# PixelCompare #
################

# PixelCompare takes in two single band images
# (generated using PIL) as well as an optional
# string and an optional double.
# If you pass in "pct" as the mode, PixelCompare
# will return the percentage difference between
# the images (out of the total value of the
# most valuable histogram).
# If any other string is passed in as the mode,
# then PixelCompare will return True if the
# percentage difference is less than alpha, and
# False otherwise

def PixelCompare(im1, im2, mode="pct", alpha=.01):
    if im1.size == im2.size and im1.mode == im2.mode:
        randPix = im1.getpixel((0, 0))
        maxSum = []
        diff = []
        for channel in range(len(randPix)):
            diff += [0.0]
            maxSum += [0.0]
        width = im1.size[0]
        height = im1.size[1]
        for i in range(width):
            for j in range(height):
                pixel1 = im1.getpixel((i, j))
                pixel2 = im2.getpixel((i, j))
                for channel in range(len(randPix)):
                    maxSum[channel] += 255
                    diff[channel] += abs(pixel1[channel] - pixel2[channel])
        if mode == "pct":
            ret = ()
            for channel in range(len(randPix)):
                ret += (diff[channel] / maxSum[channel],)
            return ret
        for channel in range(len(randPix)):
            if diff[channel] > alpha * maxSum[channel]:
                return False
        return True
    return False


def XORCompare(im1, im2, mode="pct", alpha=.01):
    if im1.size == im2.size and im1.mode == im2.mode:
        XORCount = []
        randPix = im1.getpixel((0, 0))
        for channel in range(len(randPix)):
            XORCount += [0.0]
        width = im1.size[0]
        height = im1.size[1]
        imXOR = ImageXOR(im1, im2)
        maxSum = 0.0
        for i in range(width):
            for j in range(height):
                pixel = imXOR.getpixel((i, j))
                for channel in range(len(pixel)):
                    XORCount[channel] += pixel[channel]
                maxSum += 255
        if mode == "pct":
            ret = ()
            for channel in range(len(randPix)):
                ret += (XORCount[channel] / maxSum,)
            return ret
        for channel in range(len(randPix)):
            if XORCount[channel] > alpha * maxSum:
                return False
        return True
    return False


def imageCompare(im1, im2, mode="pct", alpha=.01):
    if im1.size == im2.size and im1.mode == im2.mode:
        HistComp = HistoCompare(im1, im2, "pct")
        PixComp = PixelCompare(im1, im2, "pct")
        XORComp = XORCompare(im1, im2, "pct")
        if mode == "pct":
            return (HistComp, PixComp, XORComp)
        if mode == "alpha":
            if HistComp > alpha:
                return False
            for pct in PixComp:
                if pct > alpha:
                    return False
            for pct in XORComp:
                if pct > alpha:
                    return False
            return True
    return False


def FindDifferences(im1, im2):
    if im1.size == im2.size and im1.mode == im2.mode:
        width = im1.size[0]
        height = im2.size[1]
        ret = Image.new(im1.mode, im1.size)
        for i in range(width):
            for j in range(height):
                pixel1 = im1.getpixel((i, j))
                pixel2 = im2.getpixel((i, j))
                putPix = ()
                for channel in range(len(pixel1)):
                    putPix += (abs(pixel1[channel] - pixel2[channel]),)
                ret.putpixel((i, j), putPix)
        return ret
    return False


def ImageXOR(im1, im2):
    if im1.size == im2.size and im1.mode == im2.mode:
        width = im1.size[0]
        height = im2.size[1]
        ret = Image.new(im1.mode, im1.size)
        for i in range(width):
            for j in range(height):
                pixel1 = im1.getpixel((i, j))
                pixel2 = im2.getpixel((i, j))
                putPix = ()
                for channel in range(len(pixel1)):
                    putPix += (pixel1[channel] ^ pixel2[channel],)
                ret.putpixel((i, j), putPix)
        return ret
    return False


def GetKey(size, mode, seed=0):
    import random
    key = Image.new(mode, size)
    random.seed(seed)
    for i in range(size[0]):
        for j in range(size[1]):
            if mode == "RGB":
                key.putpixel((i, j), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            if mode == "CMYK":
                key.putpixel((i, j), (random.randint(0, 255), random.randint(0, 255), random.randint(-128, 127)))
            if mode == "L":
                key.putpixel((i, j), random.randint(0, 255))
    return key


def MonitorPicture(file, method="all", tolerance=.01):
    image = Image.open(file)
    image2 = image
    while True:
        if method == "all":
            if imageCompare(image, image2, "alpha", tolerance) == False:
                return "BING!"
        elif method == "Histogram" or method == "hist":
            if HistoCompare(image, image2, "alpha", tolerance) == False:
                return "BING!"
        elif method == "Pixel-by-pixel" or method == "pix":
            if PixelCompare(image, image2, "alpha", tolerance) == False:
                return "BING!"
        elif method == "XOR" or method == "xor":
            if XORCompare(image, image2, "alpha", tolerance) == False:
                return "BING!"
        else:
            return False, "Please enter a valid method: all, hist, pix or xor"
        image2 = image
        image = Image.open(file)


def EncryptImage(file, seed=0):
    image = Image.open(file)
    key = GetKey(image.size, image.mode, seed)
    enc = ImageXOR(image, key)
    enc.save(file)
