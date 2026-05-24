try:
    # input nama file
    file1 = input("Masukkan nama file pertama: ")
    file2 = input("Masukkan nama file kedua: ")

    # membuka file
    f1 = open(file1, "r")
    f2 = open(file2, "r")

    # membaca isi file lalu ubah menjadi lowercase
    teks1 = f1.read().lower()
    teks2 = f2.read().lower()

    # ubah menjadi set kata
    kata1 = set(teks1.split())
    kata2 = set(teks2.split())

    # mencari kata yang sama
    hasil = kata1.intersection(kata2)

    print("\nKata-kata yang muncul di kedua file:")
    print(hasil)

    # tutup file
    f1.close()
    f2.close()

except FileNotFoundError:
    print("Error: File tidak ditemukan.")

except:
    print("Error: File tidak dapat dibaca.")