# 🐝 Honeypot Login Trap (Python)

A lightweight, educational honeypot that simulates a fake FTP login portal. It captures and logs attacker behavior (IP, username, password) for security analysis.

## 🔒 Purpose

This project mimics a login system to trick attackers into revealing their tactics — without giving them real access.

## 💻 Features

- Simulates a secure FTP login prompt
- Logs all connections and login attempts
- Written in pure Python using sockets
- Easy to expand (SSH, HTTP, etc.)

## 📦 Technologies Used

- Python 3
- `socket` for networking
- `logging` for event capture

## 🧪 How It Works

1. Run `python3 honeypot.py`
2. Attacker connects via `nc 127.0.0.1 2121`
3. They enter a username + password
4. Info is saved to `honeypot.log` for later analysis

## 🗂 Example Log Entry
