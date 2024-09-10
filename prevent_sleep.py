import ctypes
import tkinter as tk
from tkinter import messagebox

# Constants for Windows sleep prevention
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

# Function to prevent sleep
def prevent_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED)
    messagebox.showinfo("Sleep Prevention", "Sleep prevention is ON.")
    on_button.config(state=tk.DISABLED)  # Disable the On button
    off_button.config(state=tk.NORMAL)   # Enable the Off button

# Function to allow sleep
def allow_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
    messagebox.showinfo("Sleep Prevention", "Sleep prevention is OFF.")
    on_button.config(state=tk.NORMAL)    # Enable the On button
    off_button.config(state=tk.DISABLED) # Disable the Off button

# Main application window
def create_app():
    global on_button, off_button  # Define these as global variables so they can be accessed in the functions

    window = tk.Tk()
    window.title("Sleep Prevention")

    label = tk.Label(window, text="Control sleep mode of your Windows machine")
    label.pack(pady=10)

    # On Button
    on_button = tk.Button(window, text="ON", width=15, command=prevent_sleep)
    on_button.pack(pady=5)

    # Off Button
    off_button = tk.Button(window, text="OFF", width=15, state=tk.DISABLED, command=allow_sleep)
    off_button.pack(pady=5)

    # Exit Button
    exit_button = tk.Button(window, text="Exit", width=15, command=window.quit)
    exit_button.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    create_app()
