import win32com.client as wincom

if __name__ == '__main__':
     print("Welcome to Robo Speaker 1.1. Created by Shubham")
     while True:
         speak = wincom.Dispatch("SAPI.SpVoice")
         x = input("Enter what you want me to speak: ")
         if x == "y":
             text= "Bye Bye Friends"
             speak.Speak(text)
             break
         command = f"{x}"
         speak.Speak(command)

