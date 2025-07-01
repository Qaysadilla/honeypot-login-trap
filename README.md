# 🎯 Honeypot Login Trap (Python)

A lightweight honeypot project that mimics a fake FTP login system. Designed for educational use to understand attacker behavior by capturing IPs and login attempts using Python sockets and logging.

## 🔐 Features

- Simulates a basic FTP login
- Logs all connections and credentials
- Easy to run with no external dependencies
- Pure Python + `socket` + `logging`

## 💻 How to Use

1. Run the honeypot server:
   ```bash
   python3 honeypot.py
   ```

2. Simulate an attacker using nc (netcat):   
   ```bash
   nc 127.0.0.1 2121
   ```

3. Try a fake login when prompted:
   ```
   Username: hacker123
   Password: letmein
   ```

4. Check the honeypot log for recorded data:
   ```bash
   cat honeypot.log
   ```

   Example:
   ```
   2025-06-30 23:12:45 - Connection from ('127.0.0.1', 53742)
   2025-06-30 23:12:47 - Login attempt - Username: hacker123, Password: letmein
   ```
