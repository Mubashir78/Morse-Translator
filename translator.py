from utils.utils import decrypt_text, encrypt_text


print("-" * 50)
print("Morse Code Translator")
print("Made by Jed")
print("-" * 50)


while True: 
    
    _type = input('Type "E" if you want to encode Morse.\nType "D" if you want to decode.\n')

    if _type.lower() == "e":
       
        text = input("Input Text: ")

        print("-" * 50 + "\nTranslated text: " + encrypt_text(text) + "\n"+ "-" * 50)

        choice = input("Translate another one? [Y/N]\n").lower()

        match choice:
            case "y" | "yes":
                pass
            case _:
                break

    elif _type.lower() == "d":
        
        text = input("Input Morse Code: ")

        print("-" * 50 + "\nDecoded Morse Code: " + decrypt_text(text) + "\n" + "-" * 50)

        choice = input("Translate another one? [Y/N]\n").lower()
        
        match choice:
            case "y":
                pass
            case "n":
                break

    else:
        print("Not a valid answer.")