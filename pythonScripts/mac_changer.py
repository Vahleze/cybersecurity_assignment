#!/usr/bin/python

import os
import subprocess

subprocess.call("sudo ifconfig wlan0 down", shell=True)
subprocess.call("sudo ifconfig wlan0 hw ether 00:22:44:66:99:20", shell=True)
subprocess.call("sudo ifconfig wlan0 up", shell=True)



