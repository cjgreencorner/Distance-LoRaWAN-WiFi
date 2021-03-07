#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""
                Ultrasonic sensor
"""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""
 For measuring distance between object and itself.
"""""""""""""""""""""""""""""""""""""""""""""""""""

#AUTHORINFO
_author_ = "Joel Chapon"
_email_  = "joel.chapon@student.kdg.be"
_status_ = "Finished"
_date_   = "2021-02-24"

#IMPORTS
from machine import UART

#CONFIGURATIONS
uart = UART(1)
uart.init(9600, bits=8, parity=None, stop=1, timeout_chars=100, pins=('P3', 'P4'))

while True:
    header_bytes = uart.read(1)
    while(header_bytes != b'\xff'):
        header_bytes=uart.read(1)
    data_high = int(uart.read(1)[0])
    data_low = int(uart.read(1)[0])
    data_sum = int(uart.read(1)[0])
    sum = data_high + data_low
    if (sum == data_sum + 1):
        distance = (data_high*256 + data_low)
        calc = "{:2.2f}".format(distance)
        print(calc + " mm distance")
