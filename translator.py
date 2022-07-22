from utils.utils import decrypt_text, encrypt_text, save_audio, save_to_file
from pydub import AudioSegment
import os

print("-" * 50)
print("Morse Code Translator")
print("Made by Jed")
print("-" * 50)


while True: 
    
    _type = input('[1] Encode Morse from Text\n[2] Decode Morse\n')

    if _type.lower() == "1":
       
        text = input("Input Text: ")

        encrypted = encrypt_text(text)

        print("-" * 50 + "\nTranslated text: " + encrypted + "\n"+ "-" * 50)
        save_to_file(encrypted)
        print("Saved into logs.txt")
        print("-" * 50)

        save = input("Do you want to save Audio file? [Y/N]: ").lower()
        print("-" * 50)
        if save == "y":
            dot = AudioSegment.from_wav("./utils/sounds/dot.wav")
            dash = AudioSegment.from_wav("./utils//sounds/dash.wav")
            silence = AudioSegment.from_wav("./utils/sounds/silent.wav")
            starting_audio = AudioSegment.from_wav("./utils/sounds/starting_audio.wav") 

            """Loop over the morse code and concatenate audios matching the elements of the morse code."""

            for i in encrypted:
                if i == ".":
                    starting_audio += dot
                elif i == "-":
                    starting_audio += dash
                elif i == " " or "/":
                    starting_audio += silence
            
            try:
                folder = "exported_sounds"
                audio = save_audio(folder, starting_audio)
                print(f"Audio file saved as: {audio.name[18:]}")
            except FileNotFoundError:
                os.mkdir("exported_sounds")
                folder = "exported_sounds"
                audio = save_audio(folder, starting_audio)
                print(f"Audio file saved as: {audio.name[18:]}")

        elif save == "n":
            pass

        else:
            print("Not a valid answer")

        choice = input("Translate another one? [Y/N]: \n" + "-" * 50 + "\n").lower()

        if choice == "y":
            pass
        else:
            print("Thank you for using my translator!")
            break

    elif _type.lower() == "2":
        
        text = input("Input Morse Code: ")

        decrypted = decrypt_text(text)

        print("-" * 50 + "\nDecoded Morse Code: " + decrypted + "\n" + "-" * 50)
        save_to_file(decrypted, morse=True)
        print("Saved into logs.txt")

        choice = input("Translate another one? [Y/N]\n" + "-" * 50 + "\n").lower()
        
        if choice == "y":
            pass
        else:
            print("Thank you for using my translator!")
            break

    else:
        print("Not a valid answer.")