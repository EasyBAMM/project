#define EA 3  // 모터드라이버 EA 핀, 아두이노 디지털 3번 핀에 연결
#define EB 11  // 모터드라이버 EB 핀, 아두이노 디지털 11번 핀에 연결
#define M_IN1 4  // 모터드라이버 IN1 핀, 아두이노 디지털 4번 핀에 연결
#define M_IN2 5  // 모터드라이버 IN2 핀, 아두이노 디지털 5번 핀에 연결
#define M_IN3 13  // 모터드라이버 IN3 핀, 아두이노 디지털 13번 핀에 연결
#define M_IN4 12  // 모터드라이버 IN4 핀, 아두이노 디지털 12번 핀에 연결
#define R_Sensor 8  // 오른쪽 트랙킹(추적)센서 모듈 DO 핀, 아두이노 우노 보드의 8번 핀에 연결
#define C_Sensor 9  // 가운데 트랙킹(추적)센서 모듈 DO 핀, 아두이노 우노 보드의 9번 핀에 연결
#define L_Sensor 10  // 왼쪽 트랙킹(추적)센서 모듈 DO 핀, 아두이노 우노 보드의 10번 핀에 연결
int motorA_vector = 1;  // 모터의 회전방향이 반대일 시 0을 1로, 1을 0으로 바꿔주면 모터의 회전방향이 바뀜.
int motorB_vector = 1;  // 모터의 회전방향이 반대일 시 0을 1로, 1을 0으로 바꿔주면 모터의 회전방향이 바뀜.
int motor_speed = 100;  // 모터 스피드 0 ~ 255
String status;


void setup()  // 초기화
{
  Serial.begin(9600);
  pinMode(EA, OUTPUT);  // EA 핀 출력 설정
  pinMode(EB, OUTPUT);  // EB 핀 출력 설정
  pinMode(M_IN1, OUTPUT);  // IN1 핀 출력 설정
  pinMode(M_IN2, OUTPUT);  // IN2 핀 출력 설정
  pinMode(M_IN3, OUTPUT);  // IN3 핀 출력 설정
  pinMode(M_IN4, OUTPUT);  // IN4 핀 출력 설정
  pinMode(R_Sensor, INPUT);  // 오른쪽 센서 D0 핀 입력 설정
  pinMode(C_Sensor, INPUT);  // 가운데 센서 D0 핀 입력 설정
  pinMode(L_Sensor, INPUT);  // 왼쪽 센서 D0 핀 입력 설정
  delay(3000);  // 갑작스러운 움직임을 막기위한 3초간 지연
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0)  // Serial에 데이터가 들어오면
  {
    //From RPi to Arduino
    status = Serial.readStringUntil('\n');// 데이터를 문자열로 읽어들여 상태변경
    Serial.println("status: " + status);
  }

  //status == forward
  if(status == "forward")
  {
    Serial.println("status: forward");
    //   if (digitalRead(L_Sensor) == 0)
    // {
    //   //Serial.println("left sensor");
    //   motorA_con( motor_speed );// 모터A 정방향
    //   //Serial.println("rightspeed: " + motor_speed);
    //   motorB_con( -motor_speed );// 모터B 역방향
    //   //Serial.println("leftspeed: " + motor_speed);
    // }
    // else if (digitalRead(R_Sensor) == 0)
    // {
    //   //Serial.println("right sensor");
      
    //   motorA_con( -motor_speed );  // 모터A 역방향
    //   motorB_con( motor_speed );  // 모터B 정방향
    // }
    // else if (digitalRead(C_Sensor) == 0) // 만약 가운데 센서가 감지되면
    // {
    //   //Serial.println("center sensor");

    //   motorA_con( motor_speed );// 모터A 정방향
    //   motorB_con( motor_speed );// 모터B 정방향
    // }
    // else {
    //   Serial.println("stop");

    //   motorA_con( 0 );// 모터A stop
    //   motorB_con( 0 );// 모터B stop
    // }

  }
  else if(status == "stop")
  {
      Serial.println("status: stop");
      // motorA_con( 0 );// 모터A stop
      // motorB_con( 0 );// 모터B stop
  }
  else
  {
    Serial.println("status: nothing");
  }

  delay(1000);
}

void motorA_con(int speed)
{
  if(speed > 0)
  {
    digitalWrite(M_IN1, HIGH);
    digitalWrite(M_IN2, LOW);
  }
  else if(speed < 0)
  {
    digitalWrite(M_IN1, LOW);
    digitalWrite(M_IN2, HIGH);
  }
  else
  {
    digitalWrite(M_IN1, LOW);
    digitalWrite(M_IN2, LOW);
  }
  analogWrite(EA, abs(speed));
}

void motorB_con(int speed)
{
  if(speed > 0)
  {
    digitalWrite(M_IN4, HIGH);
    digitalWrite(M_IN3, LOW);
  }
  else if(speed < 0)
  {
    digitalWrite(M_IN4, LOW);
    digitalWrite(M_IN3, HIGH);
  }
  else
  {
    digitalWrite(M_IN4, LOW);
    digitalWrite(M_IN3, LOW);
  }
  analogWrite(EB, abs(speed));
}
