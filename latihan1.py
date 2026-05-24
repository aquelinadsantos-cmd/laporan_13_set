# input jumlah kategori
n = int(input("Masukkan jumlah kategori: "))

# dictionary untuk menyimpan data kategori
data_aplikasi = {}

# input kategori dan aplikasi
for i in range(n):
    kategori = input("Masukkan nama kategori: ")

    aplikasi = []

    print("Masukkan 5 nama aplikasi")

    for j in range(5):
        nama = input("Nama aplikasi: ")
        aplikasi.append(nama)

    data_aplikasi[kategori] = aplikasi

# tampilkan data aplikasi
print("\nDaftar aplikasi setiap kategori:")
for kategori, aplikasi in data_aplikasi.items():
    print(kategori, ":", aplikasi)

# ubah list menjadi set
semua_set = {}

for kategori, aplikasi in data_aplikasi.items():
    semua_set[kategori] = set(aplikasi)

# mencari aplikasi yang muncul di semua kategori
hasil = list(semua_set.values())[0]

for s in list(semua_set.values())[1:]:
    hasil = hasil.intersection(s)

print("\nAplikasi yang muncul di semua kategori:")
print(hasil)

# gabungkan semua aplikasi
semua_aplikasi = []

for aplikasi in semua_set.values():
    semua_aplikasi.extend(aplikasi)

# aplikasi yang muncul satu kategori saja
unik = set()

for app in semua_aplikasi:
    if semua_aplikasi.count(app) == 1:
        unik.add(app)

print("\nAplikasi yang hanya muncul di satu kategori:")
print(unik)

# aplikasi yang muncul tepat di dua kategori
if n > 2:
    dua_kategori = set()

    for app in set(semua_aplikasi):
        if semua_aplikasi.count(app) == 2:
            dua_kategori.add(app)

    print("\nAplikasi yang muncul tepat di dua kategori:")
    print(dua_kategori)