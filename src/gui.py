import os
import hashlib
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Duplicate File Detector")
        self.root.geometry("800x400")

        # Directory path input frame
        self.path_frame = ttk.Frame(root)
        self.path_frame.pack(pady=10, fill=tk.X)

        self.path_label = ttk.Label(self.path_frame, text="Directory Path:")
        self.path_label.pack(side=tk.LEFT, padx=5)

        self.path_entry = ttk.Entry(self.path_frame, width=50)
        self.path_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        self.browse_button = ttk.Button(self.path_frame, text="Browse", command=self.browse_directory)
        self.browse_button.pack(side=tk.LEFT, padx=5)

        # Placeholder for duplicate files list with checkboxes
        self.duplicates_frame = ttk.Frame(root)
        self.duplicates_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        self.duplicates_list = []
        self.duplicates_vars = []

        # Buttons frame
        self.buttons_frame = ttk.Frame(root)
        self.buttons_frame.pack(pady=5, fill=tk.X)

        # Align buttons to the right
        self.buttons_inner_frame = ttk.Frame(self.buttons_frame)
        self.buttons_inner_frame.pack(side=tk.RIGHT)

        # Scan button
        self.scan_button = ttk.Button(self.buttons_inner_frame, text="Scan for Duplicates", command=self.scan_duplicates)
        self.scan_button.pack(side=tk.LEFT, padx=5)

        # Select All button
        self.select_all_button = ttk.Button(self.buttons_inner_frame, text="Select All", command=self.select_all)
        self.select_all_button.pack(side=tk.LEFT, padx=5)

        # Unselect All button
        self.unselect_all_button = ttk.Button(self.buttons_inner_frame, text="Unselect All", command=self.unselect_all)
        self.unselect_all_button.pack(side=tk.LEFT, padx=5)

        # Remove duplicates button
        self.remove_button = ttk.Button(self.buttons_inner_frame, text="Remove Selected Duplicates", command=self.remove_duplicates)
        self.remove_button.pack(side=tk.LEFT, padx=5)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, directory)

    def scan_duplicates(self):
        directory = self.path_entry.get()
        if not directory:
            messagebox.showerror("Error", "Please select a directory.")
            return

        duplicates = self.find_duplicates(directory)
        for widget in self.duplicates_frame.winfo_children():
            widget.destroy()
        self.duplicates_list.clear()
        self.duplicates_vars.clear()

        for dup in duplicates:
            var = tk.BooleanVar()
            frame = ttk.Frame(self.duplicates_frame)
            chk = ttk.Checkbutton(frame, text=f"{dup[0]} <-> {dup[1]}", variable=var)
            chk.pack(side=tk.LEFT, anchor='w', padx=5, pady=2)
            preview_button = ttk.Button(frame, text="Preview", command=lambda d=dup: self.preview_files(d))
            preview_button.pack(side=tk.RIGHT, padx=5)
            frame.pack(anchor='w', fill=tk.X, pady=2)
            self.duplicates_list.append(dup)
            self.duplicates_vars.append(var)

    def find_duplicates(self, directory):
        files_map = {}
        duplicates = []

        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_hash = self.hash_file(file_path)
                if file_hash in files_map:
                    duplicates.append((file_path, files_map[file_hash]))
                else:
                    files_map[file_hash] = file_path

        return duplicates

    def hash_file(self, file_path):
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()

    def remove_duplicates(self):
        for i, var in enumerate(self.duplicates_vars):
            if var.get():
                file_pair = self.duplicates_list[i]
                os.remove(file_pair[0])
        messagebox.showinfo("Info", "Selected duplicates removed.")
        self.scan_duplicates()

    def select_all(self):
        for var in self.duplicates_vars:
            var.set(True)

    def unselect_all(self):
        for var in self.duplicates_vars:
            var.set(False)

    def preview_files(self, file_pair):
        for file in file_pair:
            os.startfile(file)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()