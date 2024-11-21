import random
import string
def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    # Combine all characters
    all_characters = lowercase + uppercase + digits + special_characters
    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
def main():
    # User input for password length
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 8 characters): "))
            if length < 8:
                print("Password length should be at least 8 characters. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Generate and display the password
    generated_password = generate_password(length)
    print(f"Generated Password: {generated_password}")

if __name__ == "__main__":
    main()