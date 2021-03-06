#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""
                Connect via WiFi
"""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""
    Connect the LoPy via WiFi and send float
"""""""""""""""""""""""""""""""""""""""""""""""""""
#IMPORTS
from network import WLAN
import urequests as requests
import machine, pycom, time

#AUTHORINFO
_author_ = "Joel Chapon"
_email_  = "joel.chapon@student.kdg.be"
_date_   = "2021-02-24"
_status_ = "Finished"

#CONFIGURATIONS
aio_key = "??"
username = "cj_greencorner"
feed_name = "distance"

# connect to wifi
def connect():
    pycom.heartbeat(False)
    wlan = WLAN(mode=WLAN.STA)
    wlan.connect(ssid='telenet-82DF7B9', auth=(WLAN.WPA2, '?'))
    while not wlan.isconnected():
        machine.idle()
    print("WiFi connected succesfully")
    print(wlan.ifconfig())

# send the float to Adafruit
def send(distance):
    url = 'https://io.adafruit.com/api/v2/' + username + '/feeds/' + feed_name + '/data'
    body = {'value': distance}
    headers = {'X-AIO-Key': aio_key, 'Content-Type': 'application/json'}
    try:
        r = requests.post(url, json=body, headers=headers)
        print(r.text)
        r.close()
    except Exception as e:
        print(e)
    time.sleep(10)
