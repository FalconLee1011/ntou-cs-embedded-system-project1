/* 
  Hw1 by t15
  @ Mar.12 2020
*/ 

#include <Wire.h>

#include <LWiFi.h>
#include <DHT.h>
#include <PubSubClient.h>
#include <SeeedOLED.h>

#include <config.h>

#define MQTT_SUB_TOPIC "TESTE88D94"
#define MQTT_SERVER_IP "140.121.198.196"
#define MQTT_SERVER_PORT 1883
#define MQTT_CLIENT_ID "linklt7697_111dsf-x"

#define RELAY 10

DHT DHT(A0, DHT11);
WiFiClient mqttClient;
PubSubClient client(mqttClient);

void mqttCallback(char* topic, byte* payload, unsigned int len);
void putStringToOLED(String S, int x=0, int y=0, boolean cl=true);

void setup(){
  Serial.begin(9600);
  Wire.begin();
  SeeedOled.clearDisplay();
  SeeedOled.setNormalDisplay();
  SeeedOled.setPageMode();
  SeeedOled.setTextXY(0,0);
  pinMode(RELAY, OUTPUT);
  SeeedOled.putString("Hello");
  while (WiFi.begin(SSID, PASS) != WL_CONNECTED){
    Serial.println("Could not connect to " + String(SSID) + " Retrying...");
    delay(1000);
  }
  Serial.println("Connected to " + String(SSID) + " with IP address " + String(WiFi.localIP().toString()));
  putStringToOLED(String(WiFi.localIP().toString()));
  DHT.begin();
  client.setServer(MQTT_SERVER_IP, MQTT_SERVER_PORT);
  client.setCallback(mqttCallback);
  initMQTT();
}

void loop(){
  client.loop();
}

void initMQTT(){
  while(!client.connected()){
    if(client.connect(MQTT_CLIENT_ID)){
      Serial.println("MQTT has been connected.");
      putStringToOLED("MQTT Online");
      client.subscribe(MQTT_SUB_TOPIC);
    }
    else{
      Serial.print("MQTT connection cannot be established, error ");
      Serial.println(client.state());
      Serial.println("Retry in 5 seconds...");
      delay(5000);
      Serial.println("Reconnecting...");
    }
  }
}

void mqttCallback(char* topic, byte* payload, unsigned int len){
//  SeeedOled.clearDisplay();
  char raw0 = ((char*)payload)[0];
  String message = "[" + String(MQTT_SUB_TOPIC) + "] " + String(raw0);
  Serial.println(message);
  putStringToOLED(message);
  switch(raw0){
    case '0':
      digitalWrite(RELAY, 0);
      putStringToOLED("relay 0");
      break;
    case '1':
      digitalWrite(RELAY, 1);
      putStringToOLED("relay");
      break;
    default:
      break; 
  }
}

void putStringToOLED(String S, int x, int y, boolean cl){
  if(cl) SeeedOled.clearDisplay();
  SeeedOled.setTextXY(0,0);
  unsigned int len = S.length() + 1;
  char c[len];
  S.toCharArray(c, len);
  SeeedOled.putString(c);
}
 