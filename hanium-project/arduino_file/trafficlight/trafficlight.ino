int redled =6; // initialize digital pin 6.
int yellowled =5; // initialize digital pin 5.
int greenled =3; // initialize digital pin 3.
int pwm = 255;

void setup()
{
pinMode(redled, OUTPUT);// set the pin with red LED as “output”
pinMode(yellowled, OUTPUT); // set the pin with yellow LED as “output”
pinMode(greenled, OUTPUT); // set the pin with green LED as “output”
}

void loop()
{
  //pwm(0 ~ 255) 1st: 50,  2nd: 100, 3rd: 175, 4th: 255 
  analogWrite(greenled, pwm);// turn on green LED
  delay(5000);// wait 5 seconds
  analogWrite(greenled, 0);   // turn off green LED
  delay(500);// wait 0.5 seconds
  
  analogWrite(yellowled, pwm);// turn on yellow LED
  delay(5000);// wait 0.5 seconds
  analogWrite(yellowled, 0);// turn off yellow LED
  delay(500);// wait 0.5 seconds
  
  analogWrite(redled, pwm);// turn on red LED
  delay(5000);// wait 5 seconds
  analogWrite(redled, 0);// turn off red LED
  delay(500);// wait 0.5 seconds
}
