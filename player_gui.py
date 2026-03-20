# player_gui.py
# ---------------------------------------------------------
# Section 4: GUI for Baseball Team Manager
# Step 2: Add labels, entry boxes, and buttons
# ---------------------------------------------------------

import tkinter as tk


def main():
    # Create main window
    root = tk.Tk()
    root.title("Player Maintenance")
    root.geometry("420x300")

    # Player ID
    tk.Label(root, text="Player ID:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entry_id = tk.Entry(root)
    entry_id.grid(row=0, column=1, padx=10, pady=10)

    btn_get = tk.Button(root, text="Get Player")
    btn_get.grid(row=0, column=2, padx=10, pady=10)

    # First Name
    tk.Label(root, text="First Name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_first = tk.Entry(root)
    entry_first.grid(row=1, column=1, padx=10, pady=5)

    # Last Name
    tk.Label(root, text="Last Name:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_last = tk.Entry(root)
    entry_last.grid(row=2, column=1, padx=10, pady=5)

    # Position
    tk.Label(root, text="Position:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entry_position = tk.Entry(root)
    entry_position.grid(row=3, column=1, padx=10, pady=5)

    # At Bats
    tk.Label(root, text="At Bats:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    entry_at_bats = tk.Entry(root)
    entry_at_bats.grid(row=4, column=1, padx=10, pady=5)

    # Hits
    tk.Label(root, text="Hits:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
    entry_hits = tk.Entry(root)
    entry_hits.grid(row=5, column=1, padx=10, pady=5)

    # Buttons
    btn_save = tk.Button(root, text="Save Changes")
    btn_save.grid(row=6, column=1, padx=10, pady=15, sticky="w")

    btn_cancel = tk.Button(root, text="Cancel")
    btn_cancel.grid(row=6, column=1, padx=10, pady=15, sticky="e")

    # Start GUI loop
    root.mainloop()


if __name__ == "__main__":
    main()