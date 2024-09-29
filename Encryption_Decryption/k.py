import os
from cryptography.fernet import Fernet 

def generate_key():
    return Fernet.generate_key()

def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()

def read_encrypt_and_decrypt_files(directory_path=None, key=None):
    # Use the current working directory if no path is provided
    if directory_path is None:
        directory_path = os.getcwd()
    
    # Generate a new key if not provided
    if key is None:
        key = generate_key()
    
    files = os.listdir(directory_path)
    
    for file_name in files:
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
                encrypted_content = encrypt_message(content, key)
                
                # Store encrypted content
                encrypted_file_name = f"{file_name}.encrypted"
                with open(encrypted_file_name, 'wb') as encrypted_file:
                    encrypted_file.write(encrypted_content)
                
                # Store decrypted content
                decrypted_content = decrypt_message(encrypted_content, key)
                decrypted_file_name = f"{file_name}.decrypted"
                with open(decrypted_file_name, 'w') as decrypted_file:
                    decrypted_file.write(decrypted_content)
                
                print(f"Processed {file_name}:")
                print(f"  - Original content:")
                print(content)
                print(f"  - Encrypted content stored in: {encrypted_file_name}")
                print(f"  - Decrypted content stored in: {decrypted_file_name}")
                print()

    return key

# Call the function with the default (current working directory) path
encryption_key = read_encrypt_and_decrypt_files()
print(f"Encryption key: {encryption_key}")