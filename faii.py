from customtkinter import *

window = CTk()
window.geometry("500x500")
window.title("Logika")
window.configure(fg_color="Lightblue")

kinopca = CTkButton(window, text="клікни")
kinopca.pack()

nadpus = CTkButton(window, text="текст")
nadpus.pack()

window.mainloop()