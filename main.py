import tkinter as tk
import sys
import webbrowser
import keyboard
import os

# Window dimensions
WINDOW_GEOMETRY = {
    "width": 300,
    "height": 175,
}

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class App:
    def __init__(self):
        # Initialize the main window
        self.root = tk.Tk()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(
            f"{WINDOW_GEOMETRY['width']}x{WINDOW_GEOMETRY['height']}+{screen_width-(2*WINDOW_GEOMETRY['width'])}+{screen_height-(2*WINDOW_GEOMETRY['height'])}"
        )
        self.root.resizable(False, False)
        self.root.title("Arrow Swap")

        media_folder = os.path.join(BASE_DIR, "media")
        image_path = os.path.join(media_folder, "ArrowSwapLogo.ico")
        self.root.wm_iconbitmap(image_path)

        # Set up keyboard interception
        keyboard.on_press(self.intercept_key, suppress=True)

        # Initial swap status
        self.swapStatus = False

        # Initialize the UI
        self.init_screen()

    def init_screen(self):
        # Title label
        title = tk.Label(
            self.root,
            text="Arrow Swap",
            font=("Bahnschrift", 20, "bold"),
        )
        title.pack()

        # Explanation label
        explanation = tk.Label(
            self.root,
            text="Arrows are currently:",
            font=("Bahnschrift", 12, "normal"),
        )
        explanation.pack()

        # Status label
        self.status = tk.Label(
            self.root,
            text=("SWAPPED" if self.swapStatus else "NOT SWAPPED"),
            font=("Bahnschrift", 15, "bold"),
            fg="green",
        )
        self.status.pack()

        # Toggle button
        toggle = tk.Button(
            self.root,
            text="Toggle",
            font=("Bahnschrift", 15, "normal"),
            bg="#3d6b4b",
            fg="white",
            command=self.toggle_swap_status,
        )
        toggle.pack()

        # Link label
        link = tk.Label(
            self.root,
            text="Made By Vihaan Chhabria",
            font=("Bahnschrift", 10, "normal"),
            cursor="hand2",
            pady=15,
        )
        link.pack()
        link.bind(
            "<Button-1>",
            lambda e: webbrowser.open("https://github.com/VihaanChhabria/ArrowSwap"),
        )

    def toggle_swap_status(self):
        # Toggle the swap status and update the status label
        self.swapStatus = not self.swapStatus
        self.status.config(
            text=("SWAPPED" if self.swapStatus else "NOT SWAPPED"),
            fg=("red" if self.swapStatus else "green"),
        )

    def intercept_key(self, event):
        # Intercept arrow key presses and swap them if swapStatus is True
        if self.swapStatus:
            match (event.name):
                case "up":
                    print("here")
                    keyboard.press("down")
                    return False
                case "down":
                    keyboard.press("up")
                    return False
                case "left":
                    keyboard.press("right")
                    return False
                case "right":
                    keyboard.press("left")
                    return False
        return True

    def run(self):
        # Run the main loop of the Tkinter application
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            sys.exit()


if __name__ == "__main__":
    # Create and run the application
    app = App()
    app.run()
