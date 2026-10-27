import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memformat angka ke format Rupiah dengan pemisah ribuan titik
def format_rupiah(amount):
    return f"Rp {int(round(amount)):,}".replace(",", ".")

# Fungsi untuk membaca nominal input (mendukung format 25000, 25.000, atau 25.000,50)
def parse_rupiah(value):
    cleaned = value.strip().lower().replace("rp", "").replace(" ", "")
    if not cleaned:
        return 0
    cleaned = cleaned.replace(".", "").replace(",", ".")
    return float(cleaned)

# Fungsi untuk menghitung total dan pembagian tagihan
def calculate_split():
    try:
        # Mengambil data dari inputan user
        num_friends = int(entry_friends.get().strip())
        appetizers = parse_rupiah(entry_appetizers.get())
        main_courses = parse_rupiah(entry_main_courses.get())
        desserts = parse_rupiah(entry_desserts.get())
        drinks = parse_rupiah(entry_drinks.get())
        
        if num_friends <= 0:
            messagebox.showerror("Error", "Jumlah orang tidak boleh 0 atau negatif!")
            return

        # Kalkulasi (dibulatkan sempurna ke bilangan bulat)
        running_total = round(appetizers + main_courses + desserts + drinks)
        tip = round(running_total * 0.25)
        total_with_tip = round(running_total + tip)
        each_pays = round(total_with_tip / num_friends)

        # Menampilkan hasil ke label output
        result_text = (
            f"Subtotal: {format_rupiah(running_total)}\n"
            f"Tip (25%): {format_rupiah(tip)}\n"
            f"Total + Tip: {format_rupiah(total_with_tip)}\n"
            f"----------------------------------\n"
            f"Masing-masing Bayar: {format_rupiah(each_pays)}"
        )
        lbl_result.config(text=result_text)

    except ValueError:
        messagebox.showerror("Format Salah", "Harap masukkan angka yang valid (contoh: 25000 atau 25.000)!")

# Membuat Jendela Utama (Window)
root = tk.Tk()
root.title("Bill Splitter Desktop App")
root.geometry("380x480")
root.resizable(False, False)

# Judul Aplikasi
lbl_title = tk.Label(root, text="Bill Splitter Calculator", font=("Arial", 16, "bold"))
lbl_title.pack(pady=15)

# Frame Form Input
frame_form = tk.Frame(root)
frame_form.pack(pady=5)

# Input Jumlah Orang
tk.Label(frame_form, text="Jumlah Orang:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
entry_friends = tk.Entry(frame_form, font=("Arial", 10), width=15)
entry_friends.grid(row=0, column=1, padx=10, pady=5)
entry_friends.insert(0, "4") # Nilai default

# Input Appetizers
tk.Label(frame_form, text="Makanan Pembuka (Rp):", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
entry_appetizers = tk.Entry(frame_form, font=("Arial", 10), width=15)
entry_appetizers.grid(row=1, column=1, padx=10, pady=5)
entry_appetizers.insert(0, "25000")

# Input Main Courses
tk.Label(frame_form, text="Makanan Utama (Rp):", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
entry_main_courses = tk.Entry(frame_form, font=("Arial", 10), width=15)
entry_main_courses.grid(row=2, column=1, padx=10, pady=5)
entry_main_courses.insert(0, "45000")

# Input Desserts
tk.Label(frame_form, text="Makanan Penutup (Rp):", font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=5)
entry_desserts = tk.Entry(frame_form, font=("Arial", 10), width=15)
entry_desserts.grid(row=3, column=1, padx=10, pady=5)
entry_desserts.insert(0, "20000")

# Input Drinks
tk.Label(frame_form, text="Minuman (Rp):", font=("Arial", 10)).grid(row=4, column=0, sticky="w", pady=5)
entry_drinks = tk.Entry(frame_form, font=("Arial", 10), width=15)
entry_drinks.grid(row=4, column=1, padx=10, pady=5)
entry_drinks.insert(0, "15000")

# Tombol Hitung
btn_calculate = tk.Button(root, text="Hitung Tagihan", font=("Arial", 11, "bold"), bg="#000435", fg="white", width=20, command=calculate_split)
btn_calculate.pack(pady=15)

# Area Output Hasil
lbl_result = tk.Label(root, text="", font=("Arial", 10, "bold"), fg="#121212", justify="left")
lbl_result.pack(pady=5)

# Menjalankan Aplikasi
root.mainloop()