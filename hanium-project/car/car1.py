# sudo pip3 install flask, serial, opencv-python==3.4.6.27
import cv2
from flask import Flask, render_template, Response
import serial

'''
###############################################################################
'''
# 라즈베리파이 카메라 설정
# 1. USB웹 캠이 아닌 picamera이면 2번을 꼮 수행
# 2. https://webnautes.tistory.com/1192 참고하여 /etc/modules 수정하여 /dev/video0 장치로 인식
# 카메라 장치 연결, debug 모드에선 동작X
cap = cv2.VideoCapture(-1) # 0 or -1

# 아두이노 연결 포트 설정단계
# 1. 아두이노 usb와 라즈베리파이를 usb로 연결 전
# 2. 라파 터미널에서 "ls /dev/tty*" 검색
# 3. 연결 후 2단계 다시 검색
# 4. 연결된 포트 확인 후 코드 수정
# 보통 직렬 포트의 장치 이름은 '/ dev / ttyACM0' 또는 '/ dev / ttyUSB1'
try:
    ser = serial.Serial('/dev/ttyACM0', 9600)
except Exception as error:
    print(error)

# flask 웹서버
app = Flask(__name__) 

'''
###############################################################################
'''

# 해당 URL로 접속 시 아래 코드 수행

# 아두이노와 라즈베리파이간의 시리얼통신 - send to arduino "forward"
@app.route('/car1_stop')
def stop():
    #send2arduino data - 0:"stop"
    s2a = "stop"
    s2a_encode = s2a.encode()

    try:  
        ser.write(s2a_encode)
    except Exception as error:
        print(error)
        return 'car1 stop fail'

    return "car1 stop ok" 

# 아두이노와 라즈베리파이간의 시리얼통신 - send to arduino "stop"
@app.route('/car1_forward') 
def forward():
    #send2arduino data - 1:"forward"
    s2a = "forward"
    s2a_encode = s2a.encode()

    try:  
        ser.write(s2a_encode)
    except Exception as error:
        print(error)
        return 'car1 forward fail'
    
    return 'car1 forward ok' 

# 카메라 웹 스트리밍
# https://www.hackster.io/ruchir1674/video-streaming-on-flask-server-using-rpi-ef3d75 참고
# https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/ 참고
def gen():
    if cap.isOpened():  
        while True:
            # 카메라 프레임 읽기
            ret, img = cap.read() 
            
            # 프레임 읽기 실패 시 루프 반복
            if ret is None:
                continue

            # 프레임 읽기 성공 시 JPEG 로 인코딩
            (flag, encodedImage) = cv2.imencode(".jpg", img) 

            # 인코딩 성공 체크
            if not flag:
                continue

            # 프레임을 바이트 형식으로 발생
            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')


@app.route("/video_feed")
def video_feed():
	# return the response generated along with the specific media
	# type (mime type)
	return Response(gen(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")


'''
###############################################################################
'''


if __name__ == '__main__':    
    app.run(host='0.0.0.0')
