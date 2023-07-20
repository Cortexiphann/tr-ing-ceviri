import tkinter as tk
from translate import Translator

def translate_text():
    text = text_entry.get()

    translator = Translator(from_lang='tr', to_lang='en')
    translated_text = translator.translate(text)

    translated_text_label.config(text=translated_text, fg="blue")

# Tkinter uygulamasını oluşturun
app = tk.Tk()
app.title("Türkçe-İngilizce Çeviri")
app.geometry("400x200")  # Pencere boyutunu ayarlayın

# Etiket ve metin giriş kutusu
tk.Label(app, text="Türkçe Metni Girin:", font=("Arial", 14)).pack()
text_entry = tk.Entry(app, width=50, font=("Arial", 12))
text_entry.pack()

# Çeviri butonu
translate_button = tk.Button(app, text="Çevir", font=("Arial", 12), command=translate_text, bg="green", fg="white")
translate_button.pack()

# Çevrilen metni gösteren etiket
translated_text_label = tk.Label(app, text="", font=("Arial", 14), wraplength=350)
translated_text_label.pack()

# Tkinter uygulamasını başlatın
app.mainloop()
