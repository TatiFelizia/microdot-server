# Configuracion inicial

import time
def do_connect():
    import network
    from time import time
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Cooperadora Alumnos', '')
        while not sta_if.isconnected():
            print(".", end = "")
            sleep(.05)
    print('network config:', sta_if.ifconfig())
    
from machine import Pin

led_1 = Pin(32, Pin.OUT)
led_2 = Pin(33, Pin.OUT)
led_3 = Pin(25, Pin.OUT)

do_connect()
