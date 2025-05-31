import os
import shutil
from tkinter import messagebox, Tk

def simulate_encryption(target_dir):
    """Simulates file encryption by copying files with new extensions"""
    for root, _, files in os.walk(target_dir):
        for file in files:
            src_path = os.path.join(root, file)
            dest_path = src_path + ".simulated_encrypted"
            shutil.copy2(src_path, dest_path)
            os.remove(src_path)  # Simulates file deletion

def show_ransom_note():
    """Displays educational ransom note GUI"""
    root = Tk()
    root.withdraw()
    messagebox.showwarning(
        "SIMULATION: Ransomware Drill",
        "Educational Security Exercise:\n\n"
        "This simulated attack demonstrates how ransomware works.\n"
        "No files were actually encrypted.\n\n"
        "Report this incident to your security team."
    )
    root.destroy()

def create_test_environment():
    """Creates safe testing environment"""
    target_dir = os.path.join(os.getcwd(), "ransom_sim_test")
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        # Create sample files
        file_contents = [
            "This is a safe test document for security training.",
            "Sample data for ransomware simulation exercise.",
            "Educational file - no sensitive content."
        ]
        for i, content in enumerate(file_contents, 1):
            with open(os.path.join(target_dir, f"doc{i}.txt"), "w") as f:
                f.write(content)
    return target_dir

if __name__ == "__main__":
    test_dir = create_test_environment()
    simulate_encryption(test_dir)
    show_ransom_note()
    print(f"Simulation complete. Check {test_dir} for results.")
