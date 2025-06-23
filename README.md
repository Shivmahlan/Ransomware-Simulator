# 🛡️ Ransomware Simulator

> ⚠️ **Disclaimer:** This project is intended for **educational and ethical cybersecurity purposes only**. Do **not** use this tool maliciously or on any system or data without explicit permission.

---

## 🔍 Overview

The **Ransomware Simulator** is a Python-based tool that mimics the core behavior of real ransomware in a controlled and non-destructive environment. It encrypts files in a target directory and generates a fake ransom note — helping learners understand how ransomware works.

This project is 100% safe for practice and cybersecurity awareness demonstrations.

---

## 🎯 Features

- 🔐 Simulated file encryption using AES or XOR
- 📝 Auto-generated ransom note
- 📁 Recursive directory encryption
- 🧪 Includes test files for safe simulation
- 🔓 Optional decryption script (if provided)
- 🧠 Educational and training focused

---

## 📁 Project Structure

Ransomware-Simulator/
├── main.py # Main script to launch the ransomware simulation
├── encryptor.py # Encryption logic (e.g., XOR, AES)
├── decryptor.py # Decryption logic to reverse encryption (optional)
├── ransom_note.txt # Template for ransom message
├── test_files/ # Directory with safe sample files
├── requirements.txt # Python package dependencies
└── README.md # Documentation 


---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/Shivmahlan/Ransomware-Simulator
cd Ransomware-Simulator
2. Install Dependencies
Make sure you have Python 3 installed. Then install required packages:

bash
Copy
Edit
pip install -r requirements.txt
3. Run the Simulator
bash
Copy
Edit
python main.py
The script will simulate ransomware behavior by encrypting files in the test_files/ directory and generating a ransom note.

🔓 Decryption (Optional)
If you have a decryptor.py script and access to the encryption key, run:

bash
Copy
Edit
python decryptor.py
Make sure the decryption key matches the one used during encryption.

⚙️ How It Works
The script scans the target folder (test_files/)

Each file is encrypted using a basic encryption method

A ransom_note.txt file is created in the folder

(Optional) A decryption tool can reverse the encryption

🧪 Safe Testing Guidelines
Only run this on non-essential test files

Do not use on real system or personal data

For added safety, use a virtual machine

🧠 Use Cases
Cybersecurity training labs

Ransomware attack demonstrations

Ethical hacking practice

Honeypot simulation environments

