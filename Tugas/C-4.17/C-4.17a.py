print("Program Mengecek Kata Palindrom atau Bukan Palindrom")
print()

# Fungsi rekursif untuk memeriksa apakah sebuah string adalah palindrom
def is_palindrome(s):
    # Basis: Jika panjang string adalah 0 atau 1, itu adalah palindrom
    if len(s) <= 1:
        return True
    
    # Rekursi: Periksa karakter pertama dan terakhir, lalu periksa sisa string
    if s[0] == s[-1]:
        # Jika karakter pertama dan terakhir sama, periksa sisa string
        return is_palindrome(s[1:-1])
    else:
        # Jika karakter pertama dan terakhir berbeda, bukan palindrom
        return False

# Inputan beresta aturan minor
kata = input("Input Kata : ")
kata = kata.strip() # Hapus spasi
kata = kata.lower() # Menjadikan huruf kecil

# Panggil fungsi is_palindrome untuk memeriksa apakah string adalah palindrom
if is_palindrome(kata):
    print(f"{kata} adalah palindrom.")
else:
    print(f"{kata} bukan palindrom.")
