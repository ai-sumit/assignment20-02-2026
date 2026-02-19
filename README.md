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
2. Cosmic Wikipedia Search App  
3. Blink Photo Capture System  

Each project demonstrates automation, computer vision, and API integration using Python.

---

# 📲 Project 1 – WhatsApp Auto Message Bot

## 📖 Description
This project sends automated WhatsApp messages using Python.  
It uses the **pywhatkit** library to send scheduled messages through WhatsApp Web.

## 🛠 Technologies Used
- Python
- pywhatkit
- datetime

## 🖼 Demo Image
![WhatsApp Automation](https://i.ibb.co/VcjLg926/image.png)

## 💻 Sample Code

```python
import pywhatkit as kit
from datetime import datetime

phone_number = "+91XXXXXXXXXX"
message = "Hello! This is an automated message 🚀"

now = datetime.now()
hour = now.hour
minute = now.minute + 2

kit.sendwhatmsg(phone_number, message, hour, minute) python
```

# Project 2 – Cosmic Wikipedia Search App

📖 Description

Cosmic Wikipedia is a Python-based search application that retrieves summarized information about any person, place, or topic using the Wikipedia API.

Key Features:

API integration

User input handling

Text processing

Information retrieval system

🛠 Technologies Used

Python

Wikipedia Library

🖼 Demo Image

💻 Sample Code
import wikipedia

query = input("Enter topic to search: ")

try:
    result = wikipedia.summary(query, sentences=5)
    print("\n🔎 Result:\n")
    print(result)
except wikipedia.exceptions.DisambiguationError:
    print("Multiple results found. Please be more specific.")
except wikipedia.exceptions.PageError:
    print("No page found. Try another topic.")

👁 Project 3 – Blink Photo Capture System
📖 Description

Blink Photo Capture System is a computer vision project that captures a photo automatically when a blink is detected using a webcam.

Key Features:

Real-time camera access

Image capture automation

OpenCV integration

Basic computer vision processing

🛠 Technologies Used

Python

OpenCV

NumPy

🖼 Demo Image

💻 Sample Code
import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    cv2.imshow("Blink Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("blink_capture.jpg", frame)
        break

camera.release()
cv2.destroyAllWindows()
