from tkinter import *
from tkinter import messagebox


class KonversiBilanganGUI:
    def __init__(self, master, konversi_bilangan_logic):
        self.master = master
        self.konversi_bilangan_logic = konversi_bilangan_logic
        self.master.title("Konversi Bilangan")
        self.master.geometry("400x300")


        # Label untuk memasukkan angka
        self.label1 = Label(self.master, text="Masukkan Angka:", font=("Helvetica", 14))
        self.label1.grid(row=0, column=0, padx=10, pady=10)

        # Entry untuk memasukkan angka
        self.entry1 = Entry(self.master, width=30)
        self.entry1.grid(row=0, column=1, padx=10, pady=10)
        self.entry1.bind("<Return>", lambda event: self.convert())  # Menambahkan keyboard binding pada tombol enter

        # Label untuk memilih jenis bilangan
        self.label2 = Label(self.master, text="Pilih Jenis Bilangan:")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        # Option Menu untuk memilih jenis bilangan
        self.options = ["Desimal", "Biner", "Oktal", "Heksadesimal", "ascii"]
        self.variable = StringVar(self.master)
        self.variable.set(self.options[0])
        self.option_menu = OptionMenu(self.master, self.variable, *self.options)
        self.option_menu.grid(row=1, column=1, padx=10, pady=10)

        # Button untuk konversi
        self.button = Button(self.master, text="Konversi", command=self.convert, bg="#4CAF50",
                             fg="white", activebackground="#60A347", width=10)
        self.button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Label untuk menampilkan hasil konversi
        self.label3 = Label(self.master, text="", font=("Helvetica", 14))
        self.label3.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def convert(self):
        try:
            # Mengambil angka dan jenis bilangan dari input
            num = self.entry1.get()
            base = self.variable.get()

            # Konversi bilangan
            result = self.konversi_bilangan_logic.convert(num, base)

            # Menampilkan hasil konversi
            self.label3.config(text=result)

        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")
