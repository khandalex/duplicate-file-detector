# duplicate-file-detector

## ABSTRACT

The duplicate-file-detector project is designed to identify and manage duplicate files within a given directory. This project aims to optimize storage and improve data management by employing efficient hashing algorithms to detect duplicates and providing a user-friendly interface for managing them. The main contributions of this work include the implementation of a robust detection algorithm, the development of a graphical user interface (GUI), and the evaluation of the system's performance. The results demonstrate significant improvements in storage efficiency and data organization, making the project a valuable tool for both personal and professional use.

## 1.0 INTRODUCTION

### 1.1 Background

With the exponential increase in digital data, the creation of duplicate files has become a common issue, consuming valuable storage space and complicating data management. Manual detection and removal of these duplicates is a tedious and error-prone process. This project addresses this issue by automating the detection and management of duplicate files.

### 1.2 Objectives

The primary objective of this project is to develop an efficient and reliable system for detecting duplicate files. This includes the implementation of detection algorithms, the development of a user interface, and the evaluation of the system's performance in real-world scenarios. The project aims to provide a comprehensive solution for duplicate file management, enhancing storage efficiency and simplifying data organization.

## 2.0 LITERATURE SURVEY

### 2.1 Existing Tools and Methods

Several tools and methods exist for detecting duplicate files, each with its own strengths and weaknesses. Common techniques include file hashing, byte-by-byte comparison, and metadata analysis. File hashing, particularly using algorithms like MD5 or SHA-1, is widely used due to its efficiency in generating unique fingerprints for files. Byte-by-byte comparison is more precise but significantly slower, especially for large datasets. Metadata analysis, which compares file attributes like name, size, and creation date, is fast but less reliable.

### 2.2 Comparative Analysis

A comparative analysis of different approaches to duplicate file detection reveals trade-offs between accuracy, speed, and resource consumption. File hashing strikes a balance between speed and accuracy, making it a popular choice for many applications. Byte-by-byte comparison, while accurate, is impractical for large datasets due to its slow processing time. Metadata analysis is fast but prone to errors, as files with different content can share the same metadata.

## 3.0 SCOPE OF PROJECT

### 3.1 In-Scope Features

The project focuses on developing an application that uses the MD5 hashing algorithm to detect duplicates and provides a graphical user interface (GUI) for ease of use. The system supports directory scanning, duplicate file listing, and removal of selected duplicates. The project also includes a virtual environment for dependency management and a detailed guide on setting up and running the application.

### 3.2 Out-of-Scope Aspects

The project does not cover advanced data deduplication techniques used in enterprise storage solutions or cloud-based services. It also does not include network-based duplicate detection or integration with cloud storage services. The focus is on local file management to keep the scope manageable and the implementation straightforward.

## 4.0 METHODOLOGY

### 4.1 Algorithm and Technical Implementation

The project uses the MD5 hashing algorithm to generate unique fingerprints for each file. The algorithm processes files in chunks to handle large files efficiently. Duplicates are detected by comparing these fingerprints. The system architecture consists of three main components: the file scanner, the duplicate detector, and the user interface.

### 4.2 Tools and Technologies

The project is implemented in Python, utilizing libraries such as `os` for file handling, `hashlib` for hashing, and `tkinter` for GUI development. The development environment includes Visual Studio Code and a virtual environment for dependency management. The `requirements.txt` file lists all necessary dependencies, which can be installed using `pip`.

## 5.0 DETAILS OF DESIGNS, WORKING AND PROCESSES

### 5.1 System Architecture

The system architecture consists of three main components: the file scanner, the duplicate detector, and the user interface. The file scanner traverses directories, the duplicate detector hashes files and identifies duplicates, and the user interface allows users to interact with the system. The following diagram illustrates the system architecture:

```
+------------------+        +-----------------------+        +---------------------+
|   File Scanner   +------->+   Duplicate Detector  +------->+   User Interface    |
+------------------+        +-----------------------+        +---------------------+
```

### 5.2 Data Flow and Interaction

The data flow begins with the user selecting a directory. The file scanner reads files and sends them to the duplicate detector. Detected duplicates are displayed in the user interface, where users can choose to remove selected files. The following sequence diagram illustrates the interaction between components:

```
User -> GUI: Select Directory
GUI -> File Scanner: Scan Directory
File Scanner -> Duplicate Detector: Hash Files
Duplicate Detector -> GUI: Display Duplicates
User -> GUI: Select Duplicates to Remove
GUI -> Duplicate Detector: Remove Selected Duplicates
```

## 6.0 RESULTS AND APPLICATIONS

### 6.1 Evaluation and Performance Metrics

The system's performance is evaluated based on its accuracy in detecting duplicates, the speed of processing, and resource usage. Benchmarks are conducted using directories of varying sizes and file types. The results indicate that the system efficiently detects duplicates with minimal resource consumption. The MD5 hashing algorithm provides a good balance between speed and accuracy.

### 6.2 Real-World Applications

The application can be used in personal and professional settings to manage storage efficiently. Potential users include individuals looking to free up space on their devices and organizations managing large datasets. The application is particularly useful for photographers, video editors, and other professionals who deal with large volumes of files.

## 7.0 CONCLUSION AND FUTURE SCOPE

The duplicate-file-detector project successfully addresses the issue of duplicate files by providing an efficient detection and management solution. The system's performance demonstrates its effectiveness in optimizing storage and improving data management. Future work could explore more advanced algorithms, integration with cloud storage services, and enhancements to the user interface. Additionally, the project could be extended to support network-based duplicate detection and advanced data deduplication techniques.

## 8.0 APPENDIX

### A.1 How to Run

1. Install Python 3.9 and ensure the path is added to your system.
2. Open the DUPLICATE-FILE-DETECTOR folder in Visual Studio Code.
3. Open PowerShell as Administrator and run the following command to change the policy execution:

```
Set-ExecutionPolicy RemoteSigned
```

4. Create a virtual environment using the following command in the terminal:

```
python -m venv venv
```

5. Activate the virtual environment using the following command:

```
venv\Scripts\activate
```

6. Install all required libraries using the following command:

```
pip install -r requirements.txt
```

7. Run the project using the following command:

```
python src/main.py
```

### A.2 Code Snippets

```python name=src/detector.py
import os
import hashlib

class DuplicateFileDetector:
    def __init__(self, directory):
        self.directory = directory
        self.file_hashes = {}
        self.duplicates = []

    def find_duplicates(self):
        for dirpath, _, filenames in os.walk(self.directory):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                file_hash = self.hash_file(file_path)
                if file_hash in self.file_hashes:
                    self.duplicates.append((file_path, self.file_hashes[file_hash]))
                else:
                    self.file_hashes[file_hash] = file_path

    def hash_file(self, file_path):
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()

    def remove_duplicates(self, files_to_remove):
        for file_path in files_to_remove:
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Error removing file {file_path}: {e}")
```

```python name=src/gui.py
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
```

### A.3 Requirements

```pip requirements name=requirements.txt
certifi==2024.12.14
charset-normalizer==3.4.1
docutils==0.21.2
filetype==1.2.0
idna==3.10
Kivy==2.3.1
kivy-deps.angle==0.4.0
kivy-deps.glew==0.3.1
Kivy-Garden==0.1.5
kivy_deps.sdl2==0.8.0
pillow==11.0.0
Pygments==2.18.0
pypiwin32==223
PyQt5==5.15.11
PyQt5-Qt5==5.15.2
PyQt5_sip==12.16.1
pywin32==308
requests==2.32.3
urllib3==2.3.0
```

## 9.0 REFERENCES

1. Python Documentation: https://docs.python.org/3/
2. Tkinter Documentation: https://docs.python.org/3/library/tkinter.html
3. MD5 Hashing Algorithm: https://en.wikipedia.org/wiki/MD5
4. GitHub Repository: https://github.com/khandalex/duplicate-file-detector
