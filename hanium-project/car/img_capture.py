import cv2
import numpy as np

# 카메라 프레임 읽고 ROI 선택 후 ROI 파일 저장

img1 = None
win_name = 'Camera Matching'

cap = cv2.VideoCapture(0)              
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if cap.isOpened():
    while True:
        ret, frame = cap.read() 
        if ret:
            # 결과 출력
            cv2.imshow(win_name, frame)
            key = cv2.waitKey(1)
            if key == 27:    # Esc, 종료
                break          
            elif key == ord(' '): # 스페이스바를 누르면 ROI로 img1 설정
                x,y,w,h = cv2.selectROI(win_name, frame, False)
                if w and h:
                    img1 = frame[y:y+h, x:x+w]
                    cv2.imwrite("capture.jpg", img1)
                    break
else:
    print("can't open camera.")
cap.release()                          
cv2.destroyAllWindows()