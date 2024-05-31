from tkinter import Tk, Label, Entry, Button, Radiobutton, IntVar, StringVar, Toplevel, Frame, font, messagebox
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from datetime import datetime, timedelta

# Global variable declaration
global nama_pemesan_entry

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class UserService:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.data = {
            "customer": {
                "username": "customer",
                "password": "123",
                "role": "Customer"
            }
        }

    def checkCredentials(self):
        if self.username in self.data:
            user_data = self.data[self.username]
            if self.password == user_data['password']:
                return user_data
        return False

    def login(self):
        get_data = self.checkCredentials()
        if get_data:
            print("\nSelamat Datang di Gacor Arena", get_data['role'])
            print("Logged in as user username:", get_data['username'])
            window_Pemesanan()  # Pindah ke halaman selanjutnya setelah login berhasil
            return True
        else:
            print("\nInvalid Login!\n")
            return False

app = Tk()
app.geometry('500x400')
app.title('Pemesanan Lapangan Bulutangkis By Mustofa Ahmad Rusli')
app.resizable(False, False)
app.configure(bg='green')  # Mengatur warna latar belakang utama aplikasi

# Menggunakan font yang lebih menarik
app_font = font.Font(family="Arial", size=10)

# Membuat frame dengan latar belakang putih
login_frame = Frame(app, bg='light blue', width=480, height=300, relief='raised', borderwidth=2)
login_frame.grid(pady=20, padx=20, sticky='nsew')  # Atur padding untuk memusatkan frame

# Judul
title_label = Label(login_frame, text="Selamat Datang di Gacor Arena", bg='light blue', fg='black', font=("Helvetica", 16, "bold"), justify='center')
title_label.grid(row=0, column=0, columnspan=2, pady=30, sticky='ew')

# Mengatur label dan entry untuk username dan password
username_label = Label(login_frame, text="Username:", bg='light blue', fg='black', font=app_font)
username_label.grid(row=1, column=0, sticky='ne', pady=(0))
username_entry = Entry(login_frame, font=app_font, bd=5, width=35)
username_entry.grid(row=2, column=0, columnspan=2, pady=0)

password_label = Label(login_frame, text="Password:", bg='light blue', fg='black', font=app_font)
password_label.grid(row=3, column=0, sticky='ne', padx=10, pady=0)
password_entry = Entry(login_frame, show="*", font=app_font, bd=5, width=35)
password_entry.grid(row=4, column=0, columnspan=2, padx=40, pady=0)

# Mengatur tombol login
def window_Pemesanan():
    global nama_pemesan_entry, calendar
    # Sembunyikan elemen login
    login_frame.grid_remove()

    # Frame baru untuk pemesanan
    pemesanan_frame = Frame(app, bg='light blue', width=500, height=400, relief='raised', borderwidth=2)
    pemesanan_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    # Menampilkan pesan selamat datang
    welcome_label = Label(pemesanan_frame, text="Silahkan Pilih Lapangan", font=("Helvetica", 16), bg='light blue')
    welcome_label.grid(row=0, column=0, columnspan=4, sticky='ew', pady=10)

    nama_pemesan_entry = Entry(pemesanan_frame)
    nama_pemesan_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')
    Label(pemesanan_frame, text='Nama Pemesan:', bg='light blue').grid(row=1, column=0, padx=10, pady=10, sticky='e')

    lapangan_choice = IntVar()
    Durasi = StringVar()
    UangUser = StringVar()
    WaktuMulai = StringVar()

    waktu_options = [f"{hour:02}:00" for hour in range(8, 24)]

    # Menambahkan pilihan lapangan
    Label(pemesanan_frame, text="Pilih Lapangan:", bg='light blue').grid(row=2, column=0, padx=10, pady=10, sticky='w')
    Radiobutton(pemesanan_frame, text="Lapangan A", variable=lapangan_choice, value=1, bg='light blue').grid(row=2, column=1, sticky='w')
    Label(pemesanan_frame, text='Rp. 30000', font='Times 12 bold', bg='light blue').grid(row=2, column=2, sticky='w')
    Radiobutton(pemesanan_frame, text="Lapangan B", variable=lapangan_choice, value=2, bg='light blue').grid(row=3, column=1, sticky='w')
    Label(pemesanan_frame, text='Rp. 35000', font='Times 12 bold', bg='light blue').grid(row=3, column=2, sticky='w')

    # Mengganti Combobox dengan tkcalendar untuk pilihan tanggal dan bulan sewa
    Label(pemesanan_frame, text="Tanggal Sewa:", bg='light blue').grid(row=4, column=0, padx=10, pady=10, sticky='w')
    calendar = DateEntry(pemesanan_frame, selectmode='day', date_pattern='dd/MM/yyyy', locale='id_ID', show_dropdown=True)
    calendar.grid(row=4, column=1, padx=10, pady=10, sticky='w')

    # Mengganti Spinbox dengan Combobox untuk durasi dan waktu mulai
    Label(pemesanan_frame, text="Waktu Mulai:", bg='light blue').grid(row=5, column=0, padx=10, pady=10, sticky='w')
    waktu_mulai_combobox = Combobox(pemesanan_frame, values=waktu_options, textvariable=WaktuMulai)
    waktu_mulai_combobox.grid(row=5, column=1, padx=10, pady=10, sticky='w')
    Label(pemesanan_frame, text="Durasi (jam):", bg='light blue').grid(row=6, column=0, padx=10, pady=10, sticky='w')
    durasi_combobox = Combobox(pemesanan_frame, values=list(range(1, 25)), textvariable=Durasi)
    durasi_combobox.grid(row=6, column=1, padx=10, pady=10, sticky='w')

    # Menambahkan input untuk uang pengguna
    Label(pemesanan_frame, text="Uang Anda (Rp):", bg='light blue').grid(row=7, column=0, padx=10, pady=10, sticky='e')
    Entry(pemesanan_frame, textvariable=UangUser).grid(row=7, column=1, padx=10, pady=10, sticky='w')

    # Menambahkan tombol bayar
    Button(pemesanan_frame, text="Sewa", command=lambda: sewa_button_clicked(lapangan_choice, Durasi, UangUser, WaktuMulai), bg='gold', fg='black').grid(row=8, column=0, columnspan=4, padx=20, pady=20, sticky='n')

def sewa_button_clicked(lapangan_choice, Durasi, UangUser, WaktuMulai):
    # Menghitung total yang harus dibayar
    harga_per_jam = {1: 30000, 2: 35000}
    total = int(Durasi.get()) * harga_per_jam[lapangan_choice.get()]

    def is_valid_name(name):
        return name.isalpha() and name.strip()  # Memastikan input hanya berupa huruf dan tidak kosong

    if is_valid_name(nama_pemesan_entry.get()):
        kembalian(lapangan_choice, Durasi, UangUser, WaktuMulai, total)  # Lanjut ke proses pembayaran
    else:
        messagebox.showwarning("Peringatan", "Masukkan nama yang sesuai.")
    

def kembalian(lapangan_choice, Durasi, UangUser, WaktuMulai, total):
    uang = int(UangUser.get())

    # Cek apakah uang yang dimasukkan cukup
    if uang < total:
        # Uang tidak cukup, tampilkan peringatan
        messagebox.showwarning("Peringatan", "Uang yang Anda masukkan tidak cukup. Silakan masukkan uang yang sesuai.")
        return  # Keluar dari fungsi untuk menghentikan proses lebih lanjut
    

    TanggalBulan = calendar.get_date().strftime("%d %B %Y")
    kembalian = uang - total
    nama_pemesan = nama_pemesan_entry.get()  # Mengambil nama pemesan dari Entry

    # Menghitung waktu selesai
    format_waktu = "%H:%M"
    waktu_mulai = datetime.strptime(WaktuMulai.get(), format_waktu)
    durasi = timedelta(hours=int(Durasi.get()))
    waktu_selesai = waktu_mulai + durasi
    waktu_selesai_str = waktu_selesai.strftime(format_waktu)

    struk_text = (
        "-------------------------------------------------------------------\n"
        "                      PEMESANAN LAPANGAN BULUTANGKIS              \n"
        "-------------------------------------------------------------------\n"
        f"Waktu: {get_current_time()}\n"
        f"Nama Pemesan: {nama_pemesan}\n"
        f"Waktu Mulai: {WaktuMulai.get()}\n"
        f"Waktu Selesai: {waktu_selesai_str}\n"
        f"Tanggal Sewa: {TanggalBulan}\n"
        "-------------------------------------------------------------------\n"
        "Sewa Lapangan:\n"
        f"Lapangan: {'A' if lapangan_choice.get() == 1 else 'B'}\n"
        f"Durasi: {Durasi.get()} jam\n"
        "-------------------------------------------------------------------\n"
        f"Total : Rp {total}\n"
        f"Tunai : Rp {uang}\n"
        f"Kembalian : Rp {kembalian}\n"
        "Terimakasih Telah Bermain di Gacor Arena,\n"
        "Semoga Hari Anda Menyenangkan :D\n"
        "-------------------------------------------------------------------\n"
    )

    # Display the receipt in a new window
    receipt_window = Toplevel(app)
    receipt_window.title("Struk Pembayaran")
    receipt_window.geometry("570x400")
    receipt_window.resizable(False, False)
    receipt_window.configure(bg='light blue')  # Mengatur warna latar belakang window struk

    # Membuat frame baru untuk struk
    receipt_frame = Frame(receipt_window, bg='white', relief='raised', borderwidth=2)
    receipt_frame.pack(fill='both', expand=True)  # Mengisi seluruh window dan memperluas sesuai dengan isi

    # Label untuk menampilkan struk
    Label(receipt_frame, text=struk_text, justify='left', font=('Courier', 10), bg='light blue', fg='black').pack(padx=10, pady=10)

    # Membuat tombol "Previous" dan "Exit" pada window struk
    button_frame = Frame(receipt_frame, bg='white')
    button_frame.pack(side='bottom', pady=10)

    previous_button = Button(button_frame, text="Previous", command=receipt_window.destroy, bg='green', fg='white', width=10, height=2)
    previous_button.pack(side='left', padx=10)

    exit_button = Button(button_frame, text="Exit", command=app.destroy, bg='red', fg='white', width=10, height=2)
    exit_button.pack(side='right', padx=5)

login_button = Button(login_frame, text="Login", command=lambda: UserService(username_entry.get(), password_entry.get()).login(), bg='green', fg='white', font=("Arial", 10, "bold"), width=10)
login_button.grid(row=5, column=0, columnspan=2, padx=200, pady=50, sticky='ne')

# Menyesuaikan tata letak untuk estetika yang lebih baik
app.grid_columnconfigure(0, weight=1)  # Membuat kolom pertama lebih fleksibel dalam ukuran
app.grid_rowconfigure(0, weight=1)  # Membuat baris pertama lebih fleksibel dalam ukuran

# Menampilkan jendela utama
app.mainloop()