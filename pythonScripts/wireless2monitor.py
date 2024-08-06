#!/usr/bin/python

import os
import subprocess


subprocess.call(["sudo", "ifconfig", "wlan0", "down"])
subprocess.call(["sudo", "iwconfig",  "wlan0", "mode", "monitor"])
subprocess.call(["sudo", "ifconfig", " wlan0", " up"])

