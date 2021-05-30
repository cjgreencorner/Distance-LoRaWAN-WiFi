#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""
                Connect to LoRa
"""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""
              Send a float via LoRa
"""""""""""""""""""""""""""""""""""""""""""""""""""
#IMPORTS
from network import LoRa
import socket
import time
import ubinascii
import ustruct

#AUTHORINFO
_author_ = "Joel Chapon"
_email_  = "joel.chapon@student.kdg.be"
_date_   = "2021-02-24"
_status_ = "Finished"

# function to connect with LoRaWAN
def connect():
    count = 0
    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

    # create an OTAA authentication parameters, change them to the provided credentials
    app_eui = ubinascii.unhexlify('?')
    app_key = ubinascii.unhexlify('?')
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

    while not lora.has_joined():
        count = count + 1
        time.sleep(2.5)
        print('LoRa trying to join.')
        if count == 3:
            break

    print('LoRa is connected')
    return(lora)

# Function to send the float
def send(distance):
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    s.setblocking(True)
    packet = ustruct.pack('f', distance)
    s.send(packet)
    print ("Unpacked value is:", ustruct.unpack('f',packet)[0])
    s.setblocking(False)
