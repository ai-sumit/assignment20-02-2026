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
            @keyframes gradientShift {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            
            @keyframes softFloat {
                0% { transform: translateY(0px); }
                50% { transform: translateY(-10px); }
                100% { transform: translateY(0px); }
            }
            
            @keyframes glowPulse {
                0% { opacity: 0.6; filter: blur(5px); }
                50% { opacity: 1; filter: blur(8px); }
                100% { opacity: 0.6; filter: blur(5px); }
            }
            
            @keyframes borderFlow {
                0% { border-color: #667eea; }
                25% { border-color: #764ba2; }
                50% { border-color: #6b8cff; }
                75% { border-color: #9f7aea; }
                100% { border-color: #667eea; }
            }
            
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                background: linear-gradient(135deg, #1a1a2e 0%, #16213e 25%, #1a1a2e 50%, #0f3460 75%, #1a1a2e 100%);
                background-size: 400% 400%;
                animation: gradientShift 15s ease infinite;
                color: #e0e0e0;
                text-align: center;
                padding: 40px 20px;
                margin: 0;
                min-height: 100vh;
                position: relative;
            }
            
            /* Soft glow orbs */
            .orb {
                position: fixed;
                width: 300px;
                height: 300px;
                border-radius: 50%;
                background: radial-gradient(circle at 30% 30%, rgba(102, 126, 234, 0.15), transparent 70%);
                pointer-events: none;
                z-index: 0;
            }
            
            .orb-1 {
                top: -100px;
                left: -100px;
                background: radial-gradient(circle at 30% 30%, rgba(118, 75, 162, 0.2), transparent 70%);
                animation: softFloat 8s ease-in-out infinite;
            }
            
            .orb-2 {
                bottom: -150px;
                right: -100px;
                width: 400px;
                height: 400px;
                background: radial-gradient(circle at 70% 70%, rgba(107, 140, 255, 0.15), transparent 70%);
                animation: softFloat 12s ease-in-out infinite reverse;
            }
            
            .container {
                max-width: 1000px;
                margin: 0 auto;
                position: relative;
                z-index: 1;
            }
            
            /* Header with gradient text */
            h1 {
                font-size: 3.5em;
                margin: 20px 0 10px;
                background: linear-gradient(135deg, #667eea, #764ba2, #6b8cff, #9f7aea);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-size: 300% 300%;
                animation: gradientShift 8s ease infinite;
                font-weight: 800;
                letter-spacing: 2px;
                text-transform: uppercase;
            }
            
            .guruji-title {
                font-size: 2.5em;
                margin: 10px 0;
                background: linear-gradient(135deg, #a8b8ff, #b794f4);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-weight: 600;
                letter-spacing: 4px;
                animation: softFloat 5s ease-in-out infinite;
            }
            
            /* Credit section with glass morphism */
            .credit-section {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 30px;
                margin: 30px 0;
                flex-wrap: wrap;
            }
            
            .glass-card {
                background: rgba(255, 255, 255, 0.05);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(102, 126, 234, 0.3);
                border-radius: 20px;
                padding: 20px 35px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
                transition: all 0.3s ease;
            }
            
            .glass-card:hover {
                border-color: #667eea;
                box-shadow: 0 8px 32px 0 rgba(102, 126, 234, 0.3);
                transform: translateY(-5px);
            }
            
            .badge-content {
                display: flex;
                align-items: center;
                gap: 15px;
            }
            
            .powered-by {
                background: linear-gradient(135deg, #a0b0ff, #c0a0ff);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-size: 1.2em;
                font-weight: 600;
            }
            
            .creator-name {
                background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fad0c4, #ff9a9e);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-size: 1.6em;
                font-weight: bold;
                background-size: 300% 300%;
                animation: gradientShift 6s ease infinite;
            }
            
            .wikipedia-icon, .cosmic-emoji {
                font-size: 2em;
                filter: drop-shadow(0 0 10px rgba(102, 126, 234, 0.5));
            }
            
            /* Search box with elegant design */
            .search-container {
                background: rgba(10, 20, 30, 0.6);
                backdrop-filter: blur(15px);
                border: 1px solid rgba(102, 126, 234, 0.3);
                border-radius: 50px;
                padding: 40px;
                margin: 40px 0;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
                position: relative;
                overflow: hidden;
            }
            
            .search-container::before {
                content: '';
                position: absolute;
                top: -2px;
                left: -2px;
                right: -2px;
                bottom: -2px;
                background: linear-gradient(135deg, #667eea, #764ba2, #6b8cff, #9f7aea);
                border-radius: 52px;
                opacity: 0.1;
                z-index: -1;
                animation: borderFlow 8s linear infinite;
            }
            
            .input-group {
                display: flex;
                justify-content: center;
                gap: 15px;
                flex-wrap: wrap;
            }
            
            input {
                flex: 1;
                min-width: 300px;
                padding: 18px 30px;
                border-radius: 40px;
                border: 2px solid rgba(102, 126, 234, 0.3);
                background: rgba(0, 0, 0, 0.3);
                color: #fff;
                font-size: 16px;
                transition: all 0.3s ease;
                box-shadow: 0 0 20px rgba(102, 126, 234, 0.1);
            }
            
            input:focus {
                outline: none;
                border-color: #667eea;
                box-shadow: 0 0 30px rgba(102, 126, 234, 0.3);
                background: rgba(0, 0, 0, 0.5);
            }
            
            input::placeholder {
                color: rgba(255, 255, 255, 0.5);
                font-style: italic;
            }
            
            button {
                padding: 18px 45px;
                border-radius: 40px;
                border: none;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                cursor: pointer;
                font-size: 18px;
                font-weight: 600;
                letter-spacing: 1px;
                transition: all 0.3s ease;
                box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
                position: relative;
                overflow: hidden;
            }
            
            button::before {
                content: '';
                position: absolute;
                top: 0;
                left: -100%;
                width: 100%;
                height: 100%;
                background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
                transition: left 0.7s ease;
            }
            
            button:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 30px rgba(102, 126, 234, 0.6);
            }
            
            button:hover::before {
                left: 100%;
            }
            
            /* Result card with elegant styling */
            .result-card {
                margin-top: 40px;
                background: rgba(10, 20, 30, 0.7);
                backdrop-filter: blur(15px);
                border: 1px solid rgba(102, 126, 234, 0.3);
                border-radius: 30px;
                padding: 40px;
                text-align: left;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
                animation: softFloat 0.6s ease-out;
                position: relative;
                overflow: hidden;
            }
            
            .result-card::after {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 3px;
                background: linear-gradient(90deg, #667eea, #764ba2, #6b8cff, #9f7aea);
                background-size: 300% 300%;
                animation: gradientShift 6s ease infinite;
            }
            
            .result-title {
                color: #fff;
                font-size: 2em;
                margin-bottom: 20px;
                padding-bottom: 15px;
                border-bottom: 1px solid rgba(102, 126, 234, 0.3);
                display: flex;
                align-items: center;
                gap: 15px;
                background: linear-gradient(135deg, #fff, #e0e0ff);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            
            .result-content {
                color: #d0d0ff;
                line-height: 1.8;
                font-size: 1.1em;
                text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
            }
            
            .result-content p {
                margin-bottom: 15px;
            }
            
            /* Loading animation */
            .loading {
                display: inline-block;
                width: 20px;
                height: 20px;
                border: 3px solid rgba(102, 126, 234, 0.3);
                border-radius: 50%;
                border-top-color: #667eea;
                animation: spin 1s ease-in-out infinite;
            }
            
            @keyframes spin {
                to { transform: rotate(360deg); }
            }
            
            /* Responsive design */
            @media (max-width: 768px) {
                h1 {
                    font-size: 2.5em;
                }
                
                .guruji-title {
                    font-size: 1.8em;
                }
                
                .glass-card {
                    padding: 15px 25px;
                }
                
                .creator-name {
                    font-size: 1.3em;
                }
                
                input {
                    min-width: 250px;
                }
                
                button {
                    padding: 18px 35px;
                }
                
                .search-container {
                    padding: 30px 20px;
                }
            }
            
            @media (max-width: 480px) {
                h1 {
                    font-size: 2em;
                }
                
                .guruji-title {
                    font-size: 1.5em;
                }
                
                .credit-section {
                    gap: 15px;
                }
                
                .glass-card {
                    width: 100%;
                }
                
                .badge-content {
                    justify-content: center;
                }
                
                input {
                    width: 100%;
                }
                
                button {
                    width: 100%;
                }
            }
            
            /* Smooth scrollbar */
            ::-webkit-scrollbar {
                width: 10px;
            }
            
            ::-webkit-scrollbar-track {
                background: #1a1a2e;
            }
            
            ::-webkit-scrollbar-thumb {
                background: linear-gradient(135deg, #667eea, #764ba2);
                border-radius: 5px;
            }
            
            ::-webkit-scrollbar-thumb:hover {
                background: linear-gradient(135deg, #764ba2, #667eea);
            }
            
            /* Text selection */
            ::selection {
                background: rgba(102, 126, 234, 0.3);
                color: #fff;
            }
        </style>
    </head>
    <body>
        <div class="orb orb-1"></div>
        <div class="orb orb-2"></div>
        
        <div class="container">
            <div class="guruji-title">✨ GURUJI ✨</div>
            <h1>⚡ Cosmic Wikipedia ⚡</h1>
            
            <div class="credit-section">
                <div class="glass-card">
                    <div class="badge-content">
                        <span class="powered-by">POWERED BY</span>
                        <span class="wikipedia-icon">📚</span>
                        <span style="color: #fff; font-weight: 500;">WIKIPEDIA</span>
                    </div>
                </div>
                
                <div class="glass-card">
                    <div class="badge-content">
                        <span class="cosmic-emoji">✨</span>
                        <span class="creator-name">SUMIT HALDAR</span>
                        <span class="cosmic-emoji">💫</span>
                    </div>
                </div>
            </div>
            
            <div class="search-container">
                <form method="GET" id="searchForm">
                    <div class="input-group">
                        <input type="text" name="query" placeholder="🔍 Search the cosmos for knowledge..." required id="searchInput">
                        <button type="submit">
                            <span>🚀</span> SEEK WISDOM
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
            <div class='result-card'>
                <h3 class='result-title'>
                    <span>📜</span> 
                    {query}
                </h3>
                <div class='result-content'>
                    <p>{result}</p>
                </div>
            </div>
            """
        except wikipedia.exceptions.DisambiguationError as e:
            options = ', '.join(e.options[:5])
            html += f"""
            <div class='result-card'>
                <h3 class='result-title'>
                    <span>🌌</span> 
                    Multiple Paths Found
                </h3>
                <div class='result-content'>
                    <p>The cosmos reveals multiple possibilities: {options}</p>
                </div>
            </div>
            """
        except wikipedia.exceptions.PageError:
            html += """
            <div class='result-card'>
                <h3 class='result-title'>
                    <span>🌑</span> 
                    Void Detected
                </h3>
                <div class='result-content'>
                    <p>This knowledge lies beyond our cosmic reach. Try another query.</p>
                </div>
            </div>
            """
        except Exception as e:
            html += f"""
            <div class='result-card'>
                <h3 class='result-title'>
                    <span>⚠️</span> 
                    Cosmic Disturbance
                </h3>
                <div class='result-content'>
                    <p>Error: {str(e)}</p>
                </div>
            </div>
            """

    html += """
        </div>
        
        <script>
            // Add smooth loading effect
            const searchForm = document.getElementById('searchForm');
            const searchInput = document.getElementById('searchInput');
            
            if (searchForm) {
                searchForm.addEventListener('submit', function(e) {
                    if (!searchInput.value.trim()) {
                        e.preventDefault();
                        searchInput.style.borderColor = '#ff6b6b';
                        setTimeout(() => {
                            searchInput.style.borderColor = 'rgba(102, 126, 234, 0.3)';
                        }, 1000);
                    } else {
                        const button = this.querySelector('button');
                        button.innerHTML = '<span class="loading"></span> SEEKING...';
                        button.disabled = true;
                    }
                });
            }
            
            // Add dynamic placeholder rotation
            const placeholders = [
                '🔍 Search the cosmos for knowledge...',
                '🌟 Ask about stars, planets, and galaxies...',
                '📚 Discover ancient wisdom...',
                '⚡ Explore scientific mysteries...',
                '🎭 Learn about great minds...'
            ];
            
            let index = 0;
            if (searchInput) {
                setInterval(() => {
                    index = (index + 1) % placeholders.length;
                    searchInput.placeholder = placeholders[index];
                }, 3000);
            }
        </script>
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
