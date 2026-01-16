import socket
import threading
import queue
import sys

print("=========================================")
print("Welcome to PortScanner\n")

if len(sys.argv) == 2:
    thread_count = 5
elif len(sys.argv) == 4 and sys.argv[2] == "-t":
    thread_count = int(sys.argv[3])
else:
    print("Usage ...")
    sys.exit()

ip = sys.argv[1]

q = queue.Queue()

def scan(port):
    s = socket.socket()
    s.settimeout(0.5)
    try:
        s.connect((ip, port))
        print(f"[OPEN]   {port}")
    except:
        pass
    s.close()

def worker():
    while not q.empty():
        port = q.get()
        scan(port)
        q.task_done()

for port in range(1, 1025):
    q.put(port)

for _ in range(thread_count):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

q.join()

print("\n=========================================")
print("Scan Completed")
print("Developed by sudo_0xksh")
