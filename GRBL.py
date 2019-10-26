# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:29:28 2019

@author: Le Quang Dung
"""

import serial
import time
import serial.tools.list_ports

s=serial
def connect_grbl():
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        if "USB-SERIAL CH340" in desc:
            s=serial.Serial(port, 115200, timeout=3)
            s.write('\r\n\r\n'.encode('utf-8'))
            fb=(s.readline()).decode()
            s.flushInput()
            s.write(("G91"+'\n').encode('utf-8'))
            fb=(s.readline()).decode()
            s.write(("S1000"+'\n').encode('utf-8'))
            fb=(s.readline()).decode()
            if fb[0:2]=="ok":
                s.close()
                return port
    return "no"

def disconnect_grbl(s):
    if s.is_open==True:
        s.close()
    
def init_reset_grbl(s):
    s.write(("G01 Z-30 F200"+'\r\n').encode())  
    fb=(s.readline()).decode()
    print(fb)
    
def auto_level_grbl(s):
    fb=""
    s.write(("G91 G38.2 Z40 F150"+'\n').encode('utf-8'))
    while fb[0:2]!="ok":
        fb=(s.readline()).decode()
        
def cycle_run(s):
#    Close Vaccuum Motor
    s.write(("M5"+'\r\n').encode())  
    fb=(s.readline()).decode()
    #print(fb)
    #Back to First Position
    s.write(("G01 X2 Y2.2 F500"+'\r\n').encode())  
    fb=(s.readline()).decode()
    #print(fb)    
    #Move Z 0.15mm
    #s.write(("G01 Z0.15 F100"+'\r\n').encode())  
    #fb=(s.readline()).decode()
    #print(fb)
    #Back to Step 1, Table return to normal
    s.write(("G01 X-2 Y-1.1 F500"+'\r\n').encode())  
    fb=(s.readline()).decode()
    #print(fb)
#    time.sleep(0.5)
    #Step1: Lever let paper down to table
    s.write(("G01 Y-0.9 F250"+'\r\n').encode())  
    fb=(s.readline()).decode()
    #print(fb)
    #Open Vaccuum Motor
    s.write(("M3"+'\r\n').encode())  
    fb=(s.readline()).decode()
    #print(fb)
    #Stop to capture Image
    s.write(("G01 Y-0.3 F300"+'\r\n').encode())  
    fb=(s.readline()).decode()
    #print(fb)
#    time.sleep(2)
    
    