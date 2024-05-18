# Create a GUI-based file manager that allows users to browse directories, view files, and perform basic file operations like copy, move, and delete.

import os
import shutil
import tkinter as tk
from tkinter import filedialog

class FileManager:
    def __init__(self, master):
        self.master = master
        self.master.title("File Manager")

        self.directory_label = tk.Label(self.master, text="Directory:")
        self.directory_label.pack()

        self.directory_entry = tk.Entry(self.master, width=50)
        self.directory_entry.insert(0, os.getcwd())
        self.directory_entry.pack()

        self.browse_button = tk.Button(self.master, text="Browse", command=self.browse_directory)
        self.browse_button.pack()

        self.file_listbox = tk.Listbox(self.master, width=50, height=10)
        self.file_listbox.pack()

        self.refresh_button = tk.Button(self.master, text="Refresh", command=self.refresh_files)
        self.refresh_button.pack()

        self.copy_button = tk.Button(self.master, text="Copy", command=self.copy_file)
        self.copy_button.pack()

        self.move_button = tk.Button(self.master, text="Move", command=self.move_file)
        self.move_button.pack()

        self.delete_button = tk.Button(self.master, text="Delete", command=self.delete_file)
        self.delete_button.pack()

        self.refresh_files()

    def browse_directory(self):
        directory = filedialog.askdirectory()
        self.directory_entry.delete(0, tk.END)
        self.directory_entry.insert(0, directory)
        self.refresh_files()

    def refresh_files(self):
        directory = self.directory_entry.get()
        self.file_listbox.delete(0, tk.END)
        for file in os.listdir(directory):
            self.file_listbox.insert(tk.END, file)

    def copy_file(self):
        source_file = self.file_listbox.get(tk.ACTIVE)
        destination_directory = filedialog.askdirectory()
        shutil.copy2(source_file, destination_directory)

    def move_file(self):
        source_file = self.file_listbox.get(tk.ACTIVE)
        destination_directory = filedialog.askdirectory()
        shutil.move(source_file, destination_directory)

    def delete_file(self):
        file_to_delete = self.file_listbox.get(tk.ACTIVE)
        os.remove(file_to_delete)

root = tk.Tk()
file_manager = FileManager(root)
root.mainloop()