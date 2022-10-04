print("Dibuat oleh : Hamzah Nasrulloh")
print("NIM : 211001117")
print(  )

from random import choice

DaftarNama = ['Septi', 'Bayu', 'Budi', 'Tono', 'Dika', 'Danu', 'Anto', 'Elga', 'Safi', 'Anto']

tebak = choice(DaftarNama)

nyawa = 3
GameOver = False
tebakan = []
hasil = [u'\u2bbf '] * len(tebak)

while not GameOver:

    print("kesempatan : {}".format(1*nyawa))
    print("Nama Tertebak : {}".format(tebakan))

    hidden_word = ''.join(hasil)
    print("Tebak nama berikut : {}".format(hidden_word))
    print("ketik 'exit' untuk berhenti bermain")
    nama = input("Tebak 1 nama : ").lower()


    if nama == 'exit':
        print("Terimakasih telah bermain , Bye")
        GameOver =True
    elif nama in tebak and nama not in tebakan:
        print("Tebakan anda benar ! ")
        for i in range(len(tebak)):
            if tebak[i] == nama:
                hasil[i] = nama
    elif nama in tebakan:
        print("Nama Sudah di tebak sebelumnya, coba lagi")
    else:
        nyawa -= 1
        print("tebakan anda salah")

        
    if nyawa == 1:
        print("Ini kesempatan terakhir anda")
    elif nyawa <= 0:
        print("Kesempatan anda habis, anda kalah")
        GameOver = True
    elif nama == ''.join(hasil):
        print("anda berhasil menebak nama tersembunyi : ()".format(''.join(hasil)))
        GameOver = True