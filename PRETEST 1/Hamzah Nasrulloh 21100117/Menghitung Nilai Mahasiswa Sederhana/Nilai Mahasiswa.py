print("Dibuat oleh : Hamzah Nasrulloh")
print("NIM : 211001117")
print(  )

print("Program Python Menghitung Nilai Mahasiswa Sederhana")

nama=input("Masukkan Nama :")
nim=input("Maukkan NIM :")
MataKuliah=input("Masukkan Mata Kuliah :")
semester=input("Masukkan Semester :")
presensi=float(input("Masukkan Presensi Mahasiswa :"))
tugas=float(input("Masukkan Nilai Tugas :"))
quiz=float(input("Masukkan Nilai Quiz :"))
pratikum=float(input("Masukkan Nilai Pratikum :"))
uts=float(input("Masukkan Nilai UTS :"))
uas=float(input("Masukkan Nilai UAS :"))

na=(presensi * 0.1) + (tugas * 0.3) + (quiz * 0.1) + (pratikum * 0.2) + (uts * 0.1) + (uas * 0.2)

print("========= HASIL PERHITUNGAN =========")

print("Nama :",nama)
print("NIM :",nim)
print("Mata Kuliah :",MataKuliah)
print("Pesensi :",presensi)
print("Nilai Tugas :",tugas)
print("Nilai Quiz :",quiz)
print("Nilai Pratikum :",pratikum)
print("Nilai UTS :" ,uts)
print("Nilai UAS :",uas)
print("Nilai Akhir :",na)

if na >=81:
    print("Grade : A")
if na >=76:
    print("Grade : B+")
if na >=66:
    print("Grade : B")
if na >=61:
    print("Grade : C+")
if na >=51:
    print("Grade : C")
if na >=26:
    print("Grade : D")
if na >=0:
    print("Grade : E")

if na >=51:
    print("Keterangan : LULUS")
else:
    print("Keterangan : TIDAK LULUS")