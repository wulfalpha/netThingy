
import sys
import socket
import getopt
import threading
import subprocess
import os
import os.path
import struct

from netaddr import IPNetwork, IPAddress
from ctypes import *

#global Variables
listen = False
command = False
dist = os.uname()
target = ""
port = 0

#help Text
def man()

	print("netThingy is a network Diagnostic Tool")
	print("Commands are Rather simple")
	print(" -p is to ping a specific ip address or website")