# -Tugas-Studi-Kasus-6_Dimas-Surya-Pasyha_B_2609116044

## Biodata Mahasiswa
* **Nama** : Dimas Surya Pasyha
* **NIM** : 2609116044
* **Kelas** : B
* **Topik** : Studi Kasus 6 (Sistem Manajemen Inventaris Barang)

---

## Deskripsi Program
Jadi program ini adalah sistem yang bisa digunakan dalam manajemen barang, contohnya dalam suatu toko, perpustakaan, dan lain-lain. Namun sistem yang saya buat ini lebih cocok untuk manajemen inventaris barang di toko-toko. Lalu saya menggunakan 2 library yaitu os dan prettytable. Dalam program ini saya menggunakan json sebagai penyimpanan data dari sistem manajemen inventaris barang.

## Penjelasan Kode Program

**1.Pembuatan file json**

<img width="374" height="230" alt="image" src="https://github.com/user-attachments/assets/67ffdda7-f199-4a60-8905-df13f559a8c5" />

Penjelasan: kita buat data kosong dulu dengan memasukkan [] yang nantinya akan jadi penyimpanan data dari sistem main kita. Nama file "inventaris.json"

**2.Import library dan json**

<img width="404" height="165" alt="image" src="https://github.com/user-attachments/assets/34509fa1-e700-48a6-b882-b084efe756fe" />

Penjelasan: jadi saya menggunakan library os untuk melacak file dari json dan saya menggunakan library prettytable untuk pembuatan table pada data nantinya. Jangan lupa untuk membuat variable file_name dan memasukkan nama file json yang sudah dibuat tadi (inventaris.json) agar file python kita terhubung dengan file json. Lalu ada penggunaan try: return json.load(file)except json.JSONDecodeError: itu agar menghindari error atau crash.

**3.Fungsi muat_data**

<img width="400" height="74" alt="image" src="https://github.com/user-attachments/assets/b6a2fb3d-f328-4896-b2ee-a2bbc670c84c" />

Penjelasan: Kita buat function muat data untuk membaca data dan seperti yang saya bilang sebelumnya, saya menggunakan library os di bagian function muat data untuk mencari letak dari file json. Tanpa muat_data(), kamu harus menuliskan perintah open() dan json.load() secara berulang di setiap fungsi tersebut.

**4.Fungsi simpan_data**

<img width="326" height="38" alt="image" src="https://github.com/user-attachments/assets/724ba787-591b-4a2a-be02-442488386799" />

Penjelasan: Pembuatan function ini untuk nantinya buat menyimpan data ke file json secara permanen, dan penggunaan json.dump itu sebagai perintah untuk menyimpan data ke json.

**5. Fungsi tampilkan_data**

<img width="343" height="200" alt="image" src="https://github.com/user-attachments/assets/36497ce5-e68a-4bce-a107-af60b3ef9d36" />

Penjelasan: Nah disini saya buat fungsi untuk nantinya kita bisa melihat data dari file json kita dalam file mainnya. Terus seperti yang saya bilang, saya menggunakan library prettytable untuk membuat data saya memiliki tabel.

**6. Fungsi tambah_barang**

<img width="317" height="255" alt="image" src="https://github.com/user-attachments/assets/14ba8006-db9d-4051-9faf-b33580ffef22" />

Penjelasan: Kita masuk ke function tambah barang, saya bikin variable dari kode barang, nah untuk menghindari kode barang yang sama, saya buat jika memasukkan kode yang sama maka tidak akan diterima menggunakan "for". Lalu pembuatan variable nama untuk nama dari barang itu sendiri. Terus untuk pembuatan stok dan harga barang karena dua hal ini merupakan tipe data integer jadi kita pakai try except agar program tidak langsung crash saat kita memasukkan selain angka. Jangan lupa untuk tambah data kita menggunakan .append, lalu panggil function simpan_data () tadi agar data yang kita masukkan dapat tersimpan di file json.

**7. Perulangan utama/fungsi main**

<img width="289" height="226" alt="image" src="https://github.com/user-attachments/assets/09ff166c-38e7-48b4-82be-409c50f88ab5" />

Penjelasan: jadi disini kita buat while true sebagai menu utama kita dalam perulangan, nah dalam setiap logika if elif kita panggil setiap fungsi fungsi yang sudah kita buat sebelumnya, seperti untuk if pilihan 1, panggil function tampilkan_barang, dan lain-lain. Blok kode if __name__ == "__main__": adalah standar di Python untuk memastikan kode di dalamnya hanya berjalan ketika file script tersebut dieksekusi secara langsung, bukan saat diimport oleh file lain.

## Penjelasan Output

**1. Jika pilih 1 saat belum terdapat data**
<img width="260" height="91" alt="image" src="https://github.com/user-attachments/assets/2f1cd2cc-e097-4937-a06b-a94ca2c3ed6b" />

**2. Pilihan 2 menambahkan data**

<img width="251" height="272" alt="image" src="https://github.com/user-attachments/assets/84b04424-b6ed-4340-9818-2e69b321f8b3" />

**3. Pengecekan ulang pilihan 1 dan cek file json**

<img width="178" height="155" alt="image" src="https://github.com/user-attachments/assets/3b1a351e-dc3d-464e-b559-175cd94f4b02" />
<img width="143" height="146" alt="image" src="https://github.com/user-attachments/assets/9b127952-f47f-4e2c-a739-01c6e68a1e51" />

