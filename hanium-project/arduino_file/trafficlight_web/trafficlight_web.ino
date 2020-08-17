#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>

#ifndef STASSID
#define STASSID "toz"
#define STAPSK  "toz13579"
#endif

const char *ssid = STASSID;
const char *password = STAPSK;

ESP8266WebServer server(80);

int redled = D7; // initialize digital pin 6.
int yellowled = D8; // initialize digital pin 5.
int greenled = D9; // initialize digital pin 3.


void setup(void) {
  pinMode(redled, OUTPUT);// set the pin with red LED as “output”
  pinMode(yellowled, OUTPUT); // set the pin with yellow LED as “output”
  pinMode(greenled, OUTPUT); // set the pin with green LED as “output”
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  if (MDNS.begin("esp8266")) {
    Serial.println("MDNS responder started");
  }

  server.on(F("/"), []() {
    server.send(200, "text/plain", "hello from esp8266!");
  });

  server.on("/trafficlight1-red", [](){
    Serial.print("trafficlight: ");
    Serial.println("red on");
    if( digitalRead(greenled) == HIGH ){
      digitalWrite(greenled, LOW);
      delay(500);
      digitalWrite(yellowled, HIGH);
      delay(1000);
      digitalWrite(yellowled, LOW);
      digitalWrite(redled, HIGH);
    }
    else {
      digitalWrite(redled, HIGH);
    }
    server.send(200, "text/plain", "trafficlight1-red ok!");
  });

  server.on("/trafficlight1-green", [](){
    Serial.print("trafficlight: ");
    Serial.println("green on");
    if( digitalRead(redled) == HIGH ){
      digitalWrite(redled, LOW);
      delay(500);
      digitalWrite(yellowled, HIGH);
      delay(1000);
      digitalWrite(yellowled, LOW);
      digitalWrite(greenled, HIGH);
    }
    else {
      digitalWrite(greenled, HIGH);
    }
    server.send(200, "text/plain", "trafficlight1-red ok!");
  });
  
  server.begin();
  Serial.println("HTTP server started");
}

void loop(void) {
  server.handleClient();
}
