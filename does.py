from tkinter import *
from tkinter import ttk
import requests
# from tkinter import messagebox

root = Tk()

# StringVar
results = StringVar()
values1 = StringVar()
values2 = StringVar()

# code to add widgets and style window will go here
root.geometry("450x400")
root.title("Currency Converter (Uthmaan Breda)")

information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/USD')
information_json = information.json()

conversion_rates = information_json['conversion_rates']

currency = []
for i in conversion_rates.keys():
    currency.append(i)

currency2 = []
for i in conversion_rates.keys():
    currency2.append(i)

currency_cb = ttk.Combobox(root)
currency_cb['values'] = currency
currency_cb['state'] = 'readonly'
currency_cb.set('Select Currency')
currency_cb.place(x=10, y=50)

currency_cb2 = ttk.Combobox(root)
currency_cb2['values'] = currency2
currency_cb2['state'] = 'readonly'
currency_cb2.set('Select Currency')
currency_cb2.place(x=253, y=50)

Label(root, text='Enter Amount:').place(x=65, y=100)
ent1 = Entry(root)
ent1.place(x=200, y=100)
ent1.focus()
Label(root, text='Converted Amount:').place(x=65, y=150)
Label(root, text='', textvariable=results).place(x=200, y=150)


def convert(from_currency, to_currency, amount):
    # first convert it into USD if it is not in USD.
    # because our base currency is USD
    if from_currency != 'USD':
        amount = amount / conversion_rates[from_currency]

    amount = round(amount * conversion_rates[to_currency], 4)
    return amount


def perform():
    amount = float(ent1.get())
    from_curr = currency_cb.get()
    to_curr = currency_cb2.get()

    converted_amount = convert(from_curr, to_curr, amount)

    results.set(converted_amount)


Button(root, text="<>").place(x=195, y=45)
Button(root, text="convert", borderwidth=3, command=perform).place(x=170, y=200)


root.mainloop()  # continuously runs program in window
