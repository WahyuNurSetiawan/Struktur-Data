print("Program Mengecek Kata Palindrom atau Bukan Palindrom")
print()

# Inputan beresta aturan minor
kata = input("Input Kata : ")
kata = kata.strip() # Hapus spasi
kata = kata.lower() # Menjadikan huruf kecil

# Variabel Sementara untuk menyimpan kata yang akan dibalik
temp = ""

# Memulai perulangan untuk mengambil setiap karakter dari kata, dimulai dari belakang (dari indeks terakhir ke indeks pertama)
for i in range(len(kata)-1, -1, -1):
    # Mengambil karakter saat ini dan menambahkannya ke variabel 'temp'
    temp += kata[i]
    
# Mencetak pesan "Hasil : " tanpa baris baru (end="")
print("Hasil : ", end="")

# Memeriksa apakah kata asli sama dengan kata yang sudah dibalik
if(kata == temp):
    # Jika sama
    print("Palindrom")
else:
    # Jika berbeda
    print("Bukan Palindrom")


