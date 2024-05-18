# Q.4 Write a Python script that extracts the default gateway address from the output of ifconfig or ipconfig and displays it to the user

import subprocess
import sys
import re

def get_default_gateway():
    if sys.platform == 'darwin':  # macOS
        command = 'netstat -nr | grep default'
    elif sys.platform == 'linux':  # Linux
        command = 'ip route show | grep default'
    else:  # Windows
        command = 'ipconfig'

    output = subprocess.check_output(command, shell=True).decode('utf-8')
    pattern = r'default\s+via\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    match = re.search(pattern, output)
    if match:
        return match.group(1)
    else:
        return None

default_gateway = get_default_gateway()
if default_gateway:
    print(f'Default gateway: {default_gateway}')
else:
    print('Failed to extract default gateway')