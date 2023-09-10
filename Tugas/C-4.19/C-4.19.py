# Fungsi rekursif untuk mengatur ulang urutan bilangan bulat
def rearrange_even_odd(arr, start=0, end=None):
    # Jika end tidak ditentukan, atur nilai default ke panjang array
    if end is None:
        end = len(arr) - 1

    # Basis: Jika start melebihi end, rekursi selesai
    if start >= end:
        return arr

    # Jika elemen di indeks start adalah ganjil, cari elemen genap dari belakang
    if arr[start] % 2 == 1:
        while arr[end] % 2 == 1 and end > start:
            end -= 1
        # Tukar elemen ganjil dan genap
        arr[start], arr[end] = arr[end], arr[start]

    # Rekursi: Lanjutkan ke elemen berikutnya
    return rearrange_even_odd(arr, start + 1, end)

# Input dari pengguna melalui terminal
input_sequence = input("Input sequence of integers (separated by spaces): ")
sequence = list(map(int, input_sequence.split()))

# Panggil fungsi untuk mengatur ulang urutan
rearranged_sequence = rearrange_even_odd(sequence)

# Mencetak hasil yang telah diatur ulang
print("Rearranged sequence:", rearranged_sequence)
