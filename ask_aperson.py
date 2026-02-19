import os
import sys
import wikipedia
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line

# -------------------- DJANGO SETTINGS --------------------

BASE_DIR = os.path.dirname(__file__)

settings.configure(
    DEBUG=True,
    SECRET_KEY='secret-key',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=[],
)

# -------------------- VIEW --------------------

def home(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Guruji - Wikipedia Cosmic Chat</title>
        <style>
            @keyframes cosmicSpin {
                0% { transform: rotate(0deg) scale(1); }
                50% { transform: rotate(180deg) scale(1.1); }
                100% { transform: rotate(360deg) scale(1); }
            }
            
            @keyframes starTwinkle {
                0% { opacity: 0.3; transform: scale(1); }
                50% { opacity: 1; transform: scale(1.2); }
                100% { opacity: 0.3; transform: scale(1); }
            }
            
            @keyframes floatGlow {
                0% { transform: translateY(0px); filter: drop-shadow(0 0 5px #00ffff); }
                50% { transform: translateY(-15px); filter: drop-shadow(0 0 20px #ff00ff); }
                100% { transform: translateY(0px); filter: drop-shadow(0 0 5px #00ffff); }
            }
            
            @keyframes pulseGlow {
                0% { box-shadow: 0 0 20px rgba(255, 215, 0, 0.3), 0 0 40px rgba(255, 215, 0, 0.2); }
                50% { box-shadow: 0 0 40px rgba(255, 215, 0, 0.6), 0 0 80px rgba(255, 215, 0, 0.4); }
                100% { box-shadow: 0 0 20px rgba(255, 215, 0, 0.3), 0 0 40px rgba(255, 215, 0, 0.2); }
            }
            
            @keyframes textGlow {
                0% { text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #00ffff, 0 0 40px #00ffff; }
                50% { text-shadow: 0 0 20px #fff, 0 0 30px #ff00ff, 0 0 40px #ff00ff, 0 0 50px #ff00ff; }
                100% { text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #00ffff, 0 0 40px #00ffff; }
            }
            
            @keyframes slideInFromGalaxy {
                0% { transform: translateY(100px) scale(0.5); opacity: 0; filter: blur(10px); }
                100% { transform: translateY(0) scale(1); opacity: 1; filter: blur(0); }
            }
            
            @keyframes galaxyRotate {
                from { transform: rotate(0deg); }
                to { transform: rotate(360deg); }
            }
            
            body {
                font-family: 'Segoe UI', 'Arial', sans-serif;
                background: radial-gradient(ellipse at top, #0a0e2a, #030514);
                color: #fff;
                text-align: center;
                padding: 50px 20px;
                margin: 0;
                min-height: 100vh;
                position: relative;
                overflow-x: hidden;
            }
            
            /* Cosmic Stars Background */
            body::before {
                content: '';
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-image: 
                    radial-gradient(2px 2px at 20px 30px, #fff, rgba(0,0,0,0)),
                    radial-gradient(2px 2px at 40px 70px, #ffd700, rgba(0,0,0,0)),
                    radial-gradient(3px 3px at 130px 40px, #00ffff, rgba(0,0,0,0)),
                    radial-gradient(2px 2px at 160px 120px, #ff69b4, rgba(0,0,0,0)),
                    radial-gradient(4px 4px at 240px 80px, #fff, rgba(0,0,0,0)),
                    radial-gradient(3px 3px at 310px 190px, #ffa500, rgba(0,0,0,0)),
                    radial-gradient(2px 2px at 380px 50px, #ff00ff, rgba(0,0,0,0)),
                    radial-gradient(3px 3px at 450px 220px, #00ff00, rgba(0,0,0,0)),
                    radial-gradient(4px 4px at 520px 140px, #fff, rgba(0,0,0,0)),
                    radial-gradient(2px 2px at 590px 80px, #ffd700, rgba(0,0,0,0)),
                    radial-gradient(3px 3px at 660px 200px, #00ffff, rgba(0,0,0,0)),
                    radial-gradient(4px 4px at 730px 120px, #ff69b4, rgba(0,0,0,0));
                background-repeat: repeat;
                background-size: 800px 400px;
                opacity: 0.8;
                animation: starTwinkle 4s ease-in-out infinite;
                pointer-events: none;
                z-index: 0;
            }
            
            /* Nebula Effect */
            body::after {
                content: '';
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: radial-gradient(circle at 30% 50%, rgba(255, 0, 255, 0.1) 0%, transparent 25%),
                            radial-gradient(circle at 70% 30%, rgba(0, 255, 255, 0.1) 0%, transparent 30%),
                            radial-gradient(circle at 80% 80%, rgba(255, 215, 0, 0.1) 0%, transparent 35%),
                            radial-gradient(circle at 20% 70%, rgba(255, 105, 180, 0.1) 0%, transparent 28%);
                pointer-events: none;
                z-index: 0;
            }
            
            .container {
                max-width: 900px;
                margin: 0 auto;
                position: relative;
                z-index: 1;
                animation: slideInFromGalaxy 1.5s ease-out;
            }
            
            /* Cosmic Portal Effect */
            .cosmic-portal {
                position: relative;
                margin-bottom: 30px;
                padding: 20px;
            }
            
            .portal-ring {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                width: 300px;
                height: 300px;
                border: 2px solid rgba(255, 215, 0, 0.3);
                border-radius: 50%;
                box-shadow: 0 0 50px rgba(255, 215, 0, 0.5);
                animation: cosmicSpin 20s linear infinite;
                pointer-events: none;
                z-index: -1;
            }
            
            .portal-ring-inner {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                width: 200px;
                height: 200px;
                border: 2px solid rgba(0, 255, 255, 0.3);
                border-radius: 50%;
                box-shadow: 0 0 80px rgba(0, 255, 255, 0.5);
                animation: cosmicSpin 15s linear reverse infinite;
            }
            
            h1 {
                font-size: 4.5em;
                margin: 20px 0 10px;
                background: linear-gradient(135deg, #ffd700, #ff8c00, #ff69b4, #00ffff);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                animation: textGlow 3s ease-in-out infinite;
                position: relative;
                letter-spacing: 4px;
                font-weight: 800;
            }
            
            .guruji-title {
                font-size: 3em;
                color: #ffd700;
                text-transform: uppercase;
                letter-spacing: 8px;
                margin: 10px 0;
                animation: floatGlow 4s ease-in-out infinite;
            }
            
            .credit-line {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 20px;
                margin: 20px 0;
                flex-wrap: wrap;
            }
            
            .cosmic-badge {
                background: rgba(10, 20, 40, 0.7);
                backdrop-filter: blur(10px);
                padding: 15px 30px;
                border-radius: 50px;
                border: 2px solid rgba(255, 215, 0, 0.5);
                box-shadow: 0 0 30px rgba(255, 215, 0, 0.3);
                animation: pulseGlow 3s ease-in-out infinite;
            }
            
            .badge-content {
                display: flex;
                align-items: center;
                gap: 15px;
            }
            
            .powered-by {
                color: #00ffff;
                font-size: 1.2em;
                text-shadow: 0 0 15px #00ffff;
            }
            
            .wikipedia-icon {
                font-size: 2em;
                animation: starTwinkle 2s ease-in-out infinite;
            }
            
            .creator-name {
                background: linear-gradient(135deg, #ff69b4, #ffd700);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-size: 1.8em;
                font-weight: bold;
                text-shadow: 0 0 20px rgba(255, 105, 180, 0.5);
            }
            
            .search-box {
                background: rgba(10, 20, 40, 0.6);
                backdrop-filter: blur(20px);
                padding: 50px;
                border-radius: 30px;
                margin: 40px 0;
                border: 2px solid rgba(255, 215, 0, 0.3);
                box-shadow: 0 0 100px rgba(0, 255, 255, 0.2);
                position: relative;
                overflow: hidden;
            }
            
            .search-box::before {
                content: '';
                position: absolute;
                top: -50%;
                left: -50%;
                width: 200%;
                height: 200%;
                background: conic-gradient(from 0deg, transparent, rgba(255, 215, 0, 0.2), transparent, rgba(0, 255, 255, 0.2), transparent);
                animation: galaxyRotate 10s linear infinite;
                z-index: -1;
            }
            
            .input-group {
                display: flex;
                justify-content: center;
                gap: 15px;
                flex-wrap: wrap;
            }
            
            input {
                width: 350px;
                padding: 18px 25px;
                border-radius: 50px;
                border: 2px solid rgba(255, 215, 0, 0.5);
                background: rgba(255, 255, 255, 0.1);
                color: #fff;
                font-size: 16px;
                transition: all 0.4s ease;
                box-shadow: 0 0 30px rgba(0, 255, 255, 0.2);
            }
            
            input:focus {
                outline: none;
                border-color: #00ffff;
                box-shadow: 0 0 40px #00ffff, 0 0 80px #00ffff;
                transform: scale(1.02);
                background: rgba(0, 0, 0, 0.3);
            }
            
            input::placeholder {
                color: rgba(255, 255, 255, 0.6);
                text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
            }
            
            button {
                padding: 18px 40px;
                border-radius: 50px;
                border: none;
                background: linear-gradient(135deg, #ffd700, #ff8c00, #ff69b4);
                color: #0a0e2a;
                cursor: pointer;
                font-size: 18px;
                font-weight: bold;
                letter-spacing: 2px;
                transition: all 0.4s ease;
                box-shadow: 0 0 30px #ffd700, 0 0 60px #ff69b4;
                border: 2px solid rgba(255, 255, 255, 0.5);
                position: relative;
                overflow: hidden;
            }
            
            button::before {
                content: '';
                position: absolute;
                top: -50%;
                left: -50%;
                width: 200%;
                height: 200%;
                background: conic-gradient(from 0deg, transparent, rgba(255, 255, 255, 0.3), transparent);
                animation: galaxyRotate 4s linear infinite;
            }
            
            button:hover {
                transform: scale(1.1);
                box-shadow: 0 0 50px #ffd700, 0 0 100px #ff69b4, 0 0 150px #00ffff;
            }
            
            .result {
                margin-top: 40px;
                background: rgba(10, 20, 40, 0.8);
                backdrop-filter: blur(20px);
                padding: 40px;
                border-radius: 30px;
                box-shadow: 0 0 100px rgba(255, 215, 0, 0.3);
                border: 2px solid rgba(255, 215, 0, 0.5);
                animation: slideInFromGalaxy 0.8s ease-out;
                text-align: left;
                position: relative;
                overflow: hidden;
            }
            
            .result::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: radial-gradient(circle at 20% 30%, rgba(255, 215, 0, 0.1), transparent 50%),
                            radial-gradient(circle at 80% 70%, rgba(0, 255, 255, 0.1), transparent 50%);
                pointer-events: none;
            }
            
            .result h3 {
                color: #ffd700;
                margin-top: 0;
                font-size: 2em;
                border-bottom: 2px solid rgba(255, 215, 0, 0.3);
                padding-bottom: 15px;
                text-shadow: 0 0 20px #ffd700;
                display: flex;
                align-items: center;
                gap: 15px;
            }
            
            .result p {
                line-height: 1.8;
                font-size: 1.2em;
                margin-bottom: 0;
                color: rgba(255, 255, 255, 0.9);
                text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
            }
            
            .cosmic-emoji {
                font-size: 2.5em;
                filter: drop-shadow(0 0 20px currentColor);
                animation: starTwinkle 2s ease-in-out infinite;
            }
            
            .shooting-star {
                position: fixed;
                top: 20%;
                right: 10%;
                width: 150px;
                height: 2px;
                background: linear-gradient(90deg, transparent, #fff, #ffd700, #ff69b4, transparent);
                transform: rotate(45deg);
                animation: floatGlow 8s ease-in-out infinite;
                opacity: 0.5;
            }
            
            .shooting-star2 {
                top: 70%;
                left: 15%;
                width: 200px;
                transform: rotate(-30deg);
                animation-delay: 3s;
            }
            
            @media (max-width: 600px) {
                h1 {
                    font-size: 2.5em;
                }
                
                .guruji-title {
                    font-size: 2em;
                }
                
                input {
                    width: 100%;
                }
                
                .search-box {
                    padding: 30px 20px;
                }
                
                .cosmic-badge {
                    padding: 10px 20px;
                }
                
                .creator-name {
                    font-size: 1.4em;
                }
            }
        </style>
    </head>
    <body>
        <div class="shooting-star"></div>
        <div class="shooting-star shooting-star2"></div>
        
        <div class="cosmic-portal">
            <div class="portal-ring"></div>
            <div class="portal-ring-inner"></div>
        </div>
        
        <div class="container">
            <div class="guruji-title">🌟 GURUJI 🌟</div>
            <h1>⚡ COSMIC WIKIPEDIA ⚡</h1>
            
            <div class="credit-line">
                <div class="cosmic-badge">
                    <div class="badge-content">
                        <span class="powered-by">POWERED BY</span>
                        <span class="wikipedia-icon">📚</span>
                        <span style="color: #fff; font-weight: bold; text-shadow: 0 0 15px #fff;">WIKIPEDIA</span>
                    </div>
                </div>
                
                <div class="cosmic-badge">
                    <div class="badge-content">
                        <span class="cosmic-emoji">👨‍🚀</span>
                        <span class="creator-name">SUMIT HALDAR</span>
                        <span class="cosmic-emoji">✨</span>
                    </div>
                </div>
            </div>
            
            <div class="search-box">
                <form method="GET">
                    <div class="input-group">
                        <input type="text" name="query" placeholder="🔮 Ask the cosmos about someone or something..." required>
                        <button type="submit">
                            <span style="margin-right: 10px;">🌠</span> SEEK KNOWLEDGE
                        </button>
                    </div>
                </form>
            </div>
    """

    query = request.GET.get("query")

    if query:
        try:
            wikipedia.set_lang("en")
            result = wikipedia.summary(query, sentences=5)


            html += f"""
            <div class='result'>
                <h3>
                    <span class="cosmic-emoji">📜</span> 
                    COSMIC REVELATION: {query}
                </h3>
                <p>{result}</p>
            </div>
            """
        except wikipedia.exceptions.DisambiguationError as e:
            options = ', '.join(e.options[:5])
            html += f"""
            <div class='result'>
                <h3>
                    <span class="cosmic-emoji">🌌</span> 
                    MULTIPLE PATHS IN THE COSMOS
                </h3>
                <p>The universe shows multiple paths: {options}</p>
            </div>
            """
        except wikipedia.exceptions.PageError:
            html += """
            <div class='result'>
                <h3>
                    <span class="cosmic-emoji">🌑</span> 
                    VOID DETECTED
                </h3>
                <p>This knowledge exists beyond our cosmic reach. Try another query.</p>
            </div>
            """
        except Exception as e:
            html += f"""
            <div class='result'>
                <h3>
                    <span class="cosmic-emoji">⚠️</span> 
                    COSMIC DISTURBANCE
                </h3>
                <p>Error: {str(e)}</p>
            </div>
            """

    html += """
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

# -------------------- URLS --------------------

urlpatterns = [
    path('', home),
]

# -------------------- RUN SERVER --------------------

if __name__ == "__main__":
    execute_from_command_line([sys.argv[0], "runserver", "8000"])