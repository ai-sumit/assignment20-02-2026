import os
import sys
import time
import pywhatkit as w
import pyautogui
import keyboard as k

from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

# ========================
# Django Minimal Settings
# ========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    DEBUG=True,
    SECRET_KEY="secret",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    MIDDLEWARE=[
        "django.middleware.common.CommonMiddleware",
    ],
)

# ========================
# View Function
# ========================

@csrf_exempt
def home(request):
    result = ""

    if request.method == "POST":
        number = request.POST.get("number")
        message = request.POST.get("message")
        hour = int(request.POST.get("hour"))
        minute = int(request.POST.get("minute"))

        # WhatsApp Automation
        w.sendwhatmsg(number, message, hour, minute, tab_close=False)

        time.sleep(5)
        pyautogui.click(1050, 950)  # Adjust if needed
        k.press_and_release('enter')

        result = "Message Scheduled Successfully!"

    return HttpResponse(f"""
    <html>
    <head>
        <title>WhatsApp Automation</title>
        <style>
            body {{
                font-family: Arial;
                background: linear-gradient(to right, #25D366, #128C7E);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .box {{
                background: white;
                padding: 30px;
                border-radius: 15px;
                width: 400px;
                box-shadow: 0px 10px 25px rgba(0,0,0,0.2);
            }}
            input, textarea {{
                width: 100%;
                margin-top: 10px;
                padding: 8px;
                border-radius: 8px;
                border: 1px solid #ccc;
            }}
            button {{
                width: 100%;
                margin-top: 15px;
                padding: 10px;
                background: #25D366;
                color: white;
                border: none;
                border-radius: 10px;
                cursor: pointer;
            }}
        </style>
    </head>
    <body>
        <div class="box">
            <h2>📲 WhatsApp Message Sender</h2>
            <p style="color:green;">{result}</p>
            <form method="POST">
                <input type="text" name="number" placeholder="+91xxxxxxxxxx" required>
                <textarea name="message" placeholder="Type your message..." required></textarea>
                <input type="number" name="hour" placeholder="Hour (0-23)" required>
                <input type="number" name="minute" placeholder="Minute (0-59)" required>
                <button type="submit">Send Message 🚀</button>
            </form>
        </div>
    </body>
    </html>
    """)

# ========================
# URL Routing
# ========================

urlpatterns = [
    path("", home),
]

# ========================
# Run Server
# ========================

if __name__ == "__main__":
    execute_from_command_line([sys.argv[0], "runserver", "8000"])
