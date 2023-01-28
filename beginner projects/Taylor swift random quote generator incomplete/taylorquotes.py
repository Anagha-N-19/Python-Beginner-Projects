from tkinter import *
import requests


def get_quote():
    response = requests.get(url='https://api.kanye.rest/')
    response.raise_for_status()
    data = response.json()
    quote = data['quote']
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Taylor Swift Lyrics")
window.config(padx=50, pady=50, bg="#EBC7E6")

canvas = Canvas(width=300, height=400)
background_img = PhotoImage('rose_bg.png')
canvas.create_image(150, 200, image=background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 15, "bold"), fill="black")
canvas.grid(row=0, column=0)
response = requests.get(url=' https://taylorswiftapi.onrender.com/get')
response.raise_for_status()
data = response.json()
quote = data['quote']

if "/" in quote:
    quote = quote.replace("/","\n")
canvas.itemconfig(quote_text, text=quote)

tay_img = PhotoImage('taylor2.png')
tay_button = Button(image=tay_img, highlightthickness=5, command=get_quote)
tay_button.grid(row=1, column=0)

window.mainloop()
