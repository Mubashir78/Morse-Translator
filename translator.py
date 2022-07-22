from utils.utils import decrypt_text, encrypt_text, save_to_file
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

            for i in encrypted:
                if i == ".":
                    starting_audio += dot
                elif i == "-":
                    starting_audio += dash
                elif i == " " or "/":
                    starting_audio += silence
            
            folder = os.listdir("exported_sounds")
            if folder == []:
                file = folder
            else:
                file = int(folder[-1][13])

            if folder == []:
                starting_audio.export(f"exported_sounds/exportedsound0.wav", format="wav")
            else:
                starting_audio.export(f"exported_sounds/exportedsound{file + 1}.wav", format="wav")
            

        else:
            pass

        choice = input("Translate another one? [Y/N]: \n" + "-" * 50 + "\n").lower()

        if choice == "y":
            pass
        else:
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
            break

    else:
        print("Not a valid answer.")