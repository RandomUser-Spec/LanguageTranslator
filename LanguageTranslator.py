from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.config(background = "lightblue")
root.geometry("1000x500")
root.title("Translator")

language = list(LANGUAGES.values())

label_title = Label(root, text = "Language Translator", bg = "lightpink", font = ("Microsoft YaHei UI Light", 25, "bold"))
label_title.place(relx = 0.5, rely = 0.1, anchor = CENTER)

label_entertext = Label(root, bg = "lightblue", text = "Enter Text", font = ("Arial", 15))
label_entertext.place(relx = 0.1, rely = 0.3, anchor = CENTER)

dropdown_source = ttk.Combobox(root, value = language, width = 10, state = "readonly")
dropdown_source.set('english')
dropdown_source.place(relx = 0.2, rely = 0.3, anchor = CENTER)

textarea_i = Text(root, bg = "white", width = 50, height = 10, wrap = WORD, padx = 5, pady = 5, fg = "black")
textarea_i.place(relx = 0.05, rely = 0.5, anchor = W)

label_output = Label(root, bg = "lightblue", text = "Output", font = ("Arial", 15))
label_output.place(relx = 0.63, rely = 0.3, anchor = CENTER)

dropdown_output = ttk.Combobox(root, value = language, width = 10, state = "readonly")
dropdown_output.set('spanish')
dropdown_output.place(relx = 0.72, rely = 0.3, anchor = CENTER)

textarea_o = Text(root, bg = "white", width = 50, height = 10, wrap = WORD, padx = 5, pady = 5, fg = "black")
textarea_o.place(relx = 0.6, rely = 0.5, anchor = W)

def Translate():
    translator = Translator()
    translated = translator.translate(text = textarea_i.get(1.0, END), src = dropdown_source.get(), dest = dropdown_output.get())
    textarea_o.delete(1.0, END)
    textarea_o.insert(END, translated.text)    
    
translatebutton = Button(root, text = "Translate", bg = "lightpink", command = Translate)
translatebutton.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()