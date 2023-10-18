#!/usr/bin/python3
import os
import sys
import time
import random

child_pid = os.getpid()
parent_pid = os.getppid()

print(f"Child[{child_pid}]: I am started. My PID {child_pid}. Parent PID {parent_pid}.")

S = int(sys.argv[1])    
time.sleep(S)

random_status = random.randint(0, 1)
print(f"Child[{child_pid}]: I am ended. PID {child_pid}. Parent PID {parent_pid}.")
os._exit(random_status)
