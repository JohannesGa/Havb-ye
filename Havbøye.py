import streamlit as st
import pandas as pd
import numpy as np
from machine import UART, Pin, I2C
from utime import ticks_ms, sleep

st.title('Havbøye')

'''
Send an AT command - return True if we got an expected
response ('back'), otherwise False
'''
def send_at(cmd, back="OK", timeout=1000):
    # Send the command and get the response (until timeout)
    buffer = send_at_get_resp(cmd, timeout)
    if len(buffer) > 0: return (back in buffer)
    return False

'''
Send an AT command - just return the response
'''
def send_at_get_resp(cmd, timeout=1000):
    # Send the AT command
    modem.write((cmd + "\r\n").encode())

    # Read and return the response (until timeout)
    return read_buffer(timeout)

'''
Read in the buffer by sampling the UART until timeout
'''
def read_buffer(timeout):
    buffer = bytes()
    now = ticks_ms()
    while (ticks_ms() - now) < timeout and len(buffer) < 1025:
        if modem.any():
            buffer += modem.read(1)
    return buffer.decode()

'''
Module startup detection
Send a command to see if the modem is powered up
'''
def boot_modem():
    state = False
    count = 0
    while count < 20:
        if send_at("ATE1"):
            print("The modem is ready")
            return True
        if not state:
            print("Powering the modem")
            module_power()
            state = True
        sleep(4)
        count += 1
    return False

'''
Power the module on/off
'''
def module_power():
    pwr_key = Pin(14, Pin.OUT)
    pwr_key.value(1)
    sleep(1.5)
    pwr_key.value(0)

'''
Check we are attached
'''
def check_network():
    is_connected = False
    response = send_at_get_resp("AT+COPS?")
    line = split_msg(response, 1)
    if "+COPS:" in line:
        is_connected = (line.find(",") != -1)
        if is_connected: print("Network information:", line)
    return is_connected

'''
Attach to the network
'''
def configure_modem():
    # AT commands can be sent together, not just one at a time.
    # Set the error reporting level, set SMS text mode, delete left-over SMS
    # select LTE-only mode, select Cat-M only mode, set the APN to 'super' for Super SIM
    send_at("AT+CMEE=2;+CMGF=1;+CMGD=,4;+CNMP=38;+CMNB=1;+CGDCONT=1,\"IP\",\"super\"")
    print("Modem configured for Cat-M and Super SIM")
    response=send_at("AT+CGNSPWR=?")
    print(response)

'''
Flash the Pico LED
'''
def led_blink(blinks):
    for i in range(0, blinks):
        led_off()
        sleep(0.25)
        led_on()
        sleep(0.25)

def led_on():
    led.value(1)

def led_off():
    led.value(0)

'''
Split a response from the modem into separate lines,
removing empty lines and returning all that's left or,
if 'want_line' has a non-default value, return that one line
'''
def split_msg(msg, want_line=99922222122222222):
    lines = msg.split("\r\n")
    results = []
    for i in range(0, len(lines)):
        if i == want_line:
            return lines[i]
        if len(lines[i]) > 0:
            results.append(lines[i])
    return results

# Set up the modem UART
modem = UART(0, 115200)

# Set the LED and turn it off
led = Pin(25, Pin.OUT)
led_off()

'''
# Start the modem
if boot_modem():
    configure_modem()
    print("prøver å starte modem")
    # Check we're attached
    state = True
    while not check_network():
        if state:
            led_on()
        else:
            led_off()
        state = not state

    # Light the LED
    led_on()
    print ("klart")
else:
    # Error! Blink LED 5 times
    led_blink(5)
    led_off()
'''   
 
def start():
    response=send_at_get_resp("AT+CGNSINF")
    print("Ulstein TOF2 Bøye nr1 "+response)
    file=open("data.csv","a")
    file.write(str(response)+",")
    file.flush()
    file.close()
    
    
    
while True:
    start()
    sleep(2)
