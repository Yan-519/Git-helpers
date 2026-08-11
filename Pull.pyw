import subprocess
from tkinter import messagebox

if messagebox.askyesno("Update", "Are you shure you want to pull?"):
    try:
        subprocess.run(["git", "pull"], check=True)
        messagebox.showinfo("Success", "Pull succeeded.")
    except subprocess.CalledProcessError as e:
        if messagebox.askyesno("Git Error", f"Git command failed:\n{e}\nWould you like to force pull?"):
            try:
                subprocess.run(["git", "pull"], check=True)
                messagebox.showinfo("Success", "Pull succeeded.")
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Git Error", f"Git command failed:\n{e}")
