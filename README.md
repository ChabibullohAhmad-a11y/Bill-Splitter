# Bill Splitter

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FFD43B?logo=python&logoColor=black)](https://docs.python.org/3/library/tkinter.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)]()

Aplikasi kalkulator pembagi tagihan makanan berbasis **Python Desktop GUI** dengan mata uang **Rupiah (Rp)**. Masukkan jumlah orang dan biaya makanan/minuman, lalu aplikasi akan menghitung subtotal, tip, total tagihan, dan nominal yang harus dibayar setiap orang secara otomatis.

---

## Tentang Proyek

**Bill Splitter** dibuat untuk mempermudah pembagian tagihan saat makan bersama. Aplikasi ini menggunakan **Tkinter** sebagai antarmuka desktop dan menerapkan format mata uang Indonesia, termasuk pemisah ribuan dengan titik (`.`).

Seluruh perhitungan disajikan dalam bilangan bulat Rupiah tanpa angka desimal, sehingga nominal akhir lebih mudah dibaca dan digunakan.

---

## Fitur Utama

- **Perhitungan otomatis** subtotal dari makanan pembuka, makanan utama, makanan penutup, dan minuman.
- **Tip 25%** dihitung otomatis dari subtotal.
- **Total tagihan** dihitung dari subtotal ditambah tip.
- **Pembagian per orang** berdasarkan jumlah orang yang diinput.
- **Pembulatan penuh ke Rupiah** tanpa angka desimal pada semua hasil perhitungan.
- **Pemisah ribuan format Indonesia** menggunakan titik, contoh: `Rp 131.250`.
- **Parsing input angka yang fleksibel**, mendukung format:
  - `25000`
  - `25.000`
  - `Rp 25.000`
  - `25.000,50`
- **Validasi input** untuk mencegah jumlah orang nol/negatif dan format angka yang tidak valid.

---

## Tech Stack

| Teknologi | Keterangan |
| --- | --- |
| **Python 3** | Bahasa pemrograman utama |
| **Tkinter** | Library GUI bawaan Python untuk antarmuka desktop |
| **tkinter.messagebox** | Menampilkan dialog validasi dan pesan kesalahan |

Aplikasi ini tidak memerlukan dependensi eksternal karena seluruh library yang digunakan merupakan bagian dari **Python Standard Library**.

---

## Prasyarat

- **Python 3.8+** sudah terpasang di komputer.
- **Tkinter** tersedia (biasanya sudah termasuk dalam instalasi Python).

Cek instalasi Python:

```bash
python --version
```

> **Pengguna Linux:** jika Tkinter belum tersedia, instal paket sistem terlebih dahulu.
>
> ```bash
> sudo apt install python3-tk
> ```

---

## Instalasi

1. Clone repositori ini:

   ```bash
   git clone https://github.com/username/Bill-Splitter.git
   ```

2. Masuk ke direktori proyek:

   ```bash
   cd Bill-Splitter
   ```

3. Tidak ada dependensi tambahan yang perlu diinstal.

---

## Menjalankan Aplikasi

Jalankan file GUI dengan Python:

```bash
python gui.py
```

Jika sistem menggunakan perintah `python3`:

```bash
python3 gui.py
```

Jendela **Bill Splitter Calculator** akan terbuka dan siap digunakan.

---

## Cara Penggunaan

1. Isi **Jumlah Orang**.
2. Isi nominal untuk setiap kategori:
   - Makanan Pembuka (Rp)
   - Makanan Utama (Rp)
   - Makanan Penutup (Rp)
   - Minuman (Rp)
3. Klik tombol **Hitung Tagihan**.
4. Hasil perhitungan akan ditampilkan:
   - Subtotal
   - Tip (25%)
   - Total + Tip
   - Masing-masing Bayar

### Contoh Hasil

Dengan jumlah orang **4** dan total biaya **Rp 105.000**:

```text
Subtotal: Rp 105.000
Tip (25%): Rp 26.250
Total + Tip: Rp 131.250
----------------------------------
Masing-masing Bayar: Rp 32.812
```

---

## Struktur Proyek

```text
Bill-Splitter/
├── gui.py          # Aplikasi utama berbasis Tkinter
├── main.py         # Skrip latihan logika perhitungan tagihan
├── LICENSE         # Lisensi MIT
├── .gitignore      # Konfigurasi Git
└── README.md       # Dokumentasi proyek
```

---

## Lisensi

Proyek ini dilisensikan di bawah **MIT License**. Lihat file [LICENSE](LICENSE) untuk informasi lebih lanjut.

---

<p align="center">
  Dibuat dengan Python dan Tkinter.
</p>
