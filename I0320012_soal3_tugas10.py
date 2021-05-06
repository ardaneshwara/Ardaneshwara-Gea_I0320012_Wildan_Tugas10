print("===== Selamat datang di Program Biodata Kelas A ===== ")
print("")

# Ambil input dari user
nama_lengkap = input("Nama lengkap: ")
nama_panggilan = input("Nama panggilan: ")
umur = input("Umur: ")
jenis_kelamin = input("Jenis Kelamin: ")
alamat = input("Alamat: ")
hobi = input("Hobi: ")

# format teks
teks = "Nama lengkap: {}\nNama panggilan: {}\nUmur: {}\nJenis Kelamin: {}\nAlamat: {}\nHobi: {}".format(nama_lengkap, nama_panggilan, umur, jenis_kelamin, alamat, hobi)

# buka file untuk ditulis
file_bio = open("biodata.txt", "a")

# tulis teks ke file
file_bio.write(teks)

# tutup file
file_bio.close()