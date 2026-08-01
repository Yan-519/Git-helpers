import subprocess
from tkinter import messagebox

if messagebox.askyesno("Update", "Are you shure you want to pull?"):
    system("git pull")
    try:
        subprocess.run(["git", "pull"], check=True)
    except subprocess.CalledProcessError as e:
            messagebox.showerror("Git Error", f"Git command failed:\n{e}")
