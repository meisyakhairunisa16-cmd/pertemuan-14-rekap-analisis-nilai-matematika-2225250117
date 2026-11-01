def baca_data(path):
    """Membaca data siswa dari file teks."""
    data = []

    try:
        with open(path, "r") as file:
            for baris in file:
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    nama, nilai = baris.split(",")
                    data.append({
                        "nama": nama.strip(),
                        "nilai": float(nilai)
                    })

                except ValueError:
                    print(f"Data tidak valid: {baris}")

    except FileNotFoundError:
        print("Error: File data tidak ditemukan.")
        return None

    return data


def simpan_laporan(hasil, path):
    """Menyimpan hasil analisis ke file teks."""
    try:
        with open(path, "w") as file:
            file.write("LAPORAN ANALISIS NILAI MATEMATIKA\n")
            file.write("================================\n")
            file.write(f"Rata-rata nilai : {hasil['rata_rata']:.2f}\n")
            file.write(f"Nilai minimum   : {hasil['minimum']}\n")
            file.write(f"Nilai maksimum  : {hasil['maksimum']}\n")
            file.write(f"Jumlah tuntas   : {hasil['tuntas']}\n")
            file.write(f"Belum tuntas    : {hasil['belum_tuntas']}\n")

        return True

    except OSError:
        print("Error: Laporan gagal disimpan.")
        return False