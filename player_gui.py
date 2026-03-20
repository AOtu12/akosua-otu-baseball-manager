# player_gui.py
# ---------------------------------------------------------
# Section 4: GUI for Baseball Team Manager
# Step 1: Create empty window
# ---------------------------------------------------------

import tkinter as tk


def main():
    # Create main window
    root = tk.Tk()
    root.title("Player Maintenance")
    root.geometry("400x300")

    # Start GUI loop
    root.mainloop()


if __name__ == "__main__":
    main()