#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""
                Ultrasonic sensor
"""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""
                Via LoRa and WiFi
"""""""""""""""""""""""""""""""""""""""""""""""""""
#LIBRARIES
import network, sensor, wifi, lora

#AUTHORINFO
_author_ = "Joel Chapon"
_email_  = "joel.chapon@student.kdg.be"
_date_   = "2021-02-24"
_status_ = "Finished"

#CONFIGURATIONS
LORA = lora.connect()

# connect to wifi when lora doesnt work
if not LORA.has_joined():
    wifi.connect()

# when lora works send it via lora
while True:
    afstand = sensor.distance()
    if not LORA.has_joined():
        wifi.send(afstand)
    else: lora.send(afstand)
