import cv2

def convertToRGB(img): 
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

test = cv2.imread('test2.jpg')

gray_img = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
