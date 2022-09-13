#! /usr/bin/python3

#The Purpose of this exercise is to show that it is possible to use python code to execute an external program on your machine.
#The code presented here is intended to run an application known as netstat
#The prerequisits are that netsat is already installed and can run on your machine prior to running this code.
#To install netstat use sudo apt-get install net-tools
#test that it works by netering netstat into you bash cli
#IF all is well running this code should run netstat an external program

import sys
sys.version_info[0]

lab_exercise = "LaunchExternalCommand"
lab_type = "lab-code"
python_version = ("%s.%s.%s" % (sys.version_info[0], sys.version_info[1], sys.version_info[2]))
print("Exercise: %s" % (lab_exercise))
print("Type: %s" % (lab_type))
print("Python: %s\n" % (python_version))

#====================================

#CODE1: Import the os module
import os

#CODE2: Query the hostname of current machine
os.system("hostname")

#CODE3: Execute the netstat process on the current machine
with os.popen('netstat -an') as netstat_in: # <2>
  for entry in netstat_in: # <3>
    if 'ESTAB' in entry: # <4>
      print(entry, end='')
