# Password Manager

Password Manager is a command-line application for securely managing your passwords. It utilizes symmetric encryption to keep your password data safe and accessible only to you. 
This tool allows you to store, retrieve, update, and delete passwords, making it a convenient solution for managing your credentials securely.

Features:

    Add Password: Store a new password for a specific service.
    Retrieve Password: Access the password for a given service.
    Generate and Add Password: Automatically generate a strong password and store it.
    Update Password: Modify an existing password.
    Delete Password: Remove a stored password from the vault.

How It Works:

    Encryption: Passwords are encrypted using the cryptography library's Fernet module to ensure security.
    Storage: Encrypted passwords are saved in a JSON file for easy access and management.
    Password Generation: Strong passwords are generated with a mix of lowercase, uppercase letters, digits, and optionally special characters.

Installation:

Ensure you have Python 3.6 or later installed. Install the required dependencies using pip:

    pip install cryptography

Usage:

Clone the repository and navigate to the project directory. Run the script:

    python final.py

Follow the prompts to add, retrieve, update, or delete passwords.

Requirements:

    Python 3.6+
    cryptography library
