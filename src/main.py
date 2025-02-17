import os
import hashlib
from gui import App
import tkinter as tk

def find_duplicates(directory):
    files_map = {}
    duplicates = []

    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_hash = hash_file(file_path)

            if file_hash in files_map:
                duplicates.append((file_path, files_map[file_hash]))
            else:
                files_map[file_hash] = file_path

    return duplicates

def hash_file(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()