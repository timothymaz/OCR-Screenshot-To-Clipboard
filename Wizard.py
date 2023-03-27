import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

class InstallWizard:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR Screenshot Tool Installer")

        # Create widgets for input fields
        self.install_dir_label = tk.Label(self.root, text="Installation Directory:")
        self.install_dir_entry = tk.Entry(self.root, width=50)
        self.install_dir_browse_button = tk.Button(self.root, text="Browse...", command=self.browse_install_dir)

        self.packages_label = tk.Label(self.root, text="Required Packages:")
        self.packages_entry = tk.Entry(self.root, width=50)

        # Create widget for installation button
        self.install_button = tk.Button(self.root, text="Install", command=self.install)

        # Place widgets in grid
        self.install_dir_label.grid(row=0, column=0, sticky=tk.W)
        self.install_dir_entry.grid(row=0, column=1)
        self.install_dir_browse_button.grid(row=0, column=2)

        self.packages_label.grid(row=1, column=0, sticky=tk.W)
        self.packages_entry.grid(row=1, column=1)

        self.install_button.grid(row=2, column=1)

    def browse_install_dir(self):
        # Open file dialog to select installation directory
        self.install_dir_entry.delete(0, tk.END)
        install_dir = filedialog.askdirectory()
        if install_dir:
            self.install_dir_entry.insert(0, install_dir)

    def install(self):
        # Get installation directory and required packages
        install_dir = self.install_dir_entry.get()
        packages = self.packages_entry.get()

        # Run necessary commands to install packages and move files
        try:
            subprocess.check_call(["pip", "install", packages])
            subprocess.check_call(["cp", "Main-OCR-Screenshot-To-Clipboard.py", install_dir])
            messagebox.showinfo("Installation Complete", "Installation complete!")
            self.root.destroy()
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Installation failed: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Create root window and wizard instance
root = tk.Tk()
install_wizard = InstallWizard(root)

# Run GUI main loop
root.mainloop()