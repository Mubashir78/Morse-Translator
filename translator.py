from utils.utils import decrypt_text, encrypt_text, save_to_file


print("-" * 50)
print("Morse Code Translator")
print("Made by Jed")
print("-" * 50)


while True: 
    
    _type = input('Type "E" if you want to encode Morse.\nType "D" if you want to decode.\n')

    if _type.lower() == "e":
       
        text = input("Input Text: ")

        encrypted = encrypt_text(text)

        print("-" * 50 + "\nTranslated text: " + encrypted + "\n"+ "-" * 50)
        save_to_file(encrypted)
        print("Saved into logs.txt")

        choice = input("Translate another one? [Y/N]\n" + "-" * 50 + "\n").lower()

        if choice == "y":
            pass
        else:
            break

    elif _type.lower() == "d":
        
        text = input("Input Morse Code: ")

        decrypted = decrypt_text(text)

        print("-" * 50 + "\nDecoded Morse Code: " + decrypted + "\n" + "-" * 50)
        save_to_file(decrypted)
        print("Saved into logs.txt")

        choice = input("Translate another one? [Y/N]\n" + "-" * 50 + "\n").lower()
        
        if choice == "y":
            pass
        else:
            break

    else:
        print("Not a valid answer.")