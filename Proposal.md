# PROPOSAL PROYEK PROGRAM SEDERHANA
## PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA KELAS

### 1. Judul Proyek
Program Rekap dan Analisis Nilai Matematika Kelas

### 2. Latar Belakang
Pengolahan nilai siswa merupakan salah satu kegiatan yang dilakukan oleh guru matematika. Pengolahan nilai secara manual membutuhkan waktu dan berisiko menimbulkan kesalahan dalam perhitungan.

Oleh karena itu, diperlukan program sederhana yang dapat membantu guru mengolah nilai siswa secara otomatis. Program ini dirancang menggunakan bahasa Python untuk membaca data nilai, menghitung statistik, menentukan ketuntasan, dan menyimpan laporan hasil analisis.

### 3. Pengguna dan Tujuan

**Pengguna:** Guru matematika.

**Tujuan:** Membantu guru mengolah data nilai siswa secara lebih cepat, tepat, dan konsisten.

### 4. Ruang Lingkup Proyek

#### Fitur Wajib
1. Membaca data nilai siswa dari file teks.
2. Memvalidasi nilai siswa dalam rentang 0–100.
3. Menghitung rata-rata, nilai minimum, dan nilai maksimum.
4. Menentukan status ketuntasan berdasarkan Kriteria Ketuntasan Minimal (KKM).
5. Menyimpan hasil analisis ke dalam file laporan.

#### Batasan Proyek
1. Program menggunakan bahasa pemrograman Python.
2. Program dijalankan melalui terminal atau console.
3. Data siswa disimpan dalam file teks.
4. Program tidak menggunakan antarmuka grafis atau web.

### 5. Kebutuhan Proyek

#### A. Kebutuhan Fungsional
- Program dapat membaca data nilai dari file.
- Program dapat memvalidasi nilai siswa.
- Program dapat menghitung statistik nilai.
- Program dapat menentukan jumlah siswa tuntas dan belum tuntas.
- Program dapat menyimpan laporan hasil analisis.

#### B. Kebutuhan Nonfungsional
- Program mudah dijalankan melalui terminal VS Code.
- Pesan kesalahan mudah dipahami.
- Nama variabel dan fungsi jelas.
- Program dapat diuji ulang menggunakan test case yang sama.

### 6. Spesifikasi Input, Proses, dan Output (IPO)

| Input | Proses | Output |
|---|---|---|
| File berisi nama dan nilai siswa | Membaca dan memvalidasi data | Data nilai valid |
| Nilai siswa | Menghitung rata-rata, minimum, maksimum | Statistik nilai |
| Nilai dan KKM | Menentukan status ketuntasan | Jumlah siswa tuntas dan belum tuntas |
| Hasil analisis | Menyimpan laporan | File laporan.txt |

### 7. Algoritma dan Pseudocode

```text
MULAI

Baca data nilai dari file

Jika file tidak ditemukan:
    Tampilkan pesan kesalahan
    SELESAI

Untuk setiap data:
    Validasi format dan nilai
    Jika data valid:
        Simpan data

Jika tidak ada data valid:
    Tampilkan pesan
    SELESAI

Hitung rata-rata, nilai minimum,
dan nilai maksimum

Tentukan status ketuntasan berdasarkan KKM

Tampilkan hasil analisis

Simpan laporan ke file

SELESAI
```

### 8. Struktur Program

Program dibagi menjadi beberapa fungsi agar setiap bagian memiliki tanggung jawab yang jelas.

| Fungsi | Tanggung Jawab |
|---|---|
| baca_data() | Membaca data nilai dari file |
| validasi_nilai() | Memeriksa nilai dalam rentang 0–100 |
| hitung_statistik() | Menghitung statistik nilai |
| tentukan_status() | Menentukan ketuntasan siswa |
| hitung_ketuntasan() | Menghitung jumlah siswa tuntas dan belum tuntas |
| simpan_laporan() | Menyimpan laporan ke file |
| tampilkan_hasil() | Menampilkan hasil analisis |
| main() | Mengatur alur utama program |

#### Struktur Folder

```text
proyek-akhir-nama-tim/
│
├── README.md
├── proposal.md
├── .gitignore
│
├── data/
│   └── nilai_contoh.txt
│
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
│
├── tests/
│   └── test_case.md
│
└── output/
    └── .gitkeep
```

### 9. Struktur Data

Struktur data yang digunakan dalam proyek ini adalah:

1. **List**, digunakan untuk menyimpan kumpulan nilai siswa.
2. **Dictionary**, digunakan untuk menyimpan data siswa berupa nama dan nilai.
3. **String**, digunakan untuk menyimpan teks laporan.
4. **File**, digunakan untuk menyimpan data nilai dan hasil laporan.

Contoh model data:

```python
data_siswa = {
    "A001": {"nama": "Ayu", "nilai": 85},
    "A002": {"nama": "Budi", "nilai": 78}
}
```

### 10. Test Case

| ID | Kategori | Input/Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90 | Rata-rata 80 |
| TC02 | Batas | Nilai 0 | Diterima sebagai nilai valid |
| TC03 | Batas | Nilai 100 | Diterima sebagai nilai valid |
| TC04 | Invalid | Nilai 105 | Ditolak dengan pesan validasi |
| TC05 | Invalid | File tidak ditemukan | Kesalahan ditangani |
| TC06 | Normal | Semua nilai ≥ KKM | Semua siswa dinyatakan tuntas |

