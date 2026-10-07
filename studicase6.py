import json
import os
from prettytable import PrettyTable

FILE_NAME = "inventaris.json"


def muat_data():
    if not os.path.exists(FILE_NAME):
        print(
            f"Error: File '{FILE_NAME}' tidak ditemukan! Silakan buat file tersebut terlebih dahulu."
        )
        return []

    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            print(
                f"Error: Format file '{FILE_NAME}' tidak valid/kosong. Pastikan berisi minimal '[]'."
            )
            return []


def simpan_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def tampilkan_barang():
    """Fitur membaca dan menampilkan seluruh data barang menggunakan PrettyTable."""
    data = muat_data()
    print("\n=== DAFTAR INVENTARIS BARANG ===")

    if not data:
        print("Stok barang masih kosong atau file belum terbaca dengan benar.")
        return

    # Inisialisasi PrettyTable dengan nama kolom
    tabel = PrettyTable()
    tabel.field_names = ["Kode", "Nama Barang", "Stok", "Harga"]

    # Menambahkan data ke tabel
    for item in data:
        tabel.add_row(
            [item["kode"], item["nama"], item["stok"], f"Rp{item['harga']}"]
        )

    print(tabel)


def tambah_barang():
    data = muat_data()
    print("\n=== TAMBAH BARANG BARU ===")

    kode = input("Masukkan Kode Barang  : ")
    # Cek apakah kode barang sudah ada
    for item in data:
        if item["kode"].lower() == kode:
            print("Gagal: Kode barang sudah terdaftar!")
            return

    nama = input("Masukkan Nama Barang  : ")

    try:
        stok = int(input("Masukkan Jumlah Stok : "))
        harga = int(input("Masukkan Harga (Rp)  : "))
    except ValueError:
        print("Gagal: Stok dan Harga harus berupa angka!")
        return

    barang_baru = {"kode": kode, "nama": nama, "stok": stok, "harga": harga}

    data.append(barang_baru)
    simpan_data(data)
    print(f"Berhasil: Barang '{nama}' telah ditambahkan secara permanen!")


def main():
    while True:
        print("\n=== SISTEM MANAJEMEN INVENTARIS ===")
        print("1. Lihat Semua Barang")
        print("2. Tambah Barang Baru")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            tampilkan_barang()
        elif pilihan == "2":
            tambah_barang()
        elif pilihan == "3":
            print("\nTerima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()