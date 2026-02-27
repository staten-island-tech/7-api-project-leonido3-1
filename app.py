import requests
import tkinter as tk
from tkinter import ttk
def wordfind():
    word = wordentry.get()
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.lower()}")
    if response.status_code != 200:
        defresults.config(text="Error fetching data! ")
        return 
    data = response.json()
    if len(data[0]["meanings"]) > 1:
        defresults.config(text = data[0]["meanings"][1]["definitions"][0]["definition"])
    elif len(data[0]["meanings"][0]["definitions"]) > 1:
        defresults.config(text = data[0]["meanings"][0]["definitions"][0]["definition"])
    else:
        defresults.config(text = data[0]["meanings"][0]["definitions"][-1]["definition"])

def thesfind():
    thesresultsan = []
    thesresultssyn = []
    word = wordentry.get()
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.lower()}")
    if response.status_code != 200:
        defresults.config(text="Error fetching data! ")
    data = response.json()
    thesresultssyn.extend(data[0]["meanings"][0]["synonyms"])
    thesresultsan.extend(data[0]["meanings"][0]["antonyms"])
    print(thesresultsan)
    print(thesresultssyn)
    if len(thesresultsan) > 0 and len(thesresultssyn) >0:
        theslist.config(text=f"The synonyms of {word} are: {", ".join(thesresultssyn)}. The antonyms are {", ".join(thesresultsan)}.")
    elif len(thesresultsan) > 0 and len(thesresultssyn) == 0:
        theslist.config(text=f"There are no synonyms of {word}. The antonyms are {", ".join(thesresultsan)}.")
    elif len(thesresultssyn) > 0 and len(thesresultsan) == 0:
        theslist.config(text=f"The synonyms of {word} are: {", ".join(thesresultssyn)}. There are no antonyms.")
    else:
        theslist.config(text="The word you have inputted lack synonyms or antonyms.")
def done():
    defresults.config(text="")
    theslist.config(text="")
    wordentry.delete(0, "end")
window = tk.Tk()
window.geometry("700x700")
window.grid_columnconfigure(0, weight=1)
window.title("Suburban Dictionary")

title = tk.Label(window, text=("Online Dictionary"), font=("Comic Sans MS", 24))
title.grid(row=0, column=0, pady=10)

button_frame = ttk.Frame(window)
button_frame.grid(row=3, column=0, pady=30, padx=30)
button_frame.grid_columnconfigure(0, weight=1)

results_frame = ttk.Frame(window)
results_frame.grid(row=4, column=0, pady=30, padx=30)
results_frame.grid_columnconfigure(0, weight=1)

searchmsg = tk.Label(window, text="Enter a word to search for: ")
searchmsg.grid(row=1, column=0, pady=20)

wordentry = tk.Entry(window)
wordentry.grid(row=2, column=0, pady=10)

search_button = ttk.Button(button_frame, text="Search for definition!", command=wordfind)
search_button.grid(row=0, column=0, padx=5)

synan_button = ttk.Button(button_frame, text="Search for the synonyms/antonyms!", command=thesfind)
synan_button.grid(row=0, column=1, padx=5)

defresults = tk.Label(results_frame, text=" ")
defresults.grid(row=4, column=0, pady=20)

theslist = tk.Label(results_frame, text=" ")
theslist.grid(row=4, column=1, pady=20)

donebutton = ttk.Button(window, text=("Done"), command=done)
donebutton.grid(row=5, column=0, pady=10)

window.mainloop()