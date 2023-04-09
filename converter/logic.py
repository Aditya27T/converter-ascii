class KonversiBilanganLogic:
    def convert(self, num, base):
        try:
            if base == "ascii":
                num = ord(num)
            else:
                num = int(num, self.get_base(base))
            
            bin_num = bin(num)[2:]
            oct_num = oct(num)[2:]
            hex_num = hex(num)[2:].upper()
            ascii_num = chr(num)
            
            result = "Desimal: " + str(num) + "\n"
            result += "Biner: " + bin_num + "\n"
            result += "Oktal: " + oct_num + "\n"
            result += "Heksadesimal: " + hex_num + "\n"
            result += "ASCII: " + ascii_num
            
            return result
        
        except ValueError:
            raise ValueError("Masukkan angka yang valid!")
    
    def get_base(self, base):
        if base == "Desimal":
            return 10
        elif base == "Biner":
            return 2
        elif base == "Oktal":
            return 8
        elif base == "Heksadesimal":
            return 16
        elif base == "ascii":
            return 10
