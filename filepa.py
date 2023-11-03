import json
import pwinput
import os
import random
from datetime import datetime
from prettytable import PrettyTable

##########################################################################################################################################

# # # # # # # # # # # # # # # # # # # # 
# Kodingan untuk akses file data json #
# # # # # # # # # # # # # # # # # # # # 

os.system("cls") # Menghilangkan jejak file ketika program dijalankan

# Load data from JSON files
data_pengguna = {}
data_produk = []
data_invoice = {}


def load_data_from_json(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

# Membaca data invoice dari file JSON
data_invoice = load_data_from_json('datainvoice.json')


# Mendapatkan direktori kerja saat ini
current_directory = os.getcwd()

# Membuat path lengkap ke file JSON
data_pengguna_file = os.path.join(current_directory, 'datapengguna.json')
data_produk_file = os.path.join(current_directory, 'dataproduk.json')
data_invoice_file = os.path.join(current_directory, 'datainvoice.json')

try:
    with open(data_pengguna_file, "r") as pengguna_file:
        data_pengguna = json.load(pengguna_file)
except FileNotFoundError:
    data_pengguna = {}

try:
    with open(data_produk_file, "r") as produk_file:
        data_produk = json.load(produk_file)
except FileNotFoundError:
    data_produk = []

try:
    with open(data_invoice_file, "r") as invoice_file:
        data_invoice = json.load(invoice_file)
except FileNotFoundError:
    data_invoice = {}

def save_data_to_json(file_nama, data):
    with open(file_nama, 'w') as file:
        json.dump(data, file, indent=4)

def generate_invoice_number():
    return str(random.randrange(1000, 10000))

##########################################################################################################################################

#-----------------------------#
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
#  _________________________  #              
# |Function untuk menu utama| #
#  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  #              
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ # 
#-----------------------------#  



#-----------------------------------------------------------#
# 1. Function untuk menghitung id berikutnya pada data json #
#-----------------------------------------------------------#

def hitung_id_berikutnya():
    used_ids = {int(user_data['id']) for user_data in data_pengguna.values()}
    next_id = 1
    while next_id in used_ids:
        next_id += 1
    return str(next_id)



#--------------------------------#
# 2. Function untuk membuat akun #
#--------------------------------#

def create_account():
    while True:
        try:
            print('''\n
==================================================
‖                                                ‖
‖                  MEMBUAT AKUN                  ‖
‖                                                ‖
==================================================\n''')
            print("(HELP : Tekan ctrl+c untuk membatalkan pembuatan akun)")
            # Menghitung ID terbaru dengan memanggil fungsi hitung_id_berikutnya
            id_pengguna_baru = hitung_id_berikutnya()

            while True:
                role = str(input('''
        _________________________________
        |===>  Silahkan pilih role  <===|
        |                               |
        |            -USER              |
        |            -ADMIN             |
        |                               |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Tentukan opsi anda (user/admin): '''))
                if role.lower() == "admin":
                    kode_admin = pwinput.pwinput("Masukkan angka verifikasi untuk peran admin: ")
                    if kode_admin == "12345":
                        break
                    else:
                        print("\nAngka verifikasi salah. Anda harus memasukkan angka yang benar untuk peran admin.\n")
                elif role.lower() == "user":
                    break
                else:
                    print("\nPrivilege yang diterima hanya 'admin' atau 'user'.\n")
            print('''
__________________________________________________\n''')

            username = input("Masukkan nama pengguna: ")

            if username in [akun_pengguna['username'] for akun_pengguna in data_pengguna.values()]:
                print("\nUsername tersebut sudah digunakan. Pilih username lain.")
                print("Kembali pada menu utama...")
                print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
                return

            password = input("Masukkan kata sandi: ")

            data_pengguna_baru = {'id': id_pengguna_baru, 'username': username, 'password': password, 'role': role}
            data_pengguna[id_pengguna_baru] = data_pengguna_baru
            data_invoice[username] = 0
            save_data_to_json('datapengguna.json', data_pengguna)
            save_data_to_json('datainvoice.json', data_invoice)
            print("Akun pengguna berhasil dibuat.")
            print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            break  # Keluar dari loop create_account setelah akun berhasil dibuat

        except KeyboardInterrupt:
            print("\nPembuatan akun dibatalkan.")
            break

#------------------------------#
# 3. Function untuk login akun #
#------------------------------#


def login():
    while True:
        try:
            print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            print('''\n
==================================================
‖                                                ‖
‖                    LOGIN AKUN                  ‖
‖                                                ‖
==================================================\n''')
            print("\n(HELP : Tekan ctrl+c untuk menginput ulang nama dan password)")
            while True:
                # Input nama pengguna
                input_nama_pengguna = input('''
__________________________________________________\n
Masukkan nama pengguna : ''').strip()  # Hapus whitespace

                # Periksa apakah nama pengguna ada dalam data JSON
                for id_pengguna, akun_pengguna in data_pengguna.items():
                    if akun_pengguna['username'] == input_nama_pengguna:
                        # Jika ada, minta kata sandi
                        password = pwinput.pwinput("Masukkan kata sandi: ")
                        print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')

                        # Periksa apakah kata sandi sesuai
                        if akun_pengguna['password'] == password:
                            return akun_pengguna['username'], akun_pengguna['role']

                print("\nKesalahan: Pengguna/Password salah!\n")

                # Tanyakan apakah pengguna ingin mencoba lagi atau kembali ke menu utama
                while True:
                    print("1. Coba lagi")
                    print("2. Kembali ke menu utama")
                    pilihan = input("Pilih tindakan: ")
                    if pilihan == '1':
                        break  # Melanjutkan mencoba login lagi
                    elif pilihan == '2':
                        return None, None  # Kembali ke menu utama
                        print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
                    else:
                        print("\nPilihan tidak valid. Mohon memilih input yang benar.\n")
                        print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')

        except KeyboardInterrupt:
            print("\nLogin dibatalkan.")

##########################################################################################################################################

#-------------------------------------------#
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
#  _______________________________________  # 
# |Function untuk menu pelanggan dan admin| #
#  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
#-------------------------------------------# 

#-------------------------------#
# Function untuk melihat produk #
#-------------------------------#

def lihat_produk():
    # Mengurutkan produk berdasarkan ID sebelum menampilkannya
    mengurutkan_produk = sorted(data_produk, key=lambda x: x['id'])
    
    table = PrettyTable(['ID', 'Tiket Pesawat', 'Kelas Pesawat', 'Tujuan', 'Waktu', 'Harga'])
    for product in mengurutkan_produk:
        table.add_row([product['id'], product['tiket_pesawat'], product['kelas_pesawat'], product['tujuan'], product['waktu'], product['harga']])
    print(table)

#-------------------------------#
# Function untuk mencari produk #
#-------------------------------#

def cari_produk_berdasarkan_keyword(keyword):
    matching_products = []
    for product in data_produk:
        # Cek apakah kata kunci ada dalam informasi produk
        if (
            keyword.lower() in product['tiket_pesawat'].lower() or
            keyword.lower() in product['kelas_pesawat'].lower() or
            keyword.lower() in product['tujuan'].lower() or
            keyword.lower() in product['waktu'].lower() or
            keyword in str(product['harga'])
        ):
            matching_products.append(product)
    return matching_products




def tampilkan_hasil_pencarian(results):
    if not results:
        print("Tidak ada produk yang cocok dengan kata kunci ini.")
        print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
    else:
        print("Hasil Pencarian:")
        table = PrettyTable(['ID', 'Tiket Pesawat', 'Kelas Pesawat', 'Tujuan', 'Waktu', 'Harga'])
        for product in results:
            table.add_row([product['id'], product['tiket_pesawat'], product['kelas_pesawat'], product['tujuan'], product['waktu'], product['harga']])
        print(table)
        print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')



def cari_dan_tampilkan_produk():
    print('''\n
==================================================
‖                                                ‖
‖                   CARI PRODUK                  ‖
‖                                                ‖
==================================================''')
    print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
    keyword = input("Masukkan kata kunci untuk mencari produk (ID/Tiket Pesawat/Kelas Pesawat/Tujuan/Waktu/Harga): ")
    hasil_pencarian = cari_produk_berdasarkan_keyword(keyword)
    tampilkan_hasil_pencarian(hasil_pencarian)

##########################################################################################################################################

#-----------------------------#
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
#  _________________________  #
# |Function untuk menu admin| #
#  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
#-----------------------------# 

#-----------------------------------#
# 1. Function untuk menambah produk #
#-----------------------------------#

def tambah_produk():
    # Hitung ID terbaru berdasarkan jumlah produk yang ada
    if data_produk:
        id_terbaru = max(product['id'] for product in data_produk) + 1
    else:
        id_terbaru = 1
    print('''\n
==================================================
‖                                                ‖
‖                   TAMBAH PRODUK                ‖
‖                                                ‖
==================================================''')
    print("\n(HELP : Tekan ctrl+c untuk menginput ulang nama dan password)")
    print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
    tiket_pesawat = input("Masukkan Nama Tiket Pesawat: ")
    kelas_pesawat = input("Masukkan Kelas Pesawat: ")
    tujuan = input("Masukkan Tujuan: ")
    waktu = input("Masukkan Waktu: ")

    while True:
        harga_input = input("Masukkan Harga: ")
        if harga_input.isdigit():
            harga = float(harga_input)
            break
        else:
            print("Harga harus berupa angka.")
            print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')

    product = {
        'id': id_terbaru,  # Menggunakan ID terbaru yang dihitung
        'tiket_pesawat': tiket_pesawat,
        'kelas_pesawat': kelas_pesawat,
        'tujuan': tujuan,
        'waktu': waktu,
        'harga': harga
    }
    data_produk.append(product)
    save_data_to_json('dataproduk.json', data_produk)
    print("Produk berhasil ditambahkan.")
    print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')




#-----------------------------------#
# 2. Function untuk mengubah produk #
#-----------------------------------#

def ubah_produk(id_produk):
    try:
        id_produk = int(id_produk)  # Coba mengonversi ID produk menjadi bilangan bulat
        for product in data_produk:
            if product['id'] == id_produk:
                product['tiket_pesawat'] = input("Masukkan Nama Tiket Pesawat: ")
                product['kelas_pesawat'] = input("Masukkan Kelas Pesawat: ")
                product['tujuan'] = input("Masukkan Tujuan: ")
                product['waktu'] = input("Masukkan Waktu: ")

                # Input harga dengan pemeriksaan untuk memastikan itu angka
                while True:
                    harga_input = input("Masukkan Harga: ")
                    if harga_input.isdigit():
                        product['harga'] = float(harga_input)
                        save_data_to_json('dataproduk.json', data_produk)  # Perbarui file produk
                        print("Produk berhasil diperbarui.")
                        print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
                        return
                    else:
                        print("Harga harus berupa angka.")
                        print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        print("Produk tidak ditemukan.")
    except ValueError:
        print("ID produk harus berupa bilangan bulat.")
        print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')



#------------------------------------#
# 3. Function untuk menghapus produk #
#------------------------------------#

def hapus_produk(id_produk):
    try:
        id_produk = int(id_produk)  # Coba mengonversi ID produk menjadi bilangan bulat
        product_found = False  # Gunakan ini untuk menandai apakah produk ditemukan atau tidak
        for product in data_produk:
            if product['id'] == id_produk:
                data_produk.remove(product)
                product_found = True  # Produk ditemukan
                break  # Keluar dari loop setelah produk ditemukan

        if product_found:
            # Perbarui ID produk untuk setiap produk yang tersisa
            for index, remaining_product in enumerate(data_produk):
                remaining_product['id'] = index + 1

            save_data_to_json('dataproduk.json', data_produk)  # Simpan perubahan ID produk
            print("Produk berhasil dihapus dan ID produk diperbarui.")
            print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        else:
            print("Produk tidak ditemukan.")
    except ValueError:
        print("ID produk harus berupa bilangan bulat.")
        print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')



#-----------------------------------------#
# 4. Function untuk melihat akun pengguna #
#-----------------------------------------#

def info_akun_pengguna():
    print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
    print("\nDaftar Informasi Akun:\n")
    print("------------------")
    for id_pengguna, akun_pengguna in data_pengguna.items():
        print(f"ID: {id_pengguna}")
        print(f"Nama Pengguna: {akun_pengguna['username']}")
        print(f"Privilege: {akun_pengguna['role']}")
        print("------------------")
        print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')


#--------------------------------------#
# 5. Function untuk menghapus pengguna #
#--------------------------------------#

def hapus_data_pengguna(id_pengguna):
    global data_pengguna

    if id_pengguna in data_pengguna:
        akun_pengguna = data_pengguna[id_pengguna]
        if akun_pengguna['role'] == 'admin':
            print("Akun admin tidak dapat dihapus.")
            return

        username = akun_pengguna['username']
        del data_pengguna[id_pengguna]

        if username in data_invoice:
            del data_invoice[username]

        # Mengurutkan ulang id pengguna
        sorted_ids = sorted(data_pengguna.keys(), key=lambda x: int(x))

        # Membuat salinan data pengguna yang baru
        new_data_pengguna = {}
        new_id = 1
        for id_existing in sorted_ids:
            user_data = data_pengguna[id_existing]
            new_data_pengguna[str(new_id)] = user_data
            new_id += 1

        # Perbarui data_pengguna dengan yang sudah diperbarui
        data_pengguna = new_data_pengguna

        save_data_to_json('datapengguna.json', data_pengguna)
        save_data_to_json('datainvoice.json', data_invoice)
        print(f"Akun dengan ID {id_pengguna} berhasil dihapus.")
        print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
    else:
        print(f"Akun dengan ID {id_pengguna} tidak ditemukan.")
        print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')



#------------------------------#
# 6. Function untuk menu admin #
#------------------------------#

def menu_admin():
    while True:
        try:
            print('''\n
==================================================
‖                                                ‖
‖                   MENU ADMIN                   ‖
‖                                                ‖
==================================================''')
            print("\n(HELP : Tekan ctrl+c untuk kembali pada menu admin)")

            pilihan = (input('''
      _____________________________________
      |===>    Silahkan pilih opsi    <===|
      |                                   |
      |         1. Lihat Produk           |
      |         2. Tambah Produk          |   
      |         3. Perbarui Produk        |
      |         4. Hapus Produk           |
      |         5. Cari Produk            |
      |         --------------            |
      |         6. Lihat Akun Pengguna    |
      |         7. Hapus Akun Pengguna    |
      |         8. Keluar                 |
      |                                   |
      ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Tentukan opsi anda (1/2/3/4/5/6/7/8): '''))

            if pilihan == '1':
                lihat_produk()
            elif pilihan == '2':
                tambah_produk()
            elif pilihan == '3':
                lihat_produk()
                print('''\n
==================================================
‖                                                ‖
‖                 PERBARUI PRODUK                ‖
‖                                                ‖
==================================================''')
                print("\n(HELP : Tekan ctrl+c untuk menginput ulang nama dan password)")
                print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
                id_produk = (input("Masukkan ID produk yang ingin diperbarui: "))
                ubah_produk(id_produk)
            elif pilihan == '4':
                lihat_produk()
                print('''\n
==================================================
‖                                                ‖
‖                  HAPUS PRODUK                  ‖
‖                                                ‖
==================================================''')
                print("\n(HELP : Tekan ctrl+c untuk menginput ulang nama dan password)")
                print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
                id_produk = (input("Masukkan ID produk yang ingin dihapus: "))
                hapus_produk(id_produk)
            elif pilihan == '5':
                cari_dan_tampilkan_produk()
            elif pilihan == '6':
                info_akun_pengguna()
            elif pilihan == '7':
                info_akun_pengguna()
                id_pengguna = input("Masukkan ID akun yang ingin dihapus: ")
                hapus_data_pengguna(id_pengguna)
            elif pilihan == '8':
                break  # Keluar dari loop dan kembali ke menu utama
            else:
                print("Pilihan tidak valid.")
                print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        except KeyboardInterrupt:
            print("\nKembali pada menu admin.")
            print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')

##########################################################################################################################################

#---------------------------------#
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
#  _____________________________  #
# |Function untuk menu pelanggan| #
#  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
#---------------------------------# 

#----------------------------------#
# 1. Function untuk membeli produk #
#----------------------------------#

def kurangi_saldo(username, jumlah_pembelian):
    # Periksa apakah username (pengguna) ada dalam data_invoice
    if username in data_invoice:
        # Kurangi saldo pengguna
        data_invoice[username] -= jumlah_pembelian

        # Simpan kembali data yang telah diubah
        save_data_to_json('datainvoice.json', data_invoice)

        return True
    else:
        return False


def beli_produk(username):
    lihat_produk()
    print('''\n
==================================================
‖                                                ‖
‖                   BELI PRODUK                  ‖
‖                                                ‖
==================================================''')
    print("\n(HELP : Tekan ctrl+c untuk menginput ulang nama dan password)")
    print('''
__________________________________________________''')
    id_produk = input("\nMasukkan ID produk yang ingin dibeli atau ketik 'b' untuk membatalkan: ")

    if id_produk.lower() == 'b':
        print("Pembelian dibatalkan.")
        print('''
__________________________________________________''')
        return

    try:
        id_produk = int(id_produk)
        for product in data_produk:
            if product['id'] == id_produk:
                harga = product['harga']
                if username in data_invoice:
                    saldo_pengguna = data_invoice[username]
                    if saldo_pengguna >= harga:
                        if kurangi_saldo(username, harga):
                            nomor_invoice = str(random.randint(1000, 10000))
                            tanggal_pembelian = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            invoice = PrettyTable(['Nomor Invoice', 'Tiket Pesawat', 'Kelas Pesawat', 'Tujuan', 'Waktu', 'Harga', 'Tanggal Pembelian'])
                            invoice.add_row([nomor_invoice, product['tiket_pesawat'], product['kelas_pesawat'], product['tujuan'], product['waktu'], harga, tanggal_pembelian])
                            print("Pembelian berhasil.")
                            print("\nBerikut adalah invoice Anda:\n")
                            print(invoice)
                        else:
                            print("Pembelian gagal. Silakan coba lagi atau hubungi administrator.")
                    else:
                        print("Saldo tidak mencukupi untuk melakukan pembelian.")
                else:
                    print("Saldo tidak mencukupi untuk melakukan pembelian.")
                return  # Keluar dari fungsi jika pembelian berhasil atau gagal
        print("Produk tidak ditemukan.")
        print('''
__________________________________________________''')
    except ValueError:
        print("\nTerjadi kesalahan, silakan input ID produk yang ingin dibeli atau 'b' untuk membatalkan.")
        print('''
__________________________________________________''')




#--------------------------------#
# 2. Function untuk top up saldo #
#--------------------------------#

def top_up_saldo(username):
    while True:
        try:
            print('''\n
            ==================================================
            ‖                                                ‖
            ‖                   MENU TOP UP                  ‖
            ‖                                                ‖
            ==================================================''')
            print("\n(HELP : Tekan ctrl+c untuk menginput ulang nama dan password)")
            print('''
__________________________________________________''')
            while True:
                input_jumlah_saldo = input("\nMasukkan jumlah saldo yang ingin di-top up (minimal adalah kelipatan 50.000): ")
                if input_jumlah_saldo.isdigit():
                    jumlah = int(input_jumlah_saldo)
                    if jumlah > 0 and jumlah % 50000 == 0:  # Periksa apakah jumlahnya positif dan merupakan kelipatan 5.0000
                        if username in data_invoice:
                            if (data_invoice[username] + jumlah) <= 100000000:
                                data_invoice[username] += jumlah
                                save_data_to_json('datainvoice.json', data_invoice)
                                print(f"Saldo berhasil ditambahkan. Saldo Anda sekarang: {data_invoice[username]}")
                                print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
                                return
                            else:
                                print("Anda tidak dapat melakukan top-up saldo melebihi Rp. 100.000.000.")
                                print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
                        else:
                            if jumlah <= 100000000:
                                data_invoice[username] = jumlah
                                save_data_to_json('datainvoice.json', data_invoice)
                                print(f"Saldo berhasil ditambahkan. Saldo Anda sekarang: {data_invoice[username]}")
                                print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
                                return
                            else:
                                print("Anda tidak dapat top up saldo melebihi Rp. 100.000.000.")
                                print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
                    else:
                        print("\nJumlah saldo harus lebih besar dari 0 dan merupakan kelipatan RP.50.000.\n")
                        print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
                else:
                    print("\nMasukkan jumlah saldo yang valid (angka saja).")
                    print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        except ValueError:
            print("\nInput jumlah saldo tidak valid. Harap coba lagi.\n")
            print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            continue




#----------------------------------#
# 3. Function untuk menu pelanggan #
#----------------------------------#

def menu_pelanggan(username):
    while True:
        try:
            print('''\n
==================================================
‖                                                ‖
‖                  MENU PELANGGAN                ‖
‖                                                ‖
==================================================''')
            print("\n(HELP : Tekan ctrl+c untuk menginput ulang nama dan password)")
            print('''
        _________________________________
        |===>  Silahkan pilih opsi  <===|
        |                               |
        |         1. Lihat Produk       |
        |         2. Beli Produk        |   
        |         3. Top up saldo       |
        |         4. Cari Produk        |
        |         5. Keluar             |
        |                               |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            print(f"Saldo Anda saat ini: Rp.{data_invoice[username]}")
            print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
            pilihan = input("Pilih tindakan (1/2/3/4/5): ")
            print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')

            if pilihan == '1':
                lihat_produk()
            elif pilihan == '2':
                beli_produk(username)
            elif pilihan == '3':
                top_up_saldo(username)
            elif pilihan == '4':
                cari_dan_tampilkan_produk()
            elif pilihan == '5':
                break  # Keluar dari loop dan kembali ke menu utama
            else:
                print("Pilihan tidak valid. Mohon input yang sesuai")
        except KeyboardInterrupt:
            print("\nKembali pada menu pelanggan.")

##########################################################################################################################################

#-----------------------------------#
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
#  _______________________________  #
# |Koding yang mengatur menu utama| #
#  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾  #
# ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ #
#-----------------------------------# 


if __name__ == "__main__":
    while True:
        try:
            print('''
==================================================
‖                                                ‖
‖                SELAMAT DATANG DI               ‖
‖                   TRAVEL SI                    ‖
‖                                                ‖
==================================================''')
            pilihan = (input('''
        _________________________________
        |===>  Silahkan pilih opsi  <===|
        |                               |
        |      1. Registrasi Akun       |
        |      2. Login Akun            |
        |      3. Keluar                |
        |                               |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Tentukan opsi anda (1/2/3): '''))
            if pilihan == '1':
                print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
                create_account()
            elif pilihan == '2':
                username, role = login()
                if username:
                    print(f"\nLogin berhasil, selamat datang {username}!")
                    print('''
########################################''')

                    if role == 'admin':
                        menu_admin()
                    elif role == 'user':
                        menu_pelanggan(username)
                    else:
                        print("Privilege tidak valid.")
            elif pilihan == '3':
                print("Terima kasih telah menggunakan Aplikasi Tiket Pesawat. Selamat tinggal!")
                break
            else:
                print("\nPilihan tidak valid, silahkan input yang benar")
                print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
        except KeyboardInterrupt:
            print("\nPilihan tidak valid, silahkan input yang benar")
            print('''
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾''')
