import tkinter as tk
from PIL import ImageGrab
from pyzbar.pyzbar import decode
import webbrowser
import keyboard

class DraggableRectangle:
    def __init__(self, canvas, color="white", width=2):
        self.canvas = canvas
        self.color = color
        self.width = width
        self.rect_id = None
        self.start_x = 0
        self.start_y = 0
        self.active = False

    def on_press(self, event):
        if not self.active:
            self.active = True
            self.start_x = self.canvas.canvasx(event.x)
            self.start_y = self.canvas.canvasy(event.y)

    def on_drag(self, event):
        if self.active:
            cur_x = self.canvas.canvasx(event.x)
            cur_y = self.canvas.canvasy(event.y)

            if self.rect_id:
                self.canvas.delete(self.rect_id)

            self.rect_id = self.canvas.create_rectangle(
                self.start_x,
                self.start_y,
                cur_x,
                cur_y,
                outline=self.color,
                width=self.width,
                stipple="gray50", 
            )

    def on_release(self, event):
        if self.active:
            self.active = False
            self.rect_id = None
            x = min(self.start_x, self.canvas.canvasx(event.x))
            y = min(self.start_y, self.canvas.canvasy(event.y))
            width = abs(self.start_x - self.canvas.canvasx(event.x))
            height = abs(self.start_y - self.canvas.canvasy(event.y))
            screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))

    
            decoded_objects = decode(screenshot)
            if decoded_objects:
                for obj in decoded_objects:
                    data = obj.data.decode('utf-8')
                    webbrowser.open(data)
            else:
                print("No QR code found in the screenshot.")

            root.after(1, root.destroy)

    def bind_events(self):
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

hotkey = 'ctrl+alt+q'

while True:
    keyboard.wait(hotkey)
    root = tk.Tk()
    root.title("Draggable Rectangle")
    root.attributes('-fullscreen', True)
    canvas = tk.Canvas(root, bg="black", width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack(fill=tk.BOTH, expand=True)
    root.attributes("-alpha", 0.5)
    draggable_rect = DraggableRectangle(canvas)
    draggable_rect.bind_events()

    root.mainloop()
