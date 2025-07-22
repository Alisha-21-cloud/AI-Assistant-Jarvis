# AI Assistant Jarvis

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![OpenCV](https://img.shields.io/badge/opencv-4.x-red)](https://opencv.org)
[![Status](https://img.shields.io/badge/status-active-brightgreen)](https://github.com/Alisha-21-cloud/AI-Assistant-Jarvis)

> A sophisticated AI-powered personal assistant with voice recognition, face authentication, and comprehensive automation capabilities inspired by Tony Stark’s JARVIS.

---

## 🚀 Features
- **🎤 Voice Recognition** – Google Speech API integration
- **👤 Face Authentication** – OpenCV + Haar Cascades
- **🌐 Web Interface** – Eel-based responsive UI
- **🔊 Hotword Detection** – Always-listening wake words (“Jarvis”, “Alexa”)
- **📱 Application Control** – Launch/close apps & websites
- **🎵 Media Integration** – YouTube search & playback
- **💬 Communication Hub** – WhatsApp automation, SMS, voice calls
- **🤖 AI Chatbot** – HugChat conversational AI
- **📊 Contact Management** – SQLite database
- **🔄 Multiprocessing** – Parallel hotword + main assistant

---

## 🛠️ Technology Stack

| Category   | Technologies                                                        |
|------------|---------------------------------------------------------------------|
| Backend    | Python 3.6+, SQLite3, Multiprocessing                               |
| AI / ML    | OpenCV, HugChat, LBPH Face Recognition, Haar Cascade                |
| Speech     | pyttsx3, SpeechRecognition, PyAudio, PVPorcupine                    |
| GUI        | Eel, HTML5, CSS3, JavaScript                                        |
| Automation | PyAutoGUI, PyWhatKit, ADB Commands                                  |
| Audio      | playsound, other audio-processing libs                              |

---

## 📋 Prerequisites
• Python 3.6 or higher  
• Windows / macOS / Linux  
• Microphone (voice input)  
• Camera (face auth)  
• Internet connection (web features)

---

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/Alisha-21-cloud/AI-Assistant-Jarvis.git
cd AI-Assistant-Jarvis
```

2. **Create virtual environment** *(recommended)*
```bash
python -m venv venv
```

**Activate**  
**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

3. **Install dependencies**

**Core**
```bash
pip install eel pyttsx3 speechrecognition opencv-python
pip install pyaudio playsound pyautogui pywhatkit
pip install hugchat pvporcupine
```

**Platform-specific**  
**Windows**
```bash
pip install pypiwin32 pipwin
pipwin install pyaudio
```

**macOS**
```bash
pip install pyobjc>=9.0.1
```

**Linux**
```bash
sudo apt-get install espeak espeak-data portaudio19-dev python3-xlib
```

---

## 🚀 Usage

**Direct execution**
```bash
python main.py
```

**With hotword detection**
```bash
python run.py
```

**Windows batch**
```
device.bat
```

### Voice Command Examples
| Category            | Examples                                                   |
|---------------------|------------------------------------------------------------|
| Apps & Web          | “Open Chrome”, “Open youtube.com”                          |
| Media               | “Play *Imagine Dragons* on YouTube”                        |
| Messaging / Calls   | “Send message to Alice”, “Call Bob”                        |
| Information         | “What time is it?”, “Tell me about black holes”            |
| General Chat        | Conversational queries to Jarvis AI                        |

---

## 📁 Project Structure

```
AI-Assistant-Jarvis/
├── main.py
├── run.py
├── device.bat
├── engine/
│   ├── features.py
│   ├── command.py
│   ├── config.py
│   ├── db.py
│   ├── helper.py
│   └── auth/
│       ├── recoganize.py
│       ├── trainer.py
│       └── samples/
├── www/
│   ├── index.html
│   ├── style.css
│   ├── *.js
│   └── assets/
└── jarvis.db
```

---

## ⚙️ Configuration

### Voice Settings (`engine/command.py`)
```python
engine.setProperty('voice', voices.id) # 0 = male, 1 = female
engine.setProperty('rate', 174)
engine.setProperty('volume', 1.0)
```

### Database  
Add contacts in `engine/db.py`  
```python
cursor.execute("INSERT INTO contacts VALUES (?, ?)", ("Name", "Phone"))
```

### Face Authentication
```bash
cd engine/auth
python sample.py # Collect face samples
python trainer.py # Train model
```

---

## 🛡️ Security Highlights
• Local processing of face & voice data  
• Encrypted SQLite storage  
• Face verification before access  
• Configurable privacy flags

---

## 🐛 Troubleshooting

| Issue                     | Fix                                                                       |
|---------------------------|---------------------------------------------------------------------------|
| PyAudio install error     | Windows: `pipwin install pyaudio` • macOS: `brew install portaudio`       |
| Camera / mic not working  | Check OS privacy settings & device usage                                  |
| Web UI won’t load         | Ensure port 8000 free • Try `http://127.0.0.1:8000`                       |

---

## 🤝 Contributing

1. Fork → `git checkout -b feature/AmazingFeature`  
2. Commit → `git commit -m 'Add AmazingFeature'`  
3. Push → `git push origin feature/AmazingFeature`  
4. Open Pull Request

### Dev Setup
```bash
python -m venv dev_env
source dev_env/bin/activate # Windows: dev_env\Scripts\activate
pip install -r requirements.txt
```

---

## 📝 License
MIT – see [LICENSE](LICENSE)

---

## 🙏 Acknowledgments
OpenCV • Google Speech API • HuggingFace • Python community – and Tony Stark for the inspiration 😉

---

*"Sometimes you gotta run before you can walk." — Tony Stark*
