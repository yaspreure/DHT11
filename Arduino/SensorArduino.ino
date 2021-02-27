#include <dht.h>

const int DHT_pin = 2;

unsigned long ms_per_s = 3L;
unsigned long minutes = 60;
unsigned long sampling_time = minutes * ms_per_s * 60;


int dht_sig = 0;

dht DHT;

void setup() {
   
    Serial.begin(9600);
}

void loop() {
    dht_sig = DHT.read11(DHT_pin);
    
    Serial.print(DHT.temperature);
    Serial.print(DHT.humidity);

    delay(sampling_time);
}
