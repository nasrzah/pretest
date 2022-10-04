print("Dibuat oleh : Hamzah Nasrulloh")
print("NIM : 211001117")
print(  )

print(10*"=")
print("Kalkulator Sederhana")
print(10*"=")

angka_1 = float(input("masukkan Angka 1 ="))
operator = input("operator (+,-,*,/) =")
angka_2 = float(input("masukkan angka 2 ="))

# Percabangannya

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
else:
    print("Perintah Tidak di kenali")

print("exit maka aplikasi akan keluar")
