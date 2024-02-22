import random
from colorama import Fore, Back, Style
from googletrans import Translator
import pyttsx3

translate = Translator()
w=[]
redBack=Back.RED
greenBack=Back.GREEN
green=Fore.GREEN
red=Fore.RED
blue=Fore.BLUE
yellow=Fore.LIGHTYELLOW_EX
cyan=Fore.CYAN
reset=Style.RESET_ALL

with open("words.txt", "r") as f:
    words = f.readlines()
    for word in words:
        l=[]
        word = word.strip()
        word=word.split(" ")
        for i in word:
            if i!="":
                l.append(i)
        w.append(l)

used_words = []
wrong_words = []

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__=="__main__":
    print(Fore.MAGENTA+
            """\n\tIMPROVE YOUR ENGLISH\n"""+reset)

    while True:
        print(cyan+"press 'q' to quit or 's' to show results"+reset)
        wr=random.choice(w)
        word=wr[0].lower()
        meaning=translate.translate(word, dest='tr').text.lower().capitalize()

        while word in used_words:
            wr=random.choice(w)
            word=wr[0].lower()
            meaning=translate.translate(word, dest='tr').text.lower().capitalize()

        print(f"Word:{blue} {word.capitalize()} {reset} Type: {yellow} {wr[1].capitalize()} {reset} Level: {green} {wr[2]} {reset}")
        speak(f"{word.capitalize()}")  # Kelimeyi seslendir
        k=input("Enter the meaning of the word: ").capitalize()

        if k=="q" or k=="Q":
            print(f"\n{greenBack}Correct Answers:{reset} {', '.join([green + word.capitalize() + reset if word in used_words else cyan + word.capitalize() + reset for word in used_words])}")
            print(f"{redBack}Wrong Answers:{reset} {', '.join([red + word.capitalize() + reset if word in wrong_words else cyan + word.capitalize() + reset for word in wrong_words])}\n")
            m = input("Press 'm' to continue or any other key to quit: ")
            if m.lower() == 'm':
                continue
            else:
                break
        elif k=="s" or k=="S":
            print(f"\n{greenBack}Correct Answers:{reset} {', '.join([green + word.capitalize() + reset if word in used_words else cyan + word.capitalize() + reset for word in used_words])}")
            print(f"{redBack}Wrong Answers:{reset} {', '.join([red + word.capitalize() + reset if word in wrong_words else cyan + word.capitalize() + reset for word in wrong_words])}\n")
            continue
        elif k==meaning:
            used_words.append(word)
            print(f"{greenBack}CORRECT!!{reset}\n")
        elif k!=meaning:
            wrong_words.append(word)
            print(f"{redBack}WRONG!!{reset} The meaning of the word is {cyan} {meaning} {reset}\n")
