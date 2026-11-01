from data_io import baca_data, simpan_laporan
from analisis import (
    validasi_nilai,
    hitung_statistik,
    hitung_ketuntasan
)
from utilitas import tampilkan_hasil


def main():
    print("PROGRAM REKAP DAN ANALISIS NILAI")
    print("================================")

    # Input lokasi file dan KKM
    path = "data/nilai_contoh.txt"

    try:
        kkm = float(input("Masukkan nilai KKM: "))

        if not validasi_nilai(kkm):
            print("Error: KKM harus berada pada rentang 0-100.")
            return

    except ValueError:
        print("Error: KKM harus berupa angka.")
        return

    # Membaca data nilai
    data = baca_data(path)

    if data is None:
        return

    # Memvalidasi nilai siswa
    data_valid = []

    for siswa in data:
        if validasi_nilai(siswa["nilai"]):
            data_valid.append(siswa)
        else:
            print(f"Nilai {siswa['nama']} tidak valid.")

    # Memeriksa data valid
    if not data_valid:
        print("Tidak ada data nilai yang valid.")
        return

    # Menghitung statistik dan ketuntasan
    statistik = hitung_statistik(data_valid)
    ketuntasan = hitung_ketuntasan(data_valid, kkm)

    # Menampilkan hasil
    tampilkan_hasil(statistik, ketuntasan)

    # Menyimpan laporan
    hasil = {
        **statistik,
        **ketuntasan
    }

    berhasil = simpan_laporan(
        hasil,
        "output/laporan.txt"
    )

    if berhasil:
        print("\nLaporan berhasil disimpan.")


if __name__ == "__main__":
    main()