from cryptography.fernet import Fernet

def safe_gk():
    key = Fernet.generate_key()
    return key

def safe(message, key):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

def unsafe(encrypted_message, key):
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message.decode())
    return decrypted_message