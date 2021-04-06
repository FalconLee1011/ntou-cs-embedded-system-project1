/* 
  Hw1 by t15
  @ Mar.12 2020
*/ 

#include <Wire.h>

#include <LWiFi.h>
#include <DHT.h>
#include <PubSubClient.h>
#include <SeeedOLED.h>

#include "config.h"

#define MQTT_SUB_TOPIC "TESTE88D94"
#define MQTT_SERVER_IP "140.121.198.196"
#define MQTT_SERVER_PORT 1883
#define MQTT_CLIENT_ID "linklt7697_111dsf-x"

#define RELAY 10

DHT DHT(A0, DHT11);
WiFiClient mqttClient;
PubSubClient client(mqttClient);

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
  initMQTT();
}

void loop(){
  upload();
  client.loop();
}

void initMQTT(){
  while(!client.connected()){
    if(client.connect(MQTT_CLIENT_ID)){
      Serial.println("MQTT has been connected.");
      putStringToOLED("MQTT Online");
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

void upload(){
  String t = String(DHT.readTemperature());
  String h = String(DHT.readHumidity());
  String json = "{\"temp\":" + t + ", \"humd\":" + h +"}";
  char json_char[json.length() + 1];
  json.toCharArray(json_char, json.length() + 1);
  client.publish(MQTT_SUB_TOPIC, json_char);
  putStringToOLED("Published.");
  delay(1000);
  putStringToOLED("Publishing...");
}

void putStringToOLED(String S, int x, int y, boolean cl){
  if(cl) SeeedOled.clearDisplay();
  SeeedOled.setTextXY(0,0);
  unsigned int len = S.length() + 1;
  char c[len];
  S.toCharArray(c, len);
  SeeedOled.putString(c);
}
 
