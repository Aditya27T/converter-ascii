from tkinter import *
from tkinter import messagebox
print("tkinter version: ", TkVersion)

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Konversi Bilangan")

        # Mengatur ukuran window
        self.master.geometry("400x300")
        
        # Frame untuk widget input
        self.input_frame = Frame(self.master)
        self.input_frame.pack(pady=10)
        
        # Label untuk memasukkan angka
        self.label1 = Label(self.input_frame, text="Masukkan Angka:")
        self.label1.pack(side=LEFT, padx=5)
        
        # Entry untuk memasukkan angka
        self.entry1 = Entry(self.input_frame, width=30)
        self.entry1.pack(side=LEFT, padx=5)
        self.entry1.bind("<Return>", lambda event: self.convert())  # Menambahkan keyboard binding pada tombol enter

        # Frame untuk memilih jenis bilangan
        self.option_frame = Frame(self.master)
        self.option_frame.pack(pady=10)

        # Label untuk memilih jenis bilangan
        self.label2 = Label(self.option_frame, text="Pilih Jenis Bilangan:")
        self.label2.pack(side=LEFT, padx=5)
        
        # Option Menu untuk memilih jenis bilangan
        self.options = ["Desimal", "Biner", "Oktal", "Heksadesimal", "ascii"]
        self.variable = StringVar(self.master)
        self.variable.set(self.options[0])
        self.option_menu = OptionMenu(self.option_frame, self.variable, *self.options)
        self.option_menu.pack(side=LEFT, padx=5)
        
        # Frame untuk tombol konversi dan hasil konversi
        self.button_frame = Frame(self.master)
        self.button_frame.pack(pady=10)
        
        # Button untuk konversi
        self.button = Button(self.button_frame, text="Konversi", command=self.convert)
        self.button.pack(side=LEFT, padx=5)

        # Frame untuk menampilkan hasil konversi
        self.result_frame = Frame(self.master)
        self.result_frame.pack(pady=10)

        # Label untuk menampilkan hasil konversi
        self.label3 = Label(self.result_frame, text="", width=40, height=10, anchor=NW, justify=LEFT)
        self.label3.pack(side=LEFT, padx=5)
    
    def convert(self):
        try: 
            # Mengambil angka dan jenis bilangan dari input
            num = self.entry1.get()
            base = self.variable.get()
        
            # Konversi bilangan
            if base == "Desimal":
                bin_num = bin(int(num))[2:]
                oct_num = oct(int(num))[2:]
                hex_num = hex(int(num))[2:].upper()
                ascii_num = chr(int(num))
            elif base == "Biner":
                dec_num = int(num, 2)
                oct_num = oct(dec_num)[2:]
                hex_num = hex(dec_num)[2:].upper()
                ascii_num = chr(dec_num)
            elif base == "Oktal":
                dec_num = int(num, 8)
                bin_num = bin(dec_num)[2:]
                hex_num = hex(dec_num)[2:].upper()
                ascii_num = chr(dec_num)
            elif base == "Heksadesimal":
                dec_num = int(num, 16)
                bin_num = bin(dec_num)[2:]
                oct_num = oct(dec_num)[2:]
                ascii_num = chr(dec_num)
            elif base == "ascii":
                dec_num = ord(num)
                bin_num = bin(dec_num)[2:]
                oct_num = oct(dec_num)[2:]
                hex_num = hex(dec_num)[2:].upper()
        
            # Menampilkan hasil konversi
            if base == "Desimal":
                self.label3.config(text = "Biner: " + bin_num + "\nOktal: " + oct_num + "\nHeksadesimal: " + hex_num + "\nASCII: " + ascii_num)
            elif base == "Biner":
                self.label3.config(text="Desimal: " + str(dec_num) + "\nOktal: " + oct_num + "\nHeksadesimal: " + hex_num + "\nASCII: " + ascii_num)
            elif base == "Oktal":
                self.label3.config(text="Desimal: " + str(dec_num) + "\nBiner: " + bin_num + "\nHeksadesimal: " + hex_num + "\nASCII: " + ascii_num)
            elif base == "Heksadesimal":
                self.label3.config(text="Desimal: " + str(dec_num) + "\nBiner: " + bin_num + "\nOktal: " + oct_num + "\nASCII: " + ascii_num)
            elif base == "ascii":
                self.label3.config(text="Desimal: " + str(dec_num) + ", Biner: " + bin_num + ", Oktal: " + oct_num + ", Heksadesimal: " + hex_num)

        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")
    

root = Tk()
app = App(root)
root.mainloop()
