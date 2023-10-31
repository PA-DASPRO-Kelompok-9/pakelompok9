## Identitas
Nama : Khalil Pradipta Lee\
NIM : 2309116046

Nama : Irene Mi'Raj Nur Sari\
NIM : 2309116015

Nama : Nova Nur Fauziah\
NIM : 23009116043

## Penjelasan
### Flow-chart


## Screenshot Input dan Output


### Penjelasan Output
# Pertama-tama, pengguna akan melihat tulisan selamat datang
```

========================================

Selamat datang di Aplikasi Tiket Pesawat

========================================

             1. Buat Akun
             2. Login
             3. Keluar

Silahkan pilih diantara opsi berikut (1/2/3):
```

# Selanjutnya jika memilih opsi 1 yaitu buat akun, maka akan diarahkan pada menu pembuatan akun
```
========================================

               Membuat Akun

========================================


(HELP : Tekan ctrl+c untuk membatalkan pembuatan akun)

1. User
2. Admin
Pilih role (user/admin):
```

# Selanjutnya kita akan membuat akun user/pelanggan biasa, input nama dan password seperti biasa, maka akun akan tersimpan pada database json
```
========================================

               Membuat Akun

========================================


(HELP : Tekan ctrl+c untuk membatalkan pembuatan akun)

1. User
2. Admin
Pilih role (user/admin): user

Masukkan nama pengguna: Tes
Masukkan kata sandi: 123
Akun pengguna berhasil dibuat.
```

# Ketika memilih role admin maka akan terdapat kode verifikasi sebelum membuat akun baru tersebut
```
========================================

               Membuat Akun

========================================


(HELP : Tekan ctrl+c untuk membatalkan pembuatan akun)

1. User
2. Admin
Pilih role (user/admin): admin 
Masukkan angka verifikasi untuk peran admin: *****

Masukkan nama pengguna: adminbaru
Masukkan kata sandi: 123
Akun pengguna berhasil dibuat.
```

# Selanjutnya kita mencoba login menggunakan akun pelanggan biasa tadi, berikut tampilan menunya
```
========================================

                Login Akun

========================================


(HELP : Tekan ctrl+c untuk menginput ulang nama dan password)


Masukkan nama pengguna: Tes
Masukkan kata sandi: ***

Login berhasil, selamat datang Tes!


========================================

              Menu Pelanggan:

========================================


(HELP : Tekan ctrl+c untuk menginput ulang nama dan password)

             1. Lihat Produk
             2. Beli Produk
             3. Top up saldo
             4. Cari Produk
             5. Keluar

Saldo Anda saat ini: Rp.0

Pilih tindakan (1/2/3/4):
```

# Berikut tampilan ketika melihat produk
```
Pilih tindakan (1/2/3/4): 1
+----+--------------------------+---------------+------------------------+-------+------------+
| ID |      Tiket Pesawat       | Kelas Pesawat |         Tujuan         | Waktu |   Harga    |
+----+--------------------------+---------------+------------------------+-------+------------+
| 1  |     Garuda Indonesia     |    Ekonomi    |  Samarinda - Jakarta   | 08:00 | 2800000.0  |
| 2  |         Air Asia         |    Ekonomi    | Jakarta - Kuala Lumpur | 12:15 | 2100000.0  |
| 3  |      Qatar Airways       |    Ekonomi    |     Jakarta - Doha     | 14:40 | 4200000.0  |
| 4  |      Delta Airlines      |    Ekonomi    |   Jakarta - New York   | 16:50 | 5600000.0  |
| 5  |      Japan Airlines      |    Ekonomi    |    Jakarta - Tokyo     | 11:10 | 4900000.0  |
| 6  |     Turkish Airlines     |    Ekonomi    |   Jakarta - Istanbul   | 13:30 | 3500000.0  |
| 7  |         Lion Air         |    Ekonomi    |    Bali - Surabaya     | 07:30 |  700000.0  |
| 8  |    Malaysia Airlines     |    Ekonomi    | Kuala Lumpur - Manila  | 13:50 | 2520000.0  |
| 9  |    America Airlines      |    Ekonomi    | New York - Los Angeles | 10:00 | 4200000.0  |
| 10 |         Aeroflot         |    Ekonomi    |     Moscow - Paris     | 14:55 | 5600000.0  |
| 11 |    Singapore Airlines    |     Bisnis    |  Jakarta - Singapura   | 10:30 |  700000.0  |
| 12 |        Lufthansa         |     Bisnis    |  Jakarta - Frankfurt   | 19:20 | 11200000.0 |
| 13 |     British Airways      |     Bisnis    |    Jakarta - London    | 21:45 | 12600000.0 |
| 14 |      Cathay Pacific      |     Bisnis    |   Hong Kong - Sydney   | 09:20 | 9800000.0  |
| 15 | KLM Royal Dutch Airlines |     Bisnis    |  Amsterdam - New York  | 17:40 | 10500000.0 |
| 16 |         Emirates         |  First Class  |    Jakarta - Dubai     | 15:45 | 16800000.0 |
+----+--------------------------+---------------+------------------------+-------+------------+
```

# Berikut tampilan ketika membeli produk
```
Pilih tindakan (1/2/3/4): 2
+----+--------------------------+---------------+------------------------+-------+------------+
| ID |      Tiket Pesawat       | Kelas Pesawat |         Tujuan         | Waktu |   Harga    |
+----+--------------------------+---------------+------------------------+-------+------------+
| 1  |     Garuda Indonesia     |    Ekonomi    |  Samarinda - Jakarta   | 08:00 | 2800000.0  |
| 2  |         Air Asia         |    Ekonomi    | Jakarta - Kuala Lumpur | 12:15 | 2100000.0  |
| 3  |      Qatar Airways       |    Ekonomi    |     Jakarta - Doha     | 14:40 | 4200000.0  |
| 4  |      Delta Airlines      |    Ekonomi    |   Jakarta - New York   | 16:50 | 5600000.0  |
| 5  |      Japan Airlines      |    Ekonomi    |    Jakarta - Tokyo     | 11:10 | 4900000.0  |
| 6  |     Turkish Airlines     |    Ekonomi    |   Jakarta - Istanbul   | 13:30 | 3500000.0  |
| 7  |         Lion Air         |    Ekonomi    |    Bali - Surabaya     | 07:30 |  700000.0  |
| 8  |    Malaysia Airlines     |    Ekonomi    | Kuala Lumpur - Manila  | 13:50 | 2520000.0  |
| 9  |    America Airlines      |    Ekonomi    | New York - Los Angeles | 10:00 | 4200000.0  |
| 10 |         Aeroflot         |    Ekonomi    |     Moscow - Paris     | 14:55 | 5600000.0  |
| 11 |    Singapore Airlines    |     Bisnis    |  Jakarta - Singapura   | 10:30 |  700000.0  |
| 12 |        Lufthansa         |     Bisnis    |  Jakarta - Frankfurt   | 19:20 | 11200000.0 |
| 13 |     British Airways      |     Bisnis    |    Jakarta - London    | 21:45 | 12600000.0 |
| 14 |      Cathay Pacific      |     Bisnis    |   Hong Kong - Sydney   | 09:20 | 9800000.0  |
| 15 | KLM Royal Dutch Airlines |     Bisnis    |  Amsterdam - New York  | 17:40 | 10500000.0 |
| 16 |         Emirates         |  First Class  |    Jakarta - Dubai     | 15:45 | 16800000.0 |
+----+--------------------------+---------------+------------------------+-------+------------+
Masukkan ID produk yang ingin dibeli atau ketik 'b' untuk membatalkan:
```

# Berikut tampilan pada menu top up
```
Pilih tindakan (1/2/3/4): 3
========================================

                Menu Top Up

========================================

Masukkan jumlah saldo yang ingin di-top up (minimal adalah kelipatan 50.000):
```

# Berikut tampilan pada cari produk, pada situasi ini saya mencoba menulis keyword ekonomi
```
Pilih tindakan (1/2/3/4): 4
Masukkan kata kunci untuk mencari produk (ID/Tiket Pesawat/Kelas Pesawat/Tujuan/Waktu/Harga): Ekonomi
Hasil Pencarian:
+----+-------------------+---------------+------------------------+-------+-----------+
| ID |   Tiket Pesawat   | Kelas Pesawat |         Tujuan         | Waktu |   Harga   |
+----+-------------------+---------------+------------------------+-------+-----------+
| 1  |  Garuda Indonesia |    Ekonomi    |  Samarinda - Jakarta   | 08:00 | 2800000.0 |
| 2  |      Air Asia     |    Ekonomi    | Jakarta - Kuala Lumpur | 12:15 | 2100000.0 |
| 3  |   Qatar Airways   |    Ekonomi    |     Jakarta - Doha     | 14:40 | 4200000.0 |
| 4  |   Delta Airlines  |    Ekonomi    |   Jakarta - New York   | 16:50 | 5600000.0 |
| 5  |   Japan Airlines  |    Ekonomi    |    Jakarta - Tokyo     | 11:10 | 4900000.0 |
| 6  |  Turkish Airlines |    Ekonomi    |   Jakarta - Istanbul   | 13:30 | 3500000.0 |
| 7  |      Lion Air     |    Ekonomi    |    Bali - Surabaya     | 07:30 |  700000.0 |
| 8  | Malaysia Airlines |    Ekonomi    | Kuala Lumpur - Manila  | 13:50 | 2520000.0 |
| 9  | America Airlines  |    Ekonomi    | New York - Los Angeles | 10:00 | 4200000.0 |
| 10 |      Aeroflot     |    Ekonomi    |     Moscow - Paris     | 14:55 | 5600000.0 |
+----+-------------------+---------------+------------------------+-------+-----------+
```

# Sekarang kita mencoba login dengan akun admin, begini tampilannya
```
========================================

                Login Akun

========================================


(HELP : Tekan ctrl+c untuk menginput ulang nama dan password)


Masukkan nama pengguna: adminbaru
Masukkan kata sandi: ***

Login berhasil, selamat datang adminbaru!


========================================

               Menu Admin:

========================================


(HELP : Tekan ctrl+c untuk kembali pada menu admin)

         1. Lihat Produk
         2. Tambah Produk
         3. Perbarui Produk
         4. Hapus Produk
         5. Cari Produk
         -----------------
         6. Lihat Akun Pengguna
         7. Hapus Akun Pelanggan
         8. Keluar

Pilih tindakan (1/2/3/4/5/6/7):
```

# Kita mencoba menu tambah produk, begini tampilannya. Pada situasi ini saya menggunakan 'tes' saja
```
========================================

               Menu Admin:

========================================


(HELP : Tekan ctrl+c untuk kembali pada menu admin)

         1. Lihat Produk
         2. Tambah Produk
         3. Perbarui Produk
         4. Hapus Produk
         5. Cari Produk
         -----------------
         6. Lihat Akun Pengguna
         7. Hapus Akun Pelanggan
         8. Keluar

Pilih tindakan (1/2/3/4/5/6/7): 2
Masukkan Nama Tiket Pesawat: Tes
Masukkan Kelas Pesawat: Tes
Masukkan Tujuan: Tes
Masukkan Waktu: Tes
Masukkan Harga: 100
Produk berhasil ditambahkan
```

# Sekarang kita mencoba memperbarui produk, pada situasi ini saya mengganti 'tes' dengan 'tesbaru'. Berikut tampilannya
```
Pilih tindakan (1/2/3/4/5/6/7): 3
+----+--------------------------+---------------+------------------------+-------+------------+
| ID |      Tiket Pesawat       | Kelas Pesawat |         Tujuan         | Waktu |   Harga    |
+----+--------------------------+---------------+------------------------+-------+------------+
| 1  |     Garuda Indonesia     |    Ekonomi    |  Samarinda - Jakarta   | 08:00 | 2800000.0  |
| 2  |         Air Asia         |    Ekonomi    | Jakarta - Kuala Lumpur | 12:15 | 2100000.0  |
| 3  |      Qatar Airways       |    Ekonomi    |     Jakarta - Doha     | 14:40 | 4200000.0  |
| 4  |      Delta Airlines      |    Ekonomi    |   Jakarta - New York   | 16:50 | 5600000.0  |
| 5  |      Japan Airlines      |    Ekonomi    |    Jakarta - Tokyo     | 11:10 | 4900000.0  |
| 6  |     Turkish Airlines     |    Ekonomi    |   Jakarta - Istanbul   | 13:30 | 3500000.0  |
| 7  |         Lion Air         |    Ekonomi    |    Bali - Surabaya     | 07:30 |  700000.0  |
| 8  |    Malaysia Airlines     |    Ekonomi    | Kuala Lumpur - Manila  | 13:50 | 2520000.0  |
| 9  |    America Airlines      |    Ekonomi    | New York - Los Angeles | 10:00 | 4200000.0  |
| 10 |         Aeroflot         |    Ekonomi    |     Moscow - Paris     | 14:55 | 5600000.0  |
| 11 |    Singapore Airlines    |     Bisnis    |  Jakarta - Singapura   | 10:30 |  700000.0  |
| 12 |        Lufthansa         |     Bisnis    |  Jakarta - Frankfurt   | 19:20 | 11200000.0 |
| 13 |     British Airways      |     Bisnis    |    Jakarta - London    | 21:45 | 12600000.0 |
| 14 |      Cathay Pacific      |     Bisnis    |   Hong Kong - Sydney   | 09:20 | 9800000.0  |
| 15 | KLM Royal Dutch Airlines |     Bisnis    |  Amsterdam - New York  | 17:40 | 10500000.0 |
| 16 |         Emirates         |  First Class  |    Jakarta - Dubai     | 15:45 | 16800000.0 |
| 17 |           Tes            |      Tes      |          Tes           |  Tes  |   100.0    |
+----+--------------------------+---------------+------------------------+-------+------------+
Masukkan ID produk yang ingin diperbarui: 17
Masukkan Nama Tiket Pesawat: tesbaru
Masukkan Kelas Pesawat: tesbaru
Masukkan Tujuan: tesbaru
Masukkan Waktu: tesbaru
Masukkan Harga: 200
Produk berhasil diperbarui.

========================================

               Menu Admin:

========================================


(HELP : Tekan ctrl+c untuk kembali pada menu admin)

         1. Lihat Produk
         2. Tambah Produk
         3. Perbarui Produk
         4. Hapus Produk
         5. Cari Produk
         -----------------
         6. Lihat Akun Pengguna
         7. Hapus Akun Pelanggan
         8. Keluar

Pilih tindakan (1/2/3/4/5/6/7): 1
+----+--------------------------+---------------+------------------------+---------+------------+        
| ID |      Tiket Pesawat       | Kelas Pesawat |         Tujuan         |  Waktu  |   Harga    |        
+----+--------------------------+---------------+------------------------+---------+------------+        
| 1  |     Garuda Indonesia     |    Ekonomi    |  Samarinda - Jakarta   |  08:00  | 2800000.0  |        
| 2  |         Air Asia         |    Ekonomi    | Jakarta - Kuala Lumpur |  12:15  | 2100000.0  |        
| 3  |      Qatar Airways       |    Ekonomi    |     Jakarta - Doha     |  14:40  | 4200000.0  |        
| 4  |      Delta Airlines      |    Ekonomi    |   Jakarta - New York   |  16:50  | 5600000.0  |        
| 5  |      Japan Airlines      |    Ekonomi    |    Jakarta - Tokyo     |  11:10  | 4900000.0  |        
| 6  |     Turkish Airlines     |    Ekonomi    |   Jakarta - Istanbul   |  13:30  | 3500000.0  |        
| 7  |         Lion Air         |    Ekonomi    |    Bali - Surabaya     |  07:30  |  700000.0  |        
| 8  |    Malaysia Airlines     |    Ekonomi    | Kuala Lumpur - Manila  |  13:50  | 2520000.0  |        
| 9  |    America Airlines      |    Ekonomi    | New York - Los Angeles |  10:00  | 4200000.0  |        
| 10 |         Aeroflot         |    Ekonomi    |     Moscow - Paris     |  14:55  | 5600000.0  |        
| 11 |    Singapore Airlines    |     Bisnis    |  Jakarta - Singapura   |  10:30  |  700000.0  |        
| 12 |        Lufthansa         |     Bisnis    |  Jakarta - Frankfurt   |  19:20  | 11200000.0 |        
| 13 |     British Airways      |     Bisnis    |    Jakarta - London    |  21:45  | 12600000.0 |        
| 14 |      Cathay Pacific      |     Bisnis    |   Hong Kong - Sydney   |  09:20  | 9800000.0  |        
| 15 | KLM Royal Dutch Airlines |     Bisnis    |  Amsterdam - New York  |  17:40  | 10500000.0 |        
| 16 |         Emirates         |  First Class  |    Jakarta - Dubai     |  15:45  | 16800000.0 |        
| 17 |         tesbaru          |    tesbaru    |        tesbaru         | tesbaru |   200.0    |        
+----+--------------------------+---------------+------------------------+---------+------------+
```

# Sekarang kita mencoba menghapus produk, di situasi ini saya menghapus id 17 yaitu 'tesbaru'. Berikut tampilannya
```
Pilih tindakan (1/2/3/4/5/6/7): 4
+----+--------------------------+---------------+------------------------+---------+------------+        
| ID |      Tiket Pesawat       | Kelas Pesawat |         Tujuan         |  Waktu  |   Harga    |        
+----+--------------------------+---------------+------------------------+---------+------------+        
| 1  |     Garuda Indonesia     |    Ekonomi    |  Samarinda - Jakarta   |  08:00  | 2800000.0  |        
| 2  |         Air Asia         |    Ekonomi    | Jakarta - Kuala Lumpur |  12:15  | 2100000.0  |        
| 3  |      Qatar Airways       |    Ekonomi    |     Jakarta - Doha     |  14:40  | 4200000.0  |        
| 4  |      Delta Airlines      |    Ekonomi    |   Jakarta - New York   |  16:50  | 5600000.0  |        
| 5  |      Japan Airlines      |    Ekonomi    |    Jakarta - Tokyo     |  11:10  | 4900000.0  |        
| 6  |     Turkish Airlines     |    Ekonomi    |   Jakarta - Istanbul   |  13:30  | 3500000.0  |        
| 7  |         Lion Air         |    Ekonomi    |    Bali - Surabaya     |  07:30  |  700000.0  |        
| 8  |    Malaysia Airlines     |    Ekonomi    | Kuala Lumpur - Manila  |  13:50  | 2520000.0  |        
| 9  |    America Airlines      |    Ekonomi    | New York - Los Angeles |  10:00  | 4200000.0  |        
| 10 |         Aeroflot         |    Ekonomi    |     Moscow - Paris     |  14:55  | 5600000.0  |        
| 11 |    Singapore Airlines    |     Bisnis    |  Jakarta - Singapura   |  10:30  |  700000.0  |        
| 12 |        Lufthansa         |     Bisnis    |  Jakarta - Frankfurt   |  19:20  | 11200000.0 |        
| 13 |     British Airways      |     Bisnis    |    Jakarta - London    |  21:45  | 12600000.0 |        
| 14 |      Cathay Pacific      |     Bisnis    |   Hong Kong - Sydney   |  09:20  | 9800000.0  |        
| 15 | KLM Royal Dutch Airlines |     Bisnis    |  Amsterdam - New York  |  17:40  | 10500000.0 |        
| 16 |         Emirates         |  First Class  |    Jakarta - Dubai     |  15:45  | 16800000.0 |        
| 17 |         tesbaru          |    tesbaru    |        tesbaru         | tesbaru |   200.0    |        
+----+--------------------------+---------------+------------------------+---------+------------+        
Masukkan ID produk yang ingin dihapus: 17
Produk berhasil dihapus dan ID produk diperbarui.

========================================

               Menu Admin:

========================================


(HELP : Tekan ctrl+c untuk kembali pada menu admin)

         1. Lihat Produk
         2. Tambah Produk
         3. Perbarui Produk
         4. Hapus Produk
         5. Cari Produk
         -----------------
         6. Lihat Akun Pengguna
         7. Hapus Akun Pelanggan
         8. Keluar

Pilih tindakan (1/2/3/4/5/6/7): 1
+----+--------------------------+---------------+------------------------+-------+------------+
| ID |      Tiket Pesawat       | Kelas Pesawat |         Tujuan         | Waktu |   Harga    |
+----+--------------------------+---------------+------------------------+-------+------------+
| 1  |     Garuda Indonesia     |    Ekonomi    |  Samarinda - Jakarta   | 08:00 | 2800000.0  |
| 2  |         Air Asia         |    Ekonomi    | Jakarta - Kuala Lumpur | 12:15 | 2100000.0  |
| 3  |      Qatar Airways       |    Ekonomi    |     Jakarta - Doha     | 14:40 | 4200000.0  |
| 4  |      Delta Airlines      |    Ekonomi    |   Jakarta - New York   | 16:50 | 5600000.0  |
| 5  |      Japan Airlines      |    Ekonomi    |    Jakarta - Tokyo     | 11:10 | 4900000.0  |
| 6  |     Turkish Airlines     |    Ekonomi    |   Jakarta - Istanbul   | 13:30 | 3500000.0  |
| 7  |         Lion Air         |    Ekonomi    |    Bali - Surabaya     | 07:30 |  700000.0  |
| 8  |    Malaysia Airlines     |    Ekonomi    | Kuala Lumpur - Manila  | 13:50 | 2520000.0  |
| 9  |    America Airlines      |    Ekonomi    | New York - Los Angeles | 10:00 | 4200000.0  |
| 10 |         Aeroflot         |    Ekonomi    |     Moscow - Paris     | 14:55 | 5600000.0  |
| 11 |    Singapore Airlines    |     Bisnis    |  Jakarta - Singapura   | 10:30 |  700000.0  |
| 12 |        Lufthansa         |     Bisnis    |  Jakarta - Frankfurt   | 19:20 | 11200000.0 |
| 13 |     British Airways      |     Bisnis    |    Jakarta - London    | 21:45 | 12600000.0 |
| 14 |      Cathay Pacific      |     Bisnis    |   Hong Kong - Sydney   | 09:20 | 9800000.0  |
| 15 | KLM Royal Dutch Airlines |     Bisnis    |  Amsterdam - New York  | 17:40 | 10500000.0 |
| 16 |         Emirates         |  First Class  |    Jakarta - Dubai     | 15:45 | 16800000.0 |
+----+--------------------------+---------------+------------------------+-------+------------+
```

# Fitur cari produk dan lihat produk sama dengan pengguna

# Sekarang kita akan melihat akun pengguna yang ada di database program. Berikut tampilannya
```
Pilih tindakan (1/2/3/4/5/6/7): 6

Daftar Informasi Akun:

------------------
ID: 1
Nama Pengguna: khalil
Privilege: admin
------------------
ID: 2
Nama Pengguna: hisyam
Privilege: admin
------------------
ID: 3
Nama Pengguna: nova
Privilege: user
------------------
ID: 4
Nama Pengguna: Tes
Privilege: user
------------------
ID: 5
Nama Pengguna: adminbaru
Privilege: admin
------------------
```

# Sekarang kita mencoba menghapus akun, pada situasi ini saya mencoba menghapus akun dengan id 4, (sedikit ctt, bahwa akun admin tidak dapat dihapus kecuali dihapus pada database itu sendiri)
```
Pilih tindakan (1/2/3/4/5/6/7): 7

Daftar Informasi Akun:

------------------
ID: 1
Nama Pengguna: khalil
Privilege: admin
------------------
ID: 2
Nama Pengguna: hisyam
Privilege: admin
------------------
ID: 3
Nama Pengguna: nova
Privilege: user
------------------
ID: 4
Nama Pengguna: Tes
Privilege: user
------------------
ID: 5
Nama Pengguna: adminbaru
Privilege: admin
------------------
Masukkan ID akun yang ingin dihapus: 4
Akun dengan ID 4 berhasil dihapus.

========================================

               Menu Admin:

========================================


(HELP : Tekan ctrl+c untuk kembali pada menu admin)

         1. Lihat Produk
         2. Tambah Produk
         3. Perbarui Produk
         4. Hapus Produk
         5. Cari Produk
         -----------------
         6. Lihat Akun Pengguna
         7. Hapus Akun Pelanggan
         8. Keluar

Pilih tindakan (1/2/3/4/5/6/7): 6

Daftar Informasi Akun:

------------------
ID: 1
Nama Pengguna: khalil
Privilege: admin
------------------
ID: 2
Nama Pengguna: hisyam
Privilege: admin
------------------
ID: 3
Nama Pengguna: nova
Privilege: user
------------------
ID: 4
Nama Pengguna: adminbaru
Privilege: admin
------------------
```

# Yang terakhir adalah keluar pada program yaitu pilihan 8, kita akan kembali pada menu utama lagi
```
Pilih tindakan (1/2/3/4/5/6/7): 8

========================================

Selamat datang di Aplikasi Tiket Pesawat

========================================

             1. Buat Akun
             2. Login
             3. Keluar

Silahkan pilih diantara opsi berikut (1/2/3):
```

# Kita mencoba input 3 dan program akan berakhir
```
========================================

Selamat datang di Aplikasi Tiket Pesawat

========================================

             1. Buat Akun
             2. Login
             3. Keluar

Silahkan pilih diantara opsi berikut (1/2/3): 3
Terima kasih telah menggunakan Aplikasi Tiket Pesawat. Selamat tinggal!
```
