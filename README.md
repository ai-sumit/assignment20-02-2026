# 🚀 Assignment Project – 20-02-2026

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Automation](https://img.shields.io/badge/Project-Automation-orange)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Project Overview

This repository contains three Python-based mini projects:

1. WhatsApp Auto Message Bot  
2. Blink Photo Capture System  
3. Cosmic Wikipedia Search App  

Each project demonstrates automation, computer vision, and API integration using Python.

---

# 1️⃣ 📲 WhatsApp Auto Message Bot

## 📖 Description
This project sends automated WhatsApp messages using Python.  
It uses the **pywhatkit** library to send scheduled messages through WhatsApp Web.

## 🛠 Technologies Used
- Python
- pywhatkit
- datetime

## 🖼 Demo Image
![WhatsApp Automation](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*4n7XGz2d7R6pujISiFDUFw.png)

## 💻 Sample Code

```python
import pywhatkit as kit
from datetime import datetime

phone_number = "+91XXXXXXXXXX"
message = "Hello! This is an automated message 🚀"

now = datetime.now()
hour = now.hour
minute = now.minute + 2

kit.sendwhatmsg(phone_number, message, hour, minute)
