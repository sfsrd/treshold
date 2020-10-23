import cv2

def make_smaller(img, percent, text):
	width = int(img.shape[1] * percent / 100)
	height = int(img.shape[0] * percent / 100)
	dim = (width, height)
	rs = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	cv2.imshow(text, rs)

img = cv2.imread('test_img.jpg')
# ret, img1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# ret, img2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# ret, img3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# ret, img4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# ret, img5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
# ret, img6 = cv2.threshold(img,127,255,cv2.THRESH_MASK)
# make_smaller(img1, 30, 'THRESH_BINARY_INV')
# make_smaller(img2, 30, 'THRESH_BINARY')
# make_smaller(img3, 30, 'THRESH_TRUNC')
# make_smaller(img4, 30, 'THRESH_TOZERO')
# make_smaller(img5, 30, 'THRESH_TOZERO_INV')
# make_smaller(img6, 30, 'THRESH_MASK')

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img1_1 = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 3)
img1_2 = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 3)
img1_3 = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)
img1_4 = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 3)
make_smaller(img1_1, 30, 'THRESH_BINARY_GAUSSIAN')
make_smaller(img1_2, 30, 'THRESH_BINARY_INV_GAUSSIAN')
make_smaller(img1_3, 30, 'THRESH_BINARY_MEAN_C')
make_smaller(img1_4, 30, 'THRESH_BINARY_INV_MEAN_C')



cv2.waitKey(0)