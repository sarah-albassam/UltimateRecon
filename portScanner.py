import socket
import re
import sys
from queue import Queue
import threading
from datetime import datetime
import os

global userIp

queue = Queue()
def threadsFunction1(threads,ip,defaultPortStart = 1,defaultPortEnd = 65536):
    global userIp
    userIp = ip
    start(ip)
    print("[+] Scanning is in progress..")
    for port in range(defaultPortStart, defaultPortEnd+1):
        queue.put(port)
    thread_list = []
    for t in range(threads):
        thread = threading.Thread(target=portScan)
        thread_list.append(thread)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    end(ip)

def threadsFunction2(threads,ip,normalPortStart = 0,normalPortend = 1024):
    global userIp
    userIp = ip
    start(ip)
    print("[+] Scanning is in progress..")
    for port in range(normalPortStart, normalPortend+1):
        queue.put(port)
    thread_list = []
    for t in range(threads):
        thread = threading.Thread(target=portScan)
        thread_list.append(thread)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    end(ip)

def threadsFunction3(threads,ip,customPortStart ,customPortEnd):
    global userIp
    userIp = ip
    start(ip)
    print("[+] Scanning is in progress..")
    for port in range(customPortStart, customPortEnd+1):
        queue.put(port)
    thread_list = []
    for t in range(threads):
        thread = threading.Thread(target=portScan)
        thread_list.append(thread)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    end(ip)

def portScan():
    while not queue.empty():
        port = queue.get()
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                result = s.connect_ex((userIp, port))
                if result == 0:
                    print(f"[+] port {port} is open")
        except:
            pass

def start(ip):
    print("\n----------------------------------------------------------------")
    print(f"Scan on ({ip}) started at: {str(datetime.now())}")
    print("----------------------------------------------------------------\n")

def end(ip):
    print("\n----------------------------------------------------------------")
    print(f"Scan on ({ip}) ended at: {str(datetime.now())}")
    print("----------------------------------------------------------------\n")
