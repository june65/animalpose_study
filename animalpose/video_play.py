
import cv2
import glob
import sys

img_files = glob.glob('.\\output\\*.png')

if not img_files:
    print("no image")
    sys.exit()

cv2.namedWindow('a',cv2.WINDOW_NORMAL)
cv2.setWindowProperty('a', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

count = len(img_files)
index = 0
for f in img_files:
    print(f)
while True:
    img = cv2.imread(img_files[index])

    if img is None:     
        print("이미지를 불러오는데 실패했습니다.")
        break
        
    cv2.imshow('a', img)
    if cv2.waitKey(10) == 27:     
        break

    index += 1      
    if index >= count :
       break

cv2.destroyAllWindows()