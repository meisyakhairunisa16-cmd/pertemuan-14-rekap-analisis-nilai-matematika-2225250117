def tampilkan_hasil(statistik, ketuntasan):
    """Menampilkan hasil analisis nilai siswa."""
    print("\n=== HASIL ANALISIS NILAI ===")
    print(f"Rata-rata nilai : {statistik['rata_rata']:.2f}")
    print(f"Nilai minimum   : {statistik['minimum']}")
    print(f"Nilai maksimum  : {statistik['maksimum']}")
    print(f"Jumlah tuntas   : {ketuntasan['tuntas']}")
    print(f"Belum tuntas    : {ketuntasan['belum_tuntas']}")