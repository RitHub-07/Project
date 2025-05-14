import psycopg2
import tkinter as tk
from tkinter import messagebox
conn = psycopg2.connect(
  dbname="notes_db",
  user="postgres",
  password="root",
   
   host="localhost",
   port="5432"
)
cur = conn.cursor()

# --- GUI functions ---

def save_note():
    note = note_entry.get("1.0", tk.END).strip()
    if note:
        cur.execute("INSERT INTO notes (content) VALUES (%s)", (note,))
        conn.commit()
        note_entry.delete("1.0", tk.END)
        messagebox.showinfo("Success", "Note saved!")
    else:
        messagebox.showwarning("Empty", "Note cannot be empty!")

def view_notes():
    cur.execute("SELECT * FROM notes")
    notes = cur.fetchall()
    note_list.delete("1.0", tk.END)
    for note in notes:
        note_list.insert(tk.END, f"{note[0]}. {note[1]}\n\n")

# --- GUI setup ---

root = tk.Tk()
root.title("Notes App")
root.geometry("500x500")

# Write note area
tk.Label(root, text="Write your note:", font=('Arial', 12, 'bold')).pack(pady=5)
note_entry = tk.Text(root, height=5, width=60)
note_entry.pack(pady=5)

# Save button
save_btn = tk.Button(root, text="Save Note", command=save_note, bg="green", fg="white", width=20)
save_btn.pack(pady=5)

# View button
view_btn = tk.Button(root, text="View All Notes", command=view_notes, bg="blue", fg="white", width=20)
view_btn.pack(pady=5)

# Notes display area
tk.Label(root, text="Saved Notes:", font=('Arial', 12, 'bold')).pack(pady=5)
note_list = tk.Text(root, height=15, width=60)
note_list.pack(pady=5)

root.mainloop()