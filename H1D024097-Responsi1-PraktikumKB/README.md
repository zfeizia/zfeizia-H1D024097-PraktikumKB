# Responsi 1 - Praktikum Kecerdasan Buatan (KB)
**Nama:** Feizia  
**NIM:** H1D024097  
**Shift:** E

---

## Deskripsi Proyek
Proyek ini dikembangkan sebagai bagian dari Responsi 1 Praktikum Kecerdasan Buatan. Proyek ini mencakup dua sistem utama yang mengimplementasikan konsep-konsep dasar AI untuk menyelesaikan masalah di dunia nyata:

1.  **Sistem Fuzzy (Penentuan Kelayakan Bansos):** Menggunakan logika fuzzy untuk menentukan tingkat kelayakan rumah tangga dalam menerima bantuan sosial berdasarkan indikator ekonomi.
2.  **Sistem Pakar (Diagnosa Stunting):** Menggunakan basis pengetahuan pakar kesehatan untuk mendiagnosa risiko stunting pada balita berdasarkan gejala dan kondisi lingkungan.

---

## Struktur Proyek
```text
H1D024097-Responsi1-PraktikumKB/
├── sistem_fuzzy/            # Implementasi Logika Fuzzy
│   ├── app.py               # Backend Flask (Logika Fuzzy)
│   ├── templates/           # UI (HTML/CSS)
│   └── README.md            # Dokumentasi Detail Fuzzy
├── sistem_pakar/            # Implementasi Sistem Pakar
│   ├── app.py               # Backend Flask (Basis Pengetahuan)
│   ├── templates/           # UI (HTML/CSS)
│   └── README.md            # Dokumentasi Detail Sistem Pakar
└── README.md                # Dokumentasi Utama (File Ini)
```

---

## Teknologi yang Digunakan
- **Bahasa Pemrograman:** Python 
- **Framework Web:** Flask
- **Frontend:** HTML5, CSS3, JavaScript
  
---

## Cara Menjalankan Secara Lokal

### 1. Persiapan
Pastikan Anda sudah menginstal Python di sistem Anda.

### 2. Menjalankan Sistem Fuzzy
```bash
cd sistem_fuzzy
pip install -r requirements.txt
python app.py
```
Akses di browser: `http://127.0.0.1:5001`

### 3. Menjalankan Sistem Pakar
```bash
cd sistem_pakar
pip install -r requirements.txt
python app.py
```
Akses di browser: `http://127.0.0.1:5002`

---

## Dokumentasi Detail
Untuk penjelasan lebih mendalam mengenai logika dan aturan di setiap sistem, silakan baca:
- [Dokumentasi Sistem Fuzzy](sistem_fuzzy/README.md)
- [Dokumentasi Sistem Pakar](sistem_pakar/README.md)
