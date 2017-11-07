import machine
import math
import network
import os
import time
import utime
from machine import RTC
from machine import SD
from machine import Timer
from L76GNSS import L76GNSS
from pytrack import Pytrack
import struct

from network import Sigfox
import socket

# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# make the socket blocking
s.setblocking(True)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)



import gc

time.sleep(2)
gc.enable()

# setup rtc
rtc = machine.RTC()
rtc.ntp_sync("pool.ntp.org")
utime.sleep_ms(750)
print('\nRTC Set from NTP to UTC:', rtc.now())
utime.timezone(7200)
print('Adjusted from UTC to EST timezone', utime.localtime(), '\n')
py = Pytrack()
l76 = L76GNSS(py, timeout=30)
chrono = Timer.Chrono()
chrono.start()
#sd = SD()
#os.mount(sd, '/sd')
#f = open('/sd/gps-record.txt', 'w')
while (True):

    coord = l76.coordinates()
    #coord = (43.345543, 7.890123)
    lat=coord[0]
    lon=coord[1]
    if lat is not None:
        byteArray=bytearray(struct.pack("f",lat))
        byteArray.extend(bytearray(struct.pack("f",lon)))
        #f.write("{} - {}\n".format(coord, rtc.now()))
        print("{} - {} - {}".format(len(byteArray), rtc.now(), gc.mem_free()))
        # send some bytes
        s.send(byteArray)
    print("sleep")
    time.sleep(60)
