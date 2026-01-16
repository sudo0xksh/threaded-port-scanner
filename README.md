# ⚡🔥 Threaded Port Scanner 🔥⚡

Threaded Port Scanner is a Python CLI tool that scans the first 1024 TCP ports
using multiple threads to save time, energy, and sanity 🧠⚙️

If waiting feels slow, this tool exists for you.

---

## 👀 Overview

Scanning ports one by one is painful 🐢  
So this scanner uses threads to speed things up 🚀

You give it a target IP.
It checks ports 1 to 1024.
Open ports get printed.
Closed ports get ignored.

Fast. Simple. Effective.

---

## 🚀 Features

- Scans ports 1 to 1024 automatically 🔢  
- Uses multi-threading for speed ⚡  
- Adjustable thread count using command-line flag 🧵  
- Clean OPEN port output 🟢  
- Lightweight and dependency-free 🪶  

---

## ⚙️ How It Works

All ports from 1 to 1024 are added to a queue.
Multiple worker threads pick ports from the queue
and attempt a TCP connection.

If the connection succeeds, the port is OPEN.
If it fails, the scanner moves on silently.

No noise. No drama.

---

## 🧪 Usage

To scan with default thread count (5 threads), run  
python portscanner.py 192.168.1.1

To specify custom thread count, run  
python portscanner.py 192.168.1.1 -t 20

More threads mean faster scans — and more noise on the network 😈

---

## 📤 Example Output

[OPEN]   22  
[OPEN]   80  
[OPEN]   443  

That’s all you need to see.

---

## 📦 Requirements

- Python 3.x  
- Network access  
- No external libraries required  

Pure Python doing pure work.

---

## 🧠 What You Learn From This Project

- Basics of multi-threading in Python  
- Queue-based task distribution  
- How real port scanners speed things up  
- TCP connection behavior  
- Why concurrency matters in recon  

---

## 🗿 Final Words

Single-threaded scans test patience.
Multi-threaded scans test networks.

Choose wisely 😎🔥
