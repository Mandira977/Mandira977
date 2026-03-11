## Voice AI Assistant

This repository now includes two versions of a Voice AI Assistant:

1. **Web app** (`index.html`) using browser Web Speech APIs.
2. **Python app** (`voice_assistant.py`) using `SpeechRecognition` + `pyttsx3`.

### Run the web version
```bash
python3 -m http.server 8000
```
Open: `http://localhost:8000`

### Run the Python version
Install dependencies:
```bash
pip install SpeechRecognition pyttsx3 pyaudio
```

Then run:
```bash
python3 voice_assistant.py
```

Say commands like:
- "hello"
- "what time is it"
- "open youtube"
- "search for python projects"
- "exit"
