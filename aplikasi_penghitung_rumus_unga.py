def hitung_luas_segitiga():
    alas = float(input("Masukkan alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    luas = 0.5 * alas * tinggi
    print(f"Luas segitiga adalah: {luas:.2f}")

def hitung_luas_persegi_panjang():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    print(f"Luas persegi panjang adalah: {luas:.2f}")

def tentukan_ganjil_genap():
    angka = int(input("Masukkan angka: "))
    if angka % 2 == 0:
        print(f"{angka} adalah angka genap.")
    else:
        print(f"{angka} adalah angka ganjil.")

while True:
    print("===== Program Kalkulator Sederhana =====")
    print("Menu")
    print("1. Hitung Luas Segitiga")
    print("2. Hitung Luas Persegi Panjang")
    print("3. Tentukan number ganjil genap")
    print("4. Quit")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        hitung_luas_segitiga()
    elif pilihan == "2":
        hitung_luas_persegi_panjang()
    elif pilihan == "3":
        tentukan_ganjil_genap()
    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

    print()  # untuk memberi spasi antar menu
