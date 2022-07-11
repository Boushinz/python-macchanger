#!/bin/python

import subprocess 
import sys

print("\nMac address befire applying any change")
subprocess.Popen(["ifconfig", "eth0"], stdout = True)

subprocess.Popen(["ifconfig", "eth0", "down"], stdout = False)
subprocess.Popen(["ifconfig", "eth0", "hw", "ether", sys.argv[1]], stdout = False)
subprocess.Popen(["ifconfig", "eth0", "up"], stdout = False)

print("Mac address after spoofing")
subprocess.Popen(["ifconfig", "eth0"], stdout = True)
