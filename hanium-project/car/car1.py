# sudo pip3 install flask, serial, opencv-python==3.4.6.27
import cv2
from flask import Flask, render_template, Response
import numpy as np
import serial
import threading
import time

'''
###############################################################################
'''

# 아두이노 연결 포트 설정단계
# 1. 아두이노 usb와 라즈베리파이를 usb로 연결 전
# 2. 라파 터미널에서 "ls /dev/tty*" 검색
# 3. 연결 후 2단계 다시 검색
# 4. 연결된 포트 확인 후 코드 수정
# 보통 직렬 포트의 장치 이름은 '/ dev / ttyACM0' 또는 '/ dev / ttyUSB1'
try:
    ser = serial.Serial('/dev/ttyACM0', 9600)
    print("serial success")
except Exception as error:
    print(error)

# flask 웹서버
app = Flask(__name__) 

'''
###############################################################################
'''

# 차의 status 값 
# car_move: "initial", "forward", "force_stop", "stop"
# trafficlight: "initial", "green", "red"
car_move = "initial"
trafficlight = "initial"

# 해당 URL로 접속 시 아래 함수 안 코드 수행 ex)"http://ip주소:port(5000)/car1_stop")
# 아두이노와 라즈베리파이간의 시리얼통신 - send to arduino "stop" and car_move status change
@app.route('/car1_stop')
def stop():
    global car_move

    #send2arduino data - 0:"stop"
    s2a = "stop"
    s2a_encode = s2a.encode()

    try:  
        ser.write(s2a_encode)
        car_move = "force_stop"
        print("serial car1_stop success")
    except Exception as error:
        print(error)
        return 'car1 stop fail'

    return "car1 stop ok" 
# def stop(): end

# 아두이노와 라즈베리파이간의 시리얼통신 - send to arduino "forward" and car_move status change
@app.route('/car1_forward') 
def forward():
    global car_move
    
    #send2arduino data - 1:"forward"
    s2a = "forward"
    s2a_encode = s2a.encode()

    try:  
        ser.write(s2a_encode)
        car_move = "forward"
        print("serial car1_forward success")
    except Exception as error:
        print(error)
        return 'car1 forward fail'
    
    return 'car1 forward ok' 
# def forward(): end

'''
###############################################################################
'''

# 카메라 웹 스트리밍
# https://www.hackster.io/ruchir1674/video-streaming-on-flask-server-using-rpi-ef3d75 참고
# https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/ 참고
# https://opencv-python.readthedocs.io/en/latest/index.html 참고
# 객체 검출

img1 = "./capture.jpg" # 검출할 이미지 등록
img1 = cv2.imread(img1, cv2.IMREAD_COLOR)

win_name = 'camera Matching'
MIN_MATCH = 10

# ORB 검출기 생성
detector = cv2.ORB_create(1000) # 파라미터: 검출할 최대 특징 수
# FLANN 추출기 생성
# 인덱스 파라미터 설정(고정)
FLANN_INDEX_LSH = 6
index_params = dict( algorithm = FLANN_INDEX_LSH,
                     table_number = 6,
                     key_size = 12,
                     multi_probe_level = 1 )
# 검색 파라미터 설정                     
search_params = dict( checks=32 )
# FlannMatcher 생성
matcher = cv2.FlannBasedMatcher(index_params, search_params)

# 라즈베리파이 카메라 설정
# 1. USB웹 캠이 아닌 picamera이면 2번을 꼭 수행
# 2. https://webnautes.tistory.com/1192 참고하여 /etc/modules 수정하여 /dev/video0 장치로 인식
# 카메라 장치 연결, debug 모드에선 동작X, 프레임 크기 축소
cap = cv2.VideoCapture(0) # 0(for USB) or -1(for picamera)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# detect_traffic():
# : 메인스레드가 아닌 서브쓰레드로 카메라를 백그라운드로 실행하고 객체를 검출한다.
# : 읽어온 카메라 이미지를 전역변수 outputFrame에 저장한다.
# gen():
# : outputFrame 에 저장된 값이 있다면 , 이 데이터를 웹이 읽을 수 있는 byte형식으로 인코딩한다.
# @app.route("/video_feed"):
# 해당 URL로 접속 시 "http://ip주소:port(5000)/video_feed") 카메라 데이터를 볼 수 있다.

# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful for multiple browsers/tabs
# are viewing tthe stream)
outputFrame = None
lock = threading.Lock()


def detect_traffic():
    global outputFrame, lock, car_move, trafficlight
    if cap.isOpened():  
        while True:
            # 카메라 프레임 읽기
            ret, frame = cap.read()
            if img1 is None:  # 등록된 이미지 없음, 카메라 바이패스
                res = frame
                print("img1 is None")
            else:             # 등록된 이미지 있는 경우, 매칭 시작
                if ret is None:     # 프레임 읽기 실패 시 루프 반복
                    continue
                # 미리 지정한 img1 와 img2(=카메라) 비교
                img2 = frame
                gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
                gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
                # 키포인트와 디스크립터 추출
                kp1, desc1 = detector.detectAndCompute(gray1, None)
                kp2, desc2 = detector.detectAndCompute(gray2, None)

                # k=2로 knnMatch, match 없으면 카메라 프레임 전달
                try:
                    matches = matcher.knnMatch(desc1, desc2,k=2)
                except Exception as error:
                    # print(error)
                    # acquire the lock, set the output frame, and release the lock
                    with lock:
                        outputFrame = frame
                    continue
                # 이웃 거리의 75%로 좋은 매칭점 추출
                ratio = 0.75
                good_matches = [m[0] for m in matches \
                if len(m) == 2 and m[0].distance < m[1].distance * ratio]
                print('good matches:%d/%d' %(len(good_matches),len(matches)))
                # 모든 매칭점 그리지 못하게 마스크를 0으로 채움
                matchesMask = np.zeros(len(good_matches)).tolist()
                # 좋은 매칭점 최소 갯수 이상 인 경우
                if len(good_matches) > MIN_MATCH:
                    # 좋은 매칭점으로 원본과 대상 영상의 좌표 구하기
                    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good_matches ])
                    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good_matches ])
                    # 원근 변환 행렬 구하기
                    mtrx, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
                    accuracy=float(mask.sum()) / mask.size
                    #print("accuracy: %d/%d(%.2f%%)"% (mask.sum(), mask.size, accuracy))
                    accuracy_text = "accuracy: " + str(round(accuracy, 2)) + " %"
                    if accuracy > 0.5:
                        cv2.putText(img2, accuracy_text, (50,440), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0))
                    else:
                        cv2.putText(img2, accuracy_text, (50,440), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255))

                    if accuracy > 0.8 and car_move == "forward":  # accuracy 90% 이상인 경우
                        trafficlight = "red"
                        car_move = "stop"
                        print("trafficlight: red");print("car_move: stop")
                        #send2arduino data - 0:"stop"
                        s2a = "stop"
                        s2a_encode = s2a.encode()
                        try:  
                            ser.write(s2a_encode)
                            print("serial car1_stop success")
                        except Exception as error:
                            print(error)
                    elif accuracy < 0.3 and car_move == "stop":
                        trafficlight = "green"
                        car_move = "forward"
                        print("trafficlight: green");print("car_move: forward")
                        #send2arduino data - 1:"forward"
                        s2a = "forward"
                        s2a_encode = s2a.encode()
                        try:  
                            ser.write(s2a_encode)
                            print("serial car1_forward success")
                        except Exception as error:
                            print(error)

                    if mask.sum() > MIN_MATCH:  # 정상치 매칭점 최소 갯수 이상 인 경우
                        # 이상점 매칭점만 그리게 마스크 설정
                        matchesMask = mask.ravel().tolist()
                        # 원본 영상 좌표로 원근 변환 후 영역 표시
                        h,w, = img1.shape[:2]
                        pts = np.float32([ [[0,0]],[[0,h-1]],[[w-1,h-1]],[[w-1,0]] ])
                        dst = cv2.perspectiveTransform(pts,mtrx)
                        img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)
                    # if mask.sum() > MIN_MATCH: end

                # if len(good_matches) > MIN_MATCH: end
                
                # 마스크로 매칭점 그리기
                res = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None, \
                                    matchesMask=matchesMask,
                                    flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
            # else end

            # acquire the lock, set the output frame, and release the lock
            with lock:
                outputFrame = res.copy()

        # while end         
    # if cap.isOpened(): end
    else:
        print("can't open camera.")
# def detect_traffic(): end

def gen():
    # grab global references to the output frame and lock variables
	global outputFrame, lock

    # loop over frames from the output stream
	while True:
		# wait until the lock is acquired
		with lock:
			# check if the output frame is available, otherwise skip
			# the iteration of the loop
			if outputFrame is None:
				continue

			# encode the frame in JPEG format
			(flag, encodedImage) = cv2.imencode(".jpg", outputFrame)

			# ensure the frame was successfully encoded
			if not flag:
				continue

		# yield the output frame in the byte format
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')
# def gen(): end

@app.route("/video_feed")
def video_feed():
	# return the response generated along with the specific media
	# type (mime type)
	return Response(gen(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")


'''
###############################################################################
'''

# 메인 스레드 시작
# : detect_traffic() 서브스레드 시작
# : flask 웹 서버 시작
if __name__ == '__main__':
    # start a thread that will perform trafficlight detect
    t = threading.Thread(target=detect_traffic)
    t.daemon = True
    try:
        t.start()
        print("sub Thread: detect_traffic run")
    except Exception as error:
        print(error)
    app.run(host='0.0.0.0', threaded=True)

# release the video stream pointer and program end
cap.release()
print("program End")


'''
###############################################################################
'''