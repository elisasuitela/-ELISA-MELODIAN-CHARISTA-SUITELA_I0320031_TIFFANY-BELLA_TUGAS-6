nilai_angka = input("masukkan nilai yang akan dihitung rata - rata nya (beri tanda koma sebagai pembatas tiap angka yang dimasukkan, contoh 1,2,3,4,5, dst): ")
split_nilai = nilai_angka.split(',')
daftar_nilai = [int(x) for x in split_nilai]

hasil_penjumlahan = 0
for nilai in daftar_nilai:
    hasil_penjumlahan += nilai


hasil_rata_rata = hasil_penjumlahan / len(daftar_nilai)
print("Rata - rata dari bilangan - bilangan tersebvut adalah: ", hasil_rata_rata)