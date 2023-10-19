import os
import sys
import random

if len(sys.argv) != 2:
    print("Введите: python3 parent.py N")
    sys.exit(1)
    
try:
    N = int(sys.argv[1])
except ValueError:
    print("N должно быть целым числом")
    sys.exit(1)

parent_pid = os.getpid()

count = N
while count > 0:
    child = os.fork()

    if child > 0:
        print(f"Parent [{parent_pid}]: I ran children process with PID {child}")
    else:
        random_arg = str(random.randint(5, 10))
        os.execve("child.py", ["child.py", random_arg], {})
    if child > 0:
        count -= 1

count = N

while count > 0:
    child_pid, exit_status = os.wait()
    print(f"Parent[{parent_pid}]: Child with PID {child_pid} terminated. Exit Status {exit_status}.")
    if exit_status != 0:
        child = os.fork()
        if child > 0:
            print(f"Parent [{parent_pid}]: I ran children process with PID {child}")
        else:
            random_arg = str(random.randint(5, 10))
            os.execve("child.py", ["child.py", random_arg], {})
    else:
        count -= 1
    
os._exit(os.EX_OK)  
