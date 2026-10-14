Progam Ganjil Genap
print("===Program Cek Ganjil Genap===")
angka = int(input("Masukkan sebuah bilangan bulat: "))

if angka % 2 == 0:
    print(f"{angka} merupakan bilangan GENAP.")
else:
    print(f"{angka} merupakan bilangan GANJIL.")

print("\n===Program Nilai===")
NilaiAngka = int(input("Masukkan Nilai Angka: "))

if NilaiAngka >= 85:
    NilaiHuruf = 'A'
elif NilaiAngka >= 70:
    NilaiHuruf = 'B'
elif NilaiAngka >= 55:
    NilaiHuruf = 'C'
elif NilaiAngka >= 40:
    NilaiHuruf = 'D'
else:
    NilaiHuruf = 'E'

print(f"Nilai Anda {NilaiAngka}, mendapatkan Indeks Nilai: {NilaiHuruf}")
