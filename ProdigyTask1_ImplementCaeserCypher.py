def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
   while True:
       choice = input("Enter 'e' for encrypt or 'd' for decrypt: ")
       if choice.lower() == 'e':
          message = input("Enter the message to encrypt: ")
          shift = int(input("Enter the shift value: "))
          encrypt_message = encrypt(message, shift)
          print("Encrypt message:", encrypt_message)
       elif choice.lower() == 'd':
          message = input("Enter the message to decrypt: ")
          shift = int(input("Enter the shift value: "))
          decrypt_message = decrypt(message, shift)
          print("Decrypt message:", decrypt_message)
       else:
          print("Invalid choice!")

       exit_choice = input("Do you want to exit? (yes/no): ")
       if exit_choice == 'yes':
          break

if __name__ == "__main__":
    main()
