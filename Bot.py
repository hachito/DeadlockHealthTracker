import tkinter as tk
import winsound


class Visuals():
    warn_label = None
    def playwarning(self):
        root = tk.Tk()
        warn_label = tk.Label(root, text="GET HEALTH IDIOT", background="red", foreground="black",
                                font=("Impact", 100), width=1920, height=1080, title="GET HEALTH IDIOT")
        warn_label.pack()
        winsound.PlaySound('HELP.wav', winsound.SND_FILENAME)
        root.update()
    def removewarning(self, warn_label=None):
        root = tk.Tk()
        warn_label.destroy()
        root.update()
