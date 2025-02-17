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