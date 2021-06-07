# Example Of request
import requests
from tkinter import *


def fetch_chucks_joke():
    response = requests.get("https://api.chucknorris.io/jokes/random")

    return response.json()["value"]


root = Tk()
root.geometry("400x400")

joke_message = Message(root, text = fetch_chucks_joke())
joke_message.pack()


def update_joke_message():
    from time import sleep
    sleep(5)
    while True:
        joke_message.configure(text = fetch_chucks_joke())
        sleep(5)
        print("Called")


update_joke_message()
root.mainloop()
