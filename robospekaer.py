
import subprocess

if __name__ == "__main__":
    print("Welcome to RoboSpeaker 2.2. Created by Shadan")

    while True:
        x = input("Enter what you want me to speak: ")

        if x.lower() == "q":
            break

        command = f'Add-Type -AssemblyName System.Speech; $speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; $speak.Speak("{x}")'

        subprocess.run(["powershell", "-Command", command])