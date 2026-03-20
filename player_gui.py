# player_gui.py
# ---------------------------------------------------------
# Section 4: GUI for Baseball Team Manager
# Step 4: Connect Get Player and Save Changes buttons
# ---------------------------------------------------------

import tkinter as tk
from tkinter import messagebox
import db_sqlite


def main():
    # Create main window
    root = tk.Tk()
    root.title("Player Maintenance")
    root.geometry("420x300")

    def clear_fields():
        """Clear all entry fields except player ID."""
        entry_first.delete(0, tk.END)
        entry_last.delete(0, tk.END)
        entry_position.delete(0, tk.END)
        entry_at_bats.delete(0, tk.END)
        entry_hits.delete(0, tk.END)

    def get_player():
        """Fetch player by ID and display data in entry boxes."""
        player_id_text = entry_id.get().strip()

        if player_id_text == "":
            messagebox.showerror("Error", "Please enter a Player ID.")
            return

        try:
            player_id = int(player_id_text)
        except ValueError:
            messagebox.showerror("Error", "Player ID must be an integer.")
            return

        player = db_sqlite.get_player(player_id)

        if player is None:
            messagebox.showerror("Error", "Player not found.")
            clear_fields()
            return

        # player tuple:
        # (playerID, batOrder, firstName, lastName, position, atBats, hits)
        entry_first.delete(0, tk.END)
        entry_first.insert(0, player[2])

        entry_last.delete(0, tk.END)
        entry_last.insert(0, player[3])

        entry_position.delete(0, tk.END)
        entry_position.insert(0, player[4])

        entry_at_bats.delete(0, tk.END)
        entry_at_bats.insert(0, player[5])

        entry_hits.delete(0, tk.END)
        entry_hits.insert(0, player[6])

    def save_changes():
        """Save edited player data back to the database."""
        player_id_text = entry_id.get().strip()

        if player_id_text == "":
            messagebox.showerror("Error", "Please enter a Player ID first.")
            return

        try:
            player_id = int(player_id_text)
            at_bats = int(entry_at_bats.get().strip())
            hits = int(entry_hits.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Player ID, At Bats, and Hits must be integers.")
            return

        position = entry_position.get().strip()

        # Save only position, atBats, and hits
        db_sqlite.update_player(player_id, position, at_bats, hits)

        messagebox.showinfo("Success", "Player updated successfully.")
        clear_fields()
        entry_id.delete(0, tk.END)

    # Player ID
    tk.Label(root, text="Player ID:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    entry_id = tk.Entry(root)
    entry_id.grid(row=0, column=1, padx=10, pady=10)

    btn_get = tk.Button(root, text="Get Player", command=get_player)
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

    # Create a frame for buttons
    frame_buttons = tk.Frame(root)
    frame_buttons.grid(row=6, column=1, columnspan=1, pady=15)

    # Save button
    btn_save = tk.Button(frame_buttons, text="Save Changes", command=save_changes)
    btn_save.pack(side="left", padx=5)

    # Cancel button
    btn_cancel = tk.Button(frame_buttons, text="Cancel", command=clear_fields)
    btn_cancel.pack(side="left", padx=5)
    
    # Start GUI loop
    root.mainloop()


if __name__ == "__main__":
    main()