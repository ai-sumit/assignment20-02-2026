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
        <title>WhatsApp Automation - Sumit Haldar</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            }}

            body {{
                background: #111b21;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }}

            .whatsapp-container {{
                width: 100%;
                max-width: 480px;
                background: #0b141a;
                border-radius: 30px;
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
                overflow: hidden;
                border: 1px solid #222e35;
            }}

            /* WhatsApp Header */
            .whatsapp-header {{
                background: #202c33;
                padding: 20px 25px;
                display: flex;
                align-items: center;
                gap: 15px;
                border-bottom: 1px solid #2a3942;
            }}

            .whatsapp-logo {{
                background: #00a884;
                width: 45px;
                height: 45px;
                border-radius: 12px;
                display: flex;
                align-items: center;
                justify-content: center;
            }}

            .whatsapp-logo i {{
                font-size: 28px;
                color: white;
            }}

            .header-text {{
                flex: 1;
            }}

            .header-text h1 {{
                color: #e9edef;
                font-size: 18px;
                font-weight: 600;
                letter-spacing: 0.3px;
            }}

            .header-text p {{
                color: #8696a0;
                font-size: 13px;
                margin-top: 3px;
            }}

            .creator-name {{
                background: #0b141a;
                padding: 5px 12px;
                border-radius: 20px;
                border: 1px solid #2a3942;
                color: #00a884;
                font-size: 13px;
                font-weight: 500;
            }}

            .creator-name i {{
                color: #ff3b5c;
                font-size: 10px;
                margin: 0 3px;
            }}

            /* Main Content */
            .whatsapp-content {{
                padding: 25px;
                background: #0b141a;
            }}

            /* Chat Message Result */
            .chat-message {{
                background: #005c4b;
                color: #e9edef;
                padding: 12px 18px;
                border-radius: 12px 12px 4px 12px;
                margin-bottom: 25px;
                display: inline-block;
                max-width: 90%;
                font-size: 14px;
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
                animation: popIn 0.3s ease;
            }}

            .chat-message i {{
                margin-right: 8px;
                color: #8a8f99;
            }}

            @keyframes popIn {{
                0% {{ opacity: 0; transform: translateY(10px); }}
                100% {{ opacity: 1; transform: translateY(0); }}
            }}

            /* Form Labels */
            .input-label {{
                color: #8696a0;
                font-size: 13px;
                font-weight: 500;
                margin-bottom: 8px;
                display: flex;
                align-items: center;
                gap: 8px;
                letter-spacing: 0.3px;
            }}

            .input-label i {{
                color: #00a884;
                width: 18px;
                font-size: 14px;
            }}

            /* Form Fields */
            .input-group {{
                margin-bottom: 20px;
            }}

            .input-field {{
                width: 100%;
                background: #202c33;
                border: 1px solid #2a3942;
                border-radius: 12px;
                padding: 14px 16px;
                color: #e9edef;
                font-size: 15px;
                transition: all 0.2s;
            }}

            .input-field:focus {{
                outline: none;
                border-color: #00a884;
                background: #2a3942;
            }}

            .input-field::placeholder {{
                color: #5f6c74;
                font-size: 14px;
            }}

            textarea.input-field {{
                min-height: 100px;
                resize: vertical;
            }}

            /* Time Row */
            .time-row {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 15px;
                margin-bottom: 10px;
            }}

            /* Send Button */
            .send-btn {{
                width: 100%;
                background: #00a884;
                border: none;
                border-radius: 12px;
                padding: 16px;
                color: white;
                font-size: 16px;
                font-weight: 600;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 12px;
                cursor: pointer;
                transition: background 0.2s;
                margin-top: 15px;
            }}

            .send-btn:hover {{
                background: #06cf9c;
            }}

            .send-btn:active {{
                transform: scale(0.98);
            }}

            .send-btn i {{
                font-size: 18px;
            }}

            /* Message Preview */
            .message-preview {{
                background: #182229;
                border-radius: 12px;
                padding: 16px;
                margin-top: 25px;
                border-left: 3px solid #00a884;
            }}

            .preview-title {{
                color: #8696a0;
                font-size: 12px;
                text-transform: uppercase;
                letter-spacing: 1px;
                margin-bottom: 10px;
            }}

            .preview-number {{
                color: #e9edef;
                font-size: 14px;
                font-weight: 500;
                margin-bottom: 5px;
            }}

            .preview-number i {{
                color: #00a884;
                margin-right: 8px;
                font-size: 12px;
            }}

            .preview-message {{
                color: #aebac1;
                font-size: 13px;
                line-height: 1.5;
                padding-left: 22px;
            }}

            /* Footer */
            .whatsapp-footer {{
                background: #111b21;
                padding: 15px 25px;
                border-top: 1px solid #222e35;
                display: flex;
                align-items: center;
                justify-content: space-between;
            }}

            .footer-left {{
                color: #5f6c74;
                font-size: 12px;
            }}

            .footer-left i {{
                color: #00a884;
                margin-right: 5px;
            }}

            .footer-right {{
                color: #00a884;
                font-size: 13px;
                font-weight: 500;
            }}

            /* Status Badge */
            .status-badge {{
                background: #1a2a33;
                color: #00a884;
                padding: 4px 10px;
                border-radius: 20px;
                font-size: 11px;
                font-weight: 500;
                display: inline-flex;
                align-items: center;
                gap: 5px;
            }}

            .status-badge i {{
                font-size: 8px;
                color: #00a884;
            }}

            /* Success Message */
            .success-message {{
                background: #1a2a33;
                color: #00a884;
                padding: 12px 18px;
                border-radius: 8px;
                margin-bottom: 20px;
                font-size: 14px;
                display: flex;
                align-items: center;
                gap: 10px;
                border-left: 4px solid #00a884;
            }}

            .success-message i {{
                font-size: 18px;
            }}
        </style>
    </head>
    <body>
        <div class="whatsapp-container">
            <!-- WhatsApp Header -->
            <div class="whatsapp-header">
                <div class="whatsapp-logo">
                    <i class="fab fa-whatsapp"></i>
                </div>
                <div class="header-text">
                    <h1>WhatsApp Automation</h1>
                    <p><i class="fas fa-circle" style="font-size: 8px; color: #00a884; margin-right: 5px;"></i> Online • Schedule Messages</p>
                </div>
                <div class="creator-name">
                    <i class="fas fa-heart"></i> Sumit Haldar <i class="fas fa-code"></i>
                </div>
            </div>

            <!-- Main Content -->
            <div class="whatsapp-content">
                <!-- Status Update -->
                <div class="status-badge" style="margin-bottom: 15px;">
                    <i class="fas fa-lock"></i> End-to-end encrypted
                </div>

                <!-- Result Message -->
                {f'''
                <div class="success-message">
                    <i class="fas fa-check-circle"></i>
                    {result}
                </div>
                ''' if result else ''}

                <!-- Form -->
                <form method="POST">
                    <!-- Phone Number Input -->
                    <div class="input-group">
                        <label class="input-label">
                            <i class="fas fa-phone-alt"></i>
                            Phone Number
                        </label>
                        <input type="text" class="input-field" name="number" 
                               placeholder="+91 98765 43210" required>
                    </div>

                    <!-- Message Input -->
                    <div class="input-group">
                        <label class="input-label">
                            <i class="fas fa-comment"></i>
                            Message
                        </label>
                        <textarea class="input-field" name="message" 
                                  placeholder="Type a message..." required></textarea>
                    </div>

                    <!-- Time Inputs -->
                    <div class="time-row">
                        <div class="input-group">
                            <label class="input-label">
                                <i class="fas fa-clock"></i>
                                Hour
                            </label>
                            <input type="number" class="input-field" name="hour" 
                                   placeholder="0-23" min="0" max="23" required>
                        </div>
                        <div class="input-group">
                            <label class="input-label">
                                <i class="fas fa-clock"></i>
                                Minute
                            </label>
                            <input type="number" class="input-field" name="minute" 
                                   placeholder="0-59" min="0" max="59" required>
                        </div>
                    </div>

                    <!-- Send Button -->
                    <button type="submit" class="send-btn">
                        <i class="fab fa-whatsapp"></i>
                        Schedule Message
                        <i class="fas fa-arrow-right"></i>
                    </button>
                </form>

                <!-- Message Preview Section -->
                <div class="message-preview">
                    <div class="preview-title">
                        <i class="fas fa-eye"></i> Message Preview
                    </div>
                    <div class="preview-number">
                        <i class="fas fa-user"></i> Will be sent to: +91 **********
                    </div>
                    <div class="preview-message">
                        <i class="fas fa-comment-dots"></i> Your scheduled message will be delivered at the specified time
                    </div>
                </div>
            </div>

            <!-- Footer -->
            <div class="whatsapp-footer">
                <div class="footer-left">
                    <i class="fas fa-shield-alt"></i> WhatsApp Automation
                </div>
                <div class="footer-right">
                    <i class="fas fa-bolt"></i> by Sumit Haldar
                </div>
            </div>
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
    print("""
    ╔══════════════════════════════════╗
    ║  WhatsApp Automation System      ║
    ║  Created by: Sumit Haldar        ║
    ║  Running on: http://localhost:8000 ║
    ╚══════════════════════════════════╝
    """)
    execute_from_command_line([sys.argv[0], "runserver", "8000"])
