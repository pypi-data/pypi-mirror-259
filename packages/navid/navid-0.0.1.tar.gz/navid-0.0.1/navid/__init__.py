name = 'navid'
from pynput import keyboard
from tkinter import Tk
import win32api
from googletrans import Translator as GoogleTranslator
import pyautogui
import time

class Translator:
    def __init__(self, language='fa',title='مترجم'):
        self.language = language
        self.title = title
        g = GoogleTranslator()
        k = keyboard.Controller()
        def on_release(key):
            if key == keyboard.Key.alt_l or key == keyboard.Key.alt_r or key == keyboard.Key.alt_gr:
                k.press(keyboard.Key.ctrl)
                k.press('c')
                k.release(keyboard.Key.ctrl)
                k.release('c')
                pyautogui.hotkey('ctrl', 'c')
                time.sleep(0.05)
                text = Tk().clipboard_get()
                win32api.MessageBox(0,  g.translate(text, language).text, title)

        with keyboard.Listener(on_release=on_release) as listener:
            listener.join()