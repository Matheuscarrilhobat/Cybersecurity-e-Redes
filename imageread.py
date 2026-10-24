import cv2

img = cv2.imread('image readable/image.jpg') # caminho do arquivo de imagem/input image path here
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (500, 500)) #altera o tamanho da imagem/resize the image

_, result = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

adaptive_result = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 41, 5)

cv2.imshow('result', result)
cv2.imshow('adaptive_result', adaptive_result)
cv2.imshow('original', img)
cv2.waitKey(0)

