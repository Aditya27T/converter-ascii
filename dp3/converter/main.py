from lib2to3.pgen2.token import STRING
from os import replace, system
from tkinter import *


def heading():
    system('cls')
    print('=====================================')
    print('Konversi Bilangan'.center(40))
    print('=====================================')  

def menu():
    heading()
    print('| 1. Desimal                        |')
    print('| 2. Biner                          |')
    print('| 3. Oktal                          |')
    print('| 4. Hexadecimal                    |')
    print('| 5. ASCII                          |')
    print('| 6. keluar                         |')
    print('=====================================')
    pilih2 = input('menu konversi pilihan :')
    if pilih2 == '1':
        desimal()
    elif pilih2 == '2':
        biner()
    elif pilih2 == '3':
        oktal()
    elif pilih2 == '4':
        hexadecimal()
    elif pilih2 == '5':
        string_to_ascii()
    elif pilih2 == '6':
        keluar()
    else:
        errorInput()

def errorInput():
    error1 = input("Menu Tidak Ada ! [Enter]")
    menu()

def desimal():
    heading()
    try:
        angka = int(input("Masukkan Bilangan Desimal : "))
    except ValueError:
        error = input ("Bilangan Tidak Sesuai! ulangi[Enter]")
        desimal()
    bineri = bin(angka).replace("0b","")
    oktal = oct(angka).replace("0o","")
    heks = hex(angka).replace("0x","")
    
    print('=====================================')
    print('| Biner : ',bineri)
    print('| Oktal : ',oktal)
    print('| Hexa  : ',heks)
    print('=====================================')
    kembali = input('Ulangi Konversi? [y/t]')
    if kembali == "y" or kembali == "Y":
        desimal()
    else:
        ulang()
    

def biner():
    heading()
    try:
        angka = int(input("Masukkan Bilangan Biner : "),2)
    except ValueError:
        error = input ("Bilangan Tidak Sesuai! ulangi[Enter]")
        biner()
    oktal = oct(angka).replace("0o","")
    heks = hex(angka).replace("0x","")

    print('=====================================')
    print('| Decimal : ',angka)
    print('| Oktal   : ',oktal)
    print('| Hexa    : ',heks)
    print('=====================================')
    kembali = input("Kembali ke konversi [y/t] : ")
    if kembali == "y" or kembali == "Y":
        biner()
    else:
        ulang()

def oktal():
    heading()
    try:
        angka = int(input("Masukkan Bilangan Oktal : "),8)
    except ValueError:
        error = input ("Bilangan Tidak Sesuai! ulangi[Enter]")
        oktal()
    biner = bin(angka).replace("0b","")
    heks = hex(angka).replace("0x","")

    print('=====================================')
    print('| Decimal : ',angka)
    print('| biner   : ',biner)
    print('| Hexa    : ',heks)
    print('=====================================')
    kembali = input("Kembali ke konversi [y/t] : ")
    if kembali == "y" or kembali == "Y":
        oktal()
    else:
        ulang()

def hexadecimal():
    heading()
    try:
        angka = int(input("Masukkan Bilangan Hexa : "),16)
    except ValueError:
        error = input ("Bilangan Tidak Sesuai! ulangi[Enter]")
        hexadecimal()
    biner = bin(angka).replace("0b","")
    oktal = oct(angka).replace("0o","")
    
    print('=====================================')
    print('| Decimal : ',angka)
    print('| Biner   : ',biner)
    print('| Oktal   : ',oktal)
    print('=====================================')
    kembali = input("Kembali ke konversi [y/t] : ")
    if kembali == "y" or kembali == "Y":
        hexadecimal()
    else:
        ulang()


def string_to_ascii():
    heading()
    try:
        string = input("Masukkan string: ")
    except ValueError:
        error = input("Input tidak valid! Tekan [Enter] untuk mengulangi...")
        string_to_ascii()
        
    ascii_string = ""
    
    for character in string:
        ascii_string += str(ord(character)) + " "

    print('=====================================')
    print('| STRING : ', string)
    print('| ASCII  : ', ascii_string)
    print('=====================================')
    kembali = input("Kembali ke konversi [y/t] : ")
    if kembali == "y" or kembali == "Y":
        string_to_ascii()
    else:
        ulang()

def keluar():
    exit()

def ulang():
    x = 0
    while x == 0:
        ulang = input('Kembali ke menu [y/t] : ')
        if ulang == 'y':
            menu()
        elif ulang == 't':
            exit()
        else:
            errorInput()


menu()