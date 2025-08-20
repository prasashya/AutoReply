import pyautogui
import pyperclip
import time
import subprocess
import sys
import io
import re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def query_deepseek(c):
    
        result = subprocess.run(
            ["ollama", "run", "deepseek-r1"],
            input=f"You are Anshul and reply like a normal human being which can speak english and hindi. you will analyze the chat history and reply as anshul.. chat:{c}",
            text=True,
            capture_output=True,
            encoding="utf-8"
        )
        return result.stdout.strip()



def clean_reply(text):
    # If DeepSeek outputs "...done thinking." keep only what comes after
    if "...done thinking." in text:
        text = text.split("...done thinking.", 1)[1]
    # Remove <think>...</think> blocks if present
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    # Remove any [thinking...] or (thinking...) parts
    text = re.sub(r"\[thinking.*?\]", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\(thinking.*?\)", "", text, flags=re.IGNORECASE)
    return text.strip()

def last_message_not_from_anshul(chat: str) -> bool:
    lines = [line.strip() for line in chat.splitlines() if line.strip()]
    if not lines:
        return True
    last_line = lines[-1]
    return not ("] Anshul Prasashya:" in last_line)


time.sleep(2)  # Time to switch to the target window

pyautogui.click(1214, 1061)
while True:

  pyautogui.moveTo(747, 260)
  pyautogui.mouseDown()

  
  pyautogui.moveTo(1750, 922, duration=1)
  pyautogui.mouseUp()

  
  pyautogui.hotkey("ctrl", "c")
  pyautogui.click(919,616)
  time.sleep(0.5)

  
  chat = pyperclip.paste()
  print(chat)

  if last_message_not_from_anshul(chat):
  

    time.sleep(1)
    reply=query_deepseek(chat)
    reply=clean_reply(reply)

    
    pyautogui.click(895, 976)
    time.sleep(0.3)

    
    pyperclip.copy(reply)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.2)

   
    pyautogui.press("enter")

  


