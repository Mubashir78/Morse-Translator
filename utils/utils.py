import json
import datetime

date = datetime.datetime.now()

formatted_date = date.strftime("%b %d, %Y - %H:%M:%S")

def encrypt_text(texts):
    """Encrypt Text
    
    Remove whitespaces from text
    """

    
    texts = " ".join(texts.split())

    msg = ""

    """Open json file and convert into a python dict"""
    with open("./utils/json/text_to_morse.json", "r") as morse:
        morse = json.load(morse)
    
    """Loop over the string and check if it matches any dict key
    and add the value to the msg variable if it does match and return the text if it doesn't match anything from the di.
    """
    for text in texts.upper():
        if text in morse.keys():
            msg += morse.get(text) + " "
        else:
            msg += text
    
    return msg


def decrypt_text(codes):
    """Decrypting Morse Code
    
    Splitting the input by spaces
    """

    codes = codes.split()

    msg = ""

    """Open json file and convert into a python dict"""
    with open("./utils/json/morse_to_text.json", "r") as text:
        text = json.load(text)

    """Loop over the list returned by the split function and check if it matches any dict key
    and add the value to the msg variable if it does match and return "#" if the character is not a morse code.
    """
    for code in codes:
        if code in text.keys():
            msg += text[code]
        else:
            msg += "#"
    
    return msg


def save_to_file(texts, morse=False):
    if morse:
        with open("logs.txt", "a") as f:
            f.write(f"Type: Morse-To-Text at {formatted_date}\nValue: {texts}\n" + "-" * 50)
    else:
        with open("logs.txt", "a") as f:
            f.write(f"Type: Text-To-Morse at {formatted_date}\nValue: {texts}\n" + "-" * 50)
