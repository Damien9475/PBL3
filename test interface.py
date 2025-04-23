import tkinter as tk
from tkinter import filedialog, messagebox

class SimpleTriathlonApp:
    def __init__(self, root):  # Correction ici
        self.root = root
        self.root.title("Simple Triathlon Performance Analyzer")

        # Weightings for different segments
        self.weights = {
            "Swimming": tk.DoubleVar(value=0.2),
            "Cycling": tk.DoubleVar(value=0.3),
            "Running": tk.DoubleVar(value=0.2),
            "Transition1": tk.DoubleVar(value=0.1),
            "Transition2": tk.DoubleVar(value=0.1)
        }

        self.file_path = tk.StringVar(value="No file selected")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Load CSV File:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.file_path, width=50, state='readonly').pack(pady=5)
        tk.Button(self.root, text="Browse", command=self.load_file).pack(pady=5)

        tk.Label(self.root, text="Weightings:").pack(pady=5)
        for segment, var in self.weights.items():
            tk.Label(self.root, text=segment).pack(anchor='w')
            tk.Entry(self.root, textvariable=var, width=10).pack(pady=2)

        tk.Button(self.root, text="Display Rankings", command=self.display_rankings).pack(pady=20)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.file_path.set(file_path)

    def display_rankings(self):
        messagebox.showinfo("Rankings", "Rankings will be displayed here based on the selected criteria.")

if __name__ == "__main__":  # Correction ici
    root = tk.Tk()
    app = SimpleTriathlonApp(root)
    root.mainloop()
