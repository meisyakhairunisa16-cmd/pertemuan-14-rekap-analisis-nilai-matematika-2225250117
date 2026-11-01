def validasi_nilai(nilai):
    """Memeriksa apakah nilai berada dalam rentang 0-100."""
    return 0 <= nilai <= 100


def hitung_statistik(data):
    """Menghitung rata-rata, nilai minimum, dan maksimum."""
    nilai_siswa = [siswa["nilai"] for siswa in data]

    statistik = {
        "rata_rata": sum(nilai_siswa) / len(nilai_siswa),
        "minimum": min(nilai_siswa),
        "maksimum": max(nilai_siswa)
    }

    return statistik


def tentukan_status(nilai, kkm):
    """Menentukan status ketuntasan siswa."""
    if nilai >= kkm:
        return "Tuntas"
    else:
        return "Belum Tuntas"


def hitung_ketuntasan(data, kkm):
    """Menghitung jumlah siswa tuntas dan belum tuntas."""
    jumlah_tuntas = 0
    jumlah_belum_tuntas = 0

    for siswa in data:
        status = tentukan_status(siswa["nilai"], kkm)

        if status == "Tuntas":
            jumlah_tuntas += 1
        else:
            jumlah_belum_tuntas += 1

    return {
        "tuntas": jumlah_tuntas,
        "belum_tuntas": jumlah_belum_tuntas
    }