#include <ArduinoJson.h>
#include <Wire.h>
#ifndef I2C_SDA
#define I2C_SDA SDA
#endif
#ifndef I2C_SCL
#define I2C_SCL SCL
#endif

#include "IGA.h"
IGA input_iga;
#include "ILB.h"
ILB input_ilb;
#include "IWA.h"
IWA input_iwa;


void setup() {
    Serial.begin(115200);
    delay(1000);
    Serial.printf("\nApp Standard\n");

    Wire.setPins(I2C_SDA, I2C_SCL);
    Wire.begin();

    if (input_ilb.begin()) {
        Serial.println("ILB initialized successfully.");
    } else {
        Serial.println("Failed to initialize ILB!");
        exit(0);
    }
    if (input_iwa.begin()) {
        Serial.println("IWA initialized successfully.");
    } else {
        Serial.println("Failed to initialize IWA!");
        exit(0);
    }
    if (input_iga.begin()) {
        Serial.println("IGA initialized successfully.");
    } else {
        Serial.println("Failed to initialize IGA!");
        exit(0);
    }
}

void loop() {
    StaticJsonDocument<1024> doc;
    JsonObject root = doc.to<JsonObject>();

    input_iwa.getJSON(root);
    input_iga.getJSON(root);
    input_ilb.getJSON(root);

    DynamicJsonDocument outputDoc(1024);
    for (JsonPair kvp : doc.as<JsonObject>()) {
      const char* key = kvp.key().c_str();
      JsonArray array = kvp.value().as<JsonArray>();
      for (JsonObject object : array) {
        const char* name = object["name"];
        double value = object["value"];
        outputDoc[key][name] = value;
      }
    }
    serializeJsonPretty(outputDoc, Serial);
    Serial.println();

    delay(1000);
}
