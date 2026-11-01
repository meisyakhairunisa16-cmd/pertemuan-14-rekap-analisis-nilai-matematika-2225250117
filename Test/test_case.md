# Test Case Program Rekap Nilai

| ID | Kategori | Input | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90 | Rata-rata 80 |
| TC02 | Batas | Nilai 0 | Nilai valid |
| TC03 | Batas | Nilai 100 | Nilai valid |
| TC04 | Invalid | Nilai 105 | Nilai ditolak |
| TC05 | Invalid | File tidak ditemukan | Error ditangani |
| TC06 | Normal | Semua nilai >= KKM | Semua siswa tuntas |