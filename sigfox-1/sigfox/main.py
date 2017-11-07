from pysense import Pysense
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01

import time
from network import Sigfox
import socket

py = Pysense()

si = SI7006A20(py)

lt = LTR329ALS01(py)


# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# make the socket blocking
s.setblocking(True)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)

while True:
    temperature = int(round(si.temperature()*100))
    light = lt.light()[0]
    print(str(temperature) + ":"+str(light))
    messageBytes=bytes((temperature & 0xff, ((temperature >> 8) & 0xff),light & 0xff, ((light >> 8) & 0xff)))
    s.send(messageBytes)
    time.sleep(60)
