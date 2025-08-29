# Auto Chat Responder with DeepSeek

This project automates reading and replying to chat messages on screen using **PyAutoGUI**, **Pyperclip**, and the **DeepSeek LLM** (via Ollama).  
It simulates mouse and keyboard actions to copy chat history, generate an AI-based reply, and send it automatically.

## 🚀 Features
- **Cursor Tracker**: `getCursor.py` helps find mouse coordinates for your system.
- **Auto Chat Bot**: `main.py`  
  - Captures chat text by simulating drag + copy  
  - Sends chat to **DeepSeek** (via Ollama CLI)  
  - Cleans the reply (removes thinking traces, tags, etc.)  
  - Pastes & sends the AI-generated response back automatically  

## 📦 Requirements
- Python 3.8+  
- [Ollama](https://ollama.ai/) installed with `deepseek-r1` model  
- Install Python packages:
  ```bash
  pip install pyautogui pyperclip
# ⚡ Usage

- Run getCursor.py to check and note your screen coordinates.

- Update those coordinates inside main.py as per your chat app window.

- Start the bot:

- python main.py

- Quickly switch to your chat window (script waits 2 seconds).

- The bot will now auto-monitor and reply as Anshul.

# 📝 Notes

- Works with any chat app that can be controlled via copy/paste and keyboard events.

- You can edit the query_deepseek() function in main.py to use other models or prompts.

- Useful for experimenting with automation + LLMs.
