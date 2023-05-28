import tkinter as tk
from PIL import ImageGrab
import os

root = tk.Tk()
root.title("LCARS")

def screenshot():
    # Get the size of the current window
    x1 = root.winfo_rootx()
    y1 = root.winfo_rooty()
    x2 = x1 + root.winfo_width()
    y2 = y1 + root.winfo_height()

    # Take a screenshot of the current window
    img = ImageGrab.grab((x1, y1, x2, y2))

    # Save the screenshot
    img.save("screenshot.png")

def disk_space():
    # Get the disk space usage
    disk_space = os.statvfs("/")
    free = disk_space.f_bavail * disk_space.f_frsize
    total = disk_space.f_blocks * disk_space.f_frsize
    used = (disk_space.f_blocks - disk_space.f_bfree) * disk_space.f_frsize
    usage = (used / total) * 100

    # Update the main section text
    main_section.config(text="Total: {} | Used: {} | Free: {} | Usage: {:.2f}%".format(total, used, free, usage))

# Create a frame for the button column
button_frame = tk.Frame(root, bg='black', width=200, height=600)
button_frame.pack(side='left', fill='y')

# Create the buttons
screenshot_button = tk.Button(button_frame, text="Screenshot", bg='red', command=screenshot)
screenshot_button.pack(fill='both')

disk_space_button = tk.Button(button_frame, text="Disk Space", bg='blue', command=disk_space)
disk_space_button.pack(fill='both')

black_button = tk.Button(button_frame, text="Black", bg='black', fg='white')
black_button.pack(fill='both')

# Create the main section
main_section = tk.Label(root, text="This is the main section", bg='white')
main_section.pack(side='right', fill='both', expand=True)

root.mainloop()

