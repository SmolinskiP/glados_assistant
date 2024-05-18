import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
import pyautogui
from time import sleep
import speech_recognition as sr

class ImageLabel(tk.Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
        try:
            self.delay = int(im.info['duration'])
        except:
            self.delay = 10
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
    def unload(self):
        self.config(image=None)
        self.frames = None
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
            
def position_window(width=256, height=256, xf = 0.5, yf = 0.83):
    global root
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width*xf) - (width/2)
    y = (screen_height*yf) - (height/2)

    if x > screen_width-width:
        x  = screen_width-width
    if x < width:
        x = 0.0
    if y > screen_height-height:
        y  = screen_height-height*1.25
    if y < 0:
        y = 0
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
def start_animation():
    global root
    root = tk.Tk()
    position_window()

    lbl = ImageLabel(root, bg='white')
    lbl.lift()
    lbl.pack()
    lbl.load('listening.gif')
    root.overrideredirect(True)
    root.lift()
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-disabled", True)
    root.wm_attributes("-transparentcolor", "white")
    root.mainloop()
    return root

def activation_actions_copilot():
    pyautogui.hotkey('win', 'c')
    sleep(1)
    mic_coordinates = pyautogui.locateCenterOnScreen("mic.png", confidence=0.9, grayscale=True)
    if mic_coordinates != None:
        root = animation_thread.start()
    else:
        print("MIC not found on screen")

    actual_mouse_position = pyautogui.position()
    pyautogui.click(mic_coordinates)
    pyautogui.moveTo(actual_mouse_position)
    sleep(5)
    terminate_thread(animation_thread)
    terminate_thread(copilot_thread)

animation_thread = Thread(target = start_animation)
copilot_thread = Thread(target = activation_actions_copilot)