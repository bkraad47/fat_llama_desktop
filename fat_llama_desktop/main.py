import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import logging
from fat_llama_desktop.feed import upscale

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FatLlamaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fat - llama")
        self.root.iconbitmap(os.path.join(os.path.dirname(__file__), 'assets', 'logo.ico'))
        self.files = []
        self.target_folder = ""
        
        # Setup UI
        self.setup_ui()
        
    def setup_ui(self):
        # Add Files Button
        self.add_files_button = tk.Button(self.root, text="Add Files", command=self.add_files, bg="lime")
        self.add_files_button.grid(row=0, column=0, padx=10, pady=10)
        
        # Target Folder Button
        self.target_folder_button = tk.Button(self.root, text="Target Folder", command=self.select_target_folder, bg="#ADD8E6")
        self.target_folder_button.grid(row=0, column=1, padx=10, pady=10)
        
        # Target Folder Label
        self.target_folder_label = tk.Label(self.root, text="Target Folder is not set")
        self.target_folder_label.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
        
        # Iterations
        tk.Label(self.root, text="Iterations").grid(row=1, column=0, padx=10, pady=5)
        self.iterations_entry = tk.Entry(self.root)
        self.iterations_entry.insert(0, "800")
        self.iterations_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Threshold
        tk.Label(self.root, text="Threshold").grid(row=1, column=2, padx=10, pady=5)
        self.threshold_entry = tk.Entry(self.root)
        self.threshold_entry.insert(0, "0.6")
        self.threshold_entry.grid(row=1, column=3, padx=10, pady=5)
        
        # Target Bit Rate
        tk.Label(self.root, text="Target Bit Rate").grid(row=1, column=4, padx=10, pady=5)
        self.bitrate_entry = tk.Entry(self.root)
        self.bitrate_entry.insert(0, "1411")
        self.bitrate_entry.grid(row=1, column=5, padx=10, pady=5)
        
        # Output Format Dropdown
        tk.Label(self.root, text="Output Format").grid(row=1, column=6, padx=10, pady=5)
        self.output_format = ttk.Combobox(self.root, values=["flac", "wav"])
        self.output_format.set("flac")
        self.output_format.grid(row=1, column=7, padx=10, pady=5)
        
        # Process Button
        self.process_button = tk.Button(self.root, text="PROCESSS!!!", command=self.process_files, bg="red", height=2, width=20)
        self.process_button.grid(row=3, column=0, columnspan=8, padx=10, pady=20)
        
        # Clear List Button
        self.clear_list_button = tk.Button(self.root, text="Clear List", command=self.clear_list, bg="orange")
        self.clear_list_button.grid(row=3, column=8, padx=10, pady=10)
        
        # File List with Scrollbar
        self.file_list = ttk.Treeview(self.root, columns=("Input File", "Status", "Output File"), show='headings')
        self.file_list.heading("Input File", text="Input File")
        self.file_list.heading("Status", text="Status")
        self.file_list.heading("Output File", text="Output File")
        
        self.file_list_scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.file_list.yview)
        self.file_list.configure(yscrollcommand=self.file_list_scrollbar.set)
        
        self.file_list.grid(row=2, column=0, columnspan=8, padx=10, pady=10, sticky="nsew")
        self.file_list_scrollbar.grid(row=2, column=8, sticky="ns")
        
    def add_files(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3;*.wav;*.ogg;*.flac")])
        for file_path in file_paths:
            self.files.append(file_path)
            self.file_list.insert('', 'end', values=(file_path, "Pending", ""))
        
    def select_target_folder(self):
        target_folder = filedialog.askdirectory()
        if target_folder:
            self.target_folder = target_folder
            self.target_folder_label.config(text=f"Target Folder Set to {self.target_folder}")
        
    def clear_list(self):
        self.files.clear()
        for item in self.file_list.get_children():
            self.file_list.delete(item)
        self.target_folder_label.config(text="Target Folder is not set")
        
    def process_files(self):
        if not self.files:
            messagebox.showerror("Error", "Please add files to process.")
            return

        if not self.target_folder:
            messagebox.showerror("Error", "Please select a target folder.")
            return
        
        try:
            iterations = int(self.iterations_entry.get())
            if not (10 <= iterations <= 1000):
                raise ValueError("Iterations must be between 10 and 1000.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        
        try:
            threshold = float(self.threshold_entry.get())
            if not (0.1 <= threshold <= 1):
                raise ValueError("Threshold must be between 0.1 and 1.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        
        try:
            bitrate = int(self.bitrate_entry.get())
            output_format = self.output_format.get()
            if output_format == "flac" and not (800 <= bitrate <= 1411):
                raise ValueError("For FLAC, bitrate must be between 800 and 1411 kbps.")
            elif output_format == "wav" and not (800 <= bitrate <= 6444):
                raise ValueError("For WAV, bitrate must be between 800 and 6444 kbps.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        
        for i, file_path in enumerate(self.files):
            output_file = os.path.join(self.target_folder, os.path.splitext(os.path.basename(file_path))[0] + f".{output_format}")
            output_file = os.path.normpath(output_file).replace('\\', '/')
            try:
                self.file_list.item(self.file_list.get_children()[i], values=(file_path, "Processing", output_file))
                self.file_list.update_idletasks()
                upscale(
                    input_file_path=file_path,
                    output_file_path=output_file,
                    source_format=file_path.split('.')[-1],
                    target_format=output_format,
                    max_iterations=iterations,
                    threshold_value=threshold,
                    target_bitrate_kbps=bitrate
                )
                self.file_list.item(self.file_list.get_children()[i], values=(file_path, "Processed", output_file))
            except Exception as e:
                self.file_list.item(self.file_list.get_children()[i], values=(file_path, "Failed", str(e)))
            finally:
                self.file_list.update_idletasks()

def main():
    root = tk.Tk()
    app = FatLlamaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
