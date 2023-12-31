## Identitas
Nama : Khalil Pradipta Lee\
NIM : 2309116046

Nama : Irene Mi'Raj Nur Sari\
NIM : 2309116015

Nama : Nova Nur Fauziah\
NIM : 23009116043

## Penjelasan
### Flow-chart
![FLOWCHART](https://github.com/PA-DASPRO-Kelompok-9/pakelompok9/assets/144671469/5ae8bdc2-8d3a-4ba1-b103-d22650f2ac44)













## Screenshot Input dan Output


# Penjelasan Output

## 1. Tampilan awal
```
==================================================
‖                                                ‖
‖                SELAMAT DATANG DI               ‖
‖                   TRAVEL SI                    ‖
‖                                                ‖
==================================================

        _________________________________
        |===>  Silahkan pilih opsi  <===|
        |                               |
        |      1. Registrasi Akun       |
        |      2. Login Akun            |
        |      3. Keluar                |
        |                               |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Tentukan opsi anda (1/2/3):
```

## 2. Tampilan registrasi akun 
```
==================================================
‖                                                ‖
‖                  MEMBUAT AKUN                  ‖
‖                                                ‖
==================================================

(HELP : Tekan ctrl+c untuk membatalkan pembuatan akun)

        _________________________________
        |===>  Silahkan pilih role  <===|
        |                               |
        |            -USER              |
        |            -ADMIN             |
        |                               |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Tentukan opsi anda (user/admin): user

__________________________________________________

Masukkan nama pengguna: tes
Masukkan kata sandi: 123
Akun pengguna berhasil dibuat.

‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
```

## 3. Tampilan login 
```
==================================================
‖                                                ‖
‖                    LOGIN AKUN                  ‖
‖                                                ‖
==================================================


(HELP : Tekan ctrl+c untuk menginput ulang nama dan password)

__________________________________________________

Masukkan nama pengguna : tes 
Masukkan kata sandi: ***

‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

Login berhasil, selamat datang tes!

########################################
```

## 4. Tampilan menu pelanggan
```
==================================================
‖                                                ‖
‖                  MENU PELANGGAN                ‖
‖                                                ‖
==================================================

(HELP : Tekan ctrl+c untuk menginput ulang nama dan password)

        _________________________________
        |===>  Silahkan pilih opsi  <===|
        |                               |
        |         1. Lihat Produk       |
        |         2. Beli Produk        |
        |         3. Top up saldo       |
        |         4. Cari Produk        |
        |         5. Keluar             |
        |                               |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Saldo Anda saat ini: Rp.0

‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
Pilih tindakan (1/2/3/4/5):
```

## Tampilan menu admin
```
==================================================
‖                                                ‖
‖                   MENU ADMIN                   ‖
‖                                                ‖
==================================================

(HELP : Tekan ctrl+c untuk kembali pada menu admin)

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
Tentukan opsi anda (1/2/3/4/5/6/7/8):
```

# ----------------------------------------------------------

# Penjelasan Function

## 1. load_data_from_json(file_name):
untuk load data json

## 2. generate_invoice_number():
untuk membuat angka random pada id invoice saat membeli produk

## 3. hitung_id_berikutnya():
untuk menghitung id berikutnya pada datapengguna.json

## 4. create_account():
untuk membuat akun

## 5. login(): 
untuk login akun

# ----------------------------------------------------------

## 6. lihat_produk():
untuk melihat produk pada menu pelanggan maupun admin (read)

## 7. cari_produk_berdasarkan_keyword(keyword):
untuk mencari produk berdasarkan keyword yang kita berikan

## 8. tampilkan_hasil_pencarian(results):
untuk menampilkan hasil pencarian berdasarkan keyword yang kita berikut

## 9. cari_dan_tampilkan_produk():
fungsi tempat kita menginput keyword untuk mencari produk

# ----------------------------------------------------------

## 10. Tambah Produk():
untuk membuat produk baru (create)

## 11. ubah_produk():
untuk mengubah produk (edit) yang sudah ada

## 12. hapus_produk(id_produk):
untuk menghapus produk yang sudah ada

## 13. info_akun_pengguna():
untuk melihat informasi semua pengguna pada datapengguna.json

## 14. hapus_data_pengguna(id_pengguna):
untuk menghapus data pengguna (pelanggan), akun admin tidak dapat dihapus

## 15. menu_admin:
untuk memuat menu admin yang berisi fungsi-fungsi diatas

# ----------------------------------------------------------

## 16. kurangi_saldo(username, jumlah_pembelian):
untuk mengurangi saldo pembeli saat melakukan pembelian

## 17. beli_produk(username):
untuk membeli produk berdasarkan produk yang sudah ada

## 18. top_up_saldo(username):
untuk mengisi saldo pelanggan

## 19. menu_pelanggan(username):
untuk memuat menu pelanggan yang berisi fungsi-fungsi diatas

