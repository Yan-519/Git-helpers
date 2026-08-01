from tkinter import Tk, Entry, Button, messagebox
import subprocess


def submit_text():
    text = entry.get().strip()

    if not text:
        messagebox.showwarning("Empty", "Commit message cannot be empty.")
        return

    if messagebox.askyesno("Commit", "Are you sure you want to save the update?"):
        try:
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", text], check=True)
            subprocess.run(["git", "push"], check=True)
            messagebox.showinfo("Success", "Changes pushed successfully.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Git Error", f"Git command failed:\n{e}")

    window.destroy()


window = Tk()
window.title("Commit")
##window.geometry("500x100")

window.columnconfigure(0, weight=1)

entry = Entry(window, width=75)
entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
entry.focus_set()

Button(window, text="Save", width=10, command=submit_text).grid(row=1, column=0, pady=5)

#print(window.winfo_height())
##window.geometry(f"500x{ window.winfo_height() }")

window.mainloop()


