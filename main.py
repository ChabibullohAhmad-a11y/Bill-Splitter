"""
Bill Splitter - Skrip Dasar Perhitungan Tagihan

Skrip ini mendemonstrasikan logika inti pembagian tagihan makanan:
menghitung subtotal, menambahkan tip 25%, lalu membagi total
ke setiap orang. Versi antarmuka desktop tersedia pada gui.py.
"""

# ---------------------------------------------------------------------------
# Inisialisasi data input
# ---------------------------------------------------------------------------

# Akumulator untuk menyimpan total biaya pesanan.
running_total = 0

# Jumlah orang yang akan berbagi tagihan.
num_of_friends = 4

# Nominal biaya untuk setiap kategori pesanan.
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# ---------------------------------------------------------------------------
# Perhitungan subtotal
# ---------------------------------------------------------------------------

# Menjumlahkan seluruh kategori pesanan sebelum tip ditambahkan.
running_total = appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

# ---------------------------------------------------------------------------
# Perhitungan tip 25%
# ---------------------------------------------------------------------------

# Tip dihitung dari subtotal pesanan, bukan dari total setelah tip.
tip = running_total * 0.25
print('Tip amount:', tip)

# Menambahkan nominal tip ke subtotal untuk memperoleh total tagihan.
running_total += tip
print('Total with tip:', running_total)

# ---------------------------------------------------------------------------
# Pembagian tagihan per orang
# ---------------------------------------------------------------------------

# Total tagihan dibagi rata berdasarkan jumlah orang.
final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

# ---------------------------------------------------------------------------
# Pembulatan nominal akhir
# ---------------------------------------------------------------------------

# Membulatkan hasil pembagian ke dua angka desimal agar nominal lebih rapi.
each_pays = round(final_bill, 2)
print('Each person pays:', each_pays)
