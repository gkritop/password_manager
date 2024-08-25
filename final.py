from cryptography.fernet import Fernet
import os
import json
import random
import string

class PasswordVault:
    def __init__(self, key_file='key.key', vault_file='vault.json'):
        self.key_file = key_file
        self.vault_file = vault_file
        self.key = self.load_key()
        self.cipher_suite = Fernet(self.key)

    def load_key(self):
        if not os.path.exists(self.key_file):
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as key_file:
                key_file.write(key)
            return key
        else:
            with open(self.key_file, 'rb') as key_file:
                return key_file.read()

    def encrypt_password(self, password):
        return self.cipher_suite.encrypt(password.encode()).decode()

    def decrypt_password(self, encrypted_password):
        return self.cipher_suite.decrypt(encrypted_password.encode()).decode()

    def add_password(self, service_name, password):
        encrypted_password = self.encrypt_password(password)
        vault_data = self.load_vault()
        vault_data[service_name] = encrypted_password
        self.save_vault(vault_data)

    def update_password(self, service_name, new_password):
        if self.get_password(service_name) is not None:
            self.add_password(service_name, new_password)
            print(f"Password for {service_name} updated.")
        else:
            print("Service not found. Password not updated.")

    def delete_password(self, service_name):
        vault_data = self.load_vault()
        if service_name in vault_data:
            del vault_data[service_name]
            self.save_vault(vault_data)
            print(f"Password for {service_name} deleted.")
        else:
            print("Service not found. Password not deleted.")

    def get_password(self, service_name):
        vault_data = self.load_vault()
        encrypted_password = vault_data.get(service_name)
        if encrypted_password:
            return self.decrypt_password(encrypted_password)
        else:
            return None

    def load_vault(self):
        if os.path.exists(self.vault_file):
            with open(self.vault_file, 'r') as vault_file:
                return json.load(vault_file)
        else:
            return {}

    def save_vault(self, vault_data):
        with open(self.vault_file, 'w') as vault_file:
            json.dump(vault_data, vault_file, indent=4)

def generate_password(length=12, include_special_chars=True):
    if length < 12:
        raise ValueError("Password length should be at least 12 characters.")
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    chars = lower + upper + digits
    if include_special_chars:
        chars += special
    
    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
    ]
    if include_special_chars:
        password_chars.append(random.choice(special))
    
    password_chars += [random.choice(chars) for _ in range(length - len(password_chars))]
    
    random.shuffle(password_chars)
    
    return ''.join(password_chars)

def main():
    vault = PasswordVault()

    while True:
        print("\nPassword Vault")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Generate and Add Password")
        print("4. Update Password")
        print("5. Delete Password")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            service_name = input("Enter service name: ")
            password = input("Enter password: ")
            vault.add_password(service_name, password)
            print("Password added.")

        elif choice == '2':
            service_name = input("Enter service name: ")
            password = vault.get_password(service_name)
            if password:
                print(f"Password for {service_name}: {password}")
            else:
                print("Service not found.")

        elif choice == '3':
            service_name = input("Enter service name: ")
            length = int(input("Enter password length (default 12): ") or 12)
            include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
            try:
                password = generate_password(length, include_special_chars)
                vault.add_password(service_name, password)
                print(f"Generated password for {service_name}: {password}")
            except ValueError as e:
                print(e)

        elif choice == '4':
            service_name = input("Enter service name: ")
            new_password = input("Enter new password: ")
            vault.update_password(service_name, new_password)

        elif choice == '5':
            service_name = input("Enter service name: ")
            vault.delete_password(service_name)

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
