import random

angka_random = random.randint(1, 10)
tebak = 0

while tebak != angka_random:
    tebak = int (input("Tebak angka antara 1 sampai 10: "))
    if tebak < angka_random:
        print("Coba lagi, tebakan anda terlalu rendah")
    elif tebak > angka_random:
        print("Coba lagi, tebakan anda terlalu tinggi")
print(f"Selamat, Anda berhasil menebak angka {angka_random} ")