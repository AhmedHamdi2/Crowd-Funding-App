import hashlib
import json
from utilities import validate_email, validate_phone

data_file = "users.json"

def register():
    print("\n--- Register ---")
    try:
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        if not validate_email(email):
            print("Invalid email format.")
            return

        password = input("Password: ")
        confirm_password = input("Confirm Password: ")
        if password != confirm_password:
            print("Passwords do not match.")
            return

        phone = input("Mobile Phone: ")
        if not validate_phone(phone):
            print("Invalid phone number format.")
            return

        users = load_users()
        if any(user["email"] == email for user in users):
            print("Email already registered.")
            return

        user = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": hash_password(password),
            "phone": phone
        }
        users.append(user)
        save_users(users)

        print("Registration successful.")
    except Exception as e:
        print(f"An error occurred during registration: {e}")

def login():
    print("\n--- Login ---")
    try:
        email = input("Email: ")
        password = input("Password: ")

        users = load_users()
        for user in users:
            if user["email"] == email and user["password"] == hash_password(password):
                print(f"Welcome back, {user['first_name']} {user['last_name']}!")
                return user

        print("Invalid email or password.")
        return None
    except Exception as e:
        print(f"An error occurred during login: {e}")


def load_users():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading users: {e}")
        return []

def save_users(users):
    try:
        with open(data_file, "w") as file:
            json.dump(users, file, indent=4)
    except Exception as e:
        print(f"Error saving users: {e}")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


