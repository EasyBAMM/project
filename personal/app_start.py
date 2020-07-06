from flask import (
    Flask,
    g, 
    redirect,
    render_template,
    request,
    session,
    url_for
)

import RPi.GPIO as GPIO
from time import sleep

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='huhjb1020@naver.com', password='8250'))

app = Flask(__name__)
app.secret_key = 'junbeom_personal_project'


@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

@app.route("/", methods=['GET', 'POST'])
def loginPage():
    if request.method == 'POST':
        session.pop('user_id', None)

        #get inputUser
        username = request.form['inputEmail']
        password = request.form['inputPassword']
        
        #check defineUser vs inputUser 
        userInput = [x for x in users if x.username == username] 

        #wrong email
        if not userInput:
            return redirect(url_for('home'))
        #right email
        else:
            user = userInput[0]

        #right password -> login success
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('home'))
        #wrong password -> login fail
        else:
            return redirect(url_for('loginPage'))

    return render_template("login.html")


@app.route("/index")
def home():
    if not g.user:
        return redirect(url_for('loginPage'))

    return render_template("index.html")

'''
# 모터 상태
STOP  = 0
FORWARD  = 1
BACKWARD = 2

# 모터 채널
CH1 = 0
CH2 = 1

# PIN 입출력 설정
OUTPUT = 1
INPUT = 0

# PIN 설정
HIGH = 1
LOW = 0

# 실제 핀 정의
#PWM PIN
ENA = 26  #37 pin
ENB = 0   #27 pin

#GPIO PIN
IN1 = 19  #37 pin
IN2 = 13  #35 pin
IN3 = 6   #31 pin
IN4 = 5   #29 pin

# 핀 설정 함수
def setPinConfig(EN, INA, INB):        
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)
    # 100khz 로 PWM 동작 시킴 
    pwm = GPIO.PWM(EN, 100) 
    # 우선 PWM 멈춤.   
    pwm.start(0) 
    return pwm

# 모터 제어 함수
def setMotorContorl(pwm, INA, INB, speed, stat):

    #모터 속도 제어 PWM
    pwm.ChangeDutyCycle(speed)  
    
    if stat == FORWARD:
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)
        
    #뒤로
    elif stat == BACKWARD:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)
        
    #정지
    elif stat == STOP:
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)

        
# 모터 제어함수 간단하게 사용하기 위해 한번더 래핑(감쌈)
def setMotor(ch, speed, stat):
    if ch == CH1:
        #pwmA는 핀 설정 후 pwm 핸들을 리턴 받은 값이다.
        setMotorContorl(pwmA, IN1, IN2, speed, stat)
    else:
        #pwmB는 핀 설정 후 pwm 핸들을 리턴 받은 값이다.
        setMotorContorl(pwmB, IN3, IN4, speed, stat)
  

# GPIO 모드 설정 
GPIO.setmode(GPIO.BCM)
      
#모터 핀 설정
#핀 설정후 PWM 핸들 얻어옴 
pwmA = setPinConfig(ENA, IN1, IN2)
pwmB = setPinConfig(ENB, IN3, IN4)

    
#제어 시작

# 앞으로 80프로 속도로
setMotor(CH1, 80, FORWARD)
setMotor(CH2, 80, FORWARD)
#5초 대기
sleep(5)

# 뒤로 40프로 속도로
setMotor(CH1, 40, BACKWARD)
setMotor(CH2, 40, BACKWARD)
sleep(5)

# 뒤로 100프로 속도로
setMotor(CH1, 100, BACKWARD)
setMotor(CH2, 100, BACKWARD)
sleep(5)

#정지 
setMotor(CH1, 80, STOP)
setMotor(CH2, 80, STOP)

# 종료
GPIO.cleanup()
'''

'''
STOP  = 0
FORWARD  = 1
BACKWARD = 2

# 모터 채널
CH1 = 0
CH2 = 1

# PIN 입출력 설정
OUTPUT = 1
INPUT = 0

# PIN 설정
HIGH = 1
LOW = 0

# 실제 핀 정의
#PWM PIN
ENA = 26  #37 pin
ENB = 0   #27 pin

#GPIO PIN
IN1 = 19  #37 pin
IN2 = 13  #35 pin
IN3 = 6   #31 pin
IN4 = 5   #29 pin

# 핀 설정 함수
def setPinConfig(EN, INA, INB):        
    GPIO.setup(EN, GPIO.OUT)
    GPIO.setup(INA, GPIO.OUT)
    GPIO.setup(INB, GPIO.OUT)
    # 100khz 로 PWM 동작 시킴 
    pwm = GPIO.PWM(EN, 100) 
    # 우선 PWM 멈춤.   
    pwm.start(0) 
    return pwm

# 모터 제어 함수
def setMotorContorl(pwm, INA, INB, speed, stat):

    #모터 속도 제어 PWM
    pwm.ChangeDutyCycle(speed)  
    
    if stat == FORWARD:
        GPIO.output(INA, HIGH)
        GPIO.output(INB, LOW)
        
    #뒤로
    elif stat == BACKWARD:
        GPIO.output(INA, LOW)
        GPIO.output(INB, HIGH)
        
    #정지
    elif stat == STOP:
        GPIO.output(INA, LOW)
        GPIO.output(INB, LOW)

        
# 모터 제어함수 간단하게 사용하기 위해 한번더 래핑(감쌈)
def setMotor(ch, speed, stat):
    if ch == CH1:
        #pwmA는 핀 설정 후 pwm 핸들을 리턴 받은 값이다.
        setMotorContorl(pwmA, IN1, IN2, speed, stat)
    else:
        #pwmB는 핀 설정 후 pwm 핸들을 리턴 받은 값이다.
        setMotorContorl(pwmB, IN3, IN4, speed, stat)

pwmA = None
pwmB = None

@app.route("/control")
def cotrol():
    if not g.user:
        return redirect(url_for('loginPage'))

    state = request.args.get("state", "error")
    
    if state == "On":
        print("On")
        # GPIO 모드 설정 
        GPIO.setmode(GPIO.BCM)
      
        #모터 핀 설정
        #핀 설정후 PWM 핸들 얻어옴 
        global pwmA, pwmB 
        try:
            pwmA = setPinConfig(ENA, IN1, IN2)
            pwmB = setPinConfig(ENB, IN3, IN4)
        except Exception as identifier:
            print(identifier)
            return "setPinConfig fail"

    elif state == "Off":
        print("Off")
        try:
            GPIO.cleanup()
        except Exception as identifier:
            print(identifier)
            return "gpio cleanup fail"
    elif state == "error":
        print("miss querystring")
    else:
        print("wrong querystring")
    
    return "control " + state

@app.route("/car")
def car():
    if not g.user:
        return redirect(url_for('loginPage'))

    state = request.args.get("state", "error")
    
    if state == "forward":
        print("forward")
        try:
            setMotor(CH1, 40, FORWARD)
            setMotor(CH2, 40, FORWARD)
            return "forward ok"
        except Exception as identifier:
            print(identifier)
            return "forward fail"

    elif state == "left":
        print("left")
        try:
            setMotor(CH1, 40, FORWARD)
            setMotor(CH2, 40, BACKWARD)
            return "left ok"
        except Exception as identifier:
            print(identifier)
            return "left fail"


    elif state == "stop":
        print("stop")
        try:
            setMotor(CH1, 80, STOP)
            setMotor(CH2, 80, STOP)
            return "stop ok"
        except Exception as identifier:
            print(identifier)
            return "stop fail"

    elif state == "right":
        print("right")
        try:
            setMotor(CH1, 40, BACKWARD)
            setMotor(CH2, 40, FORWARD)
            return "right ok"
        except Exception as identifier:
            print(identifier)
            return "right fail"

    elif state == "backward":
        print("backward")
        try:
            setMotor(CH1, 40, BACKWARD)
            setMotor(CH2, 40, BACKWARD)
            return "backward ok"
        except Exception as identifier:
            print(identifier)
            return "backward fail"

    elif state == "error":
        print("miss querystring")
    else:
        print("wrong querystring")
    
    return "car " + state

@app.route("/camera")
def camera():
    if not g.user:
        return redirect(url_for('loginPage'))

    state = request.args.get("state", "error")
    
    if state == "camera-left":
        print("camera-left")
    elif state == "camera-right":
        print("camera-right")
    elif state == "stop":
        print("stop")
    elif state == "error":
        print("miss querystring")
    else:
        print("wrong querystring")
    
    return "camera " + state


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
'''