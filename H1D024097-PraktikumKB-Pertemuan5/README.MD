# Laporan Pengerjaan Tugas Praktikum
## PERTEMUAN 5: SISTEM PAKAR 2

Repositori ini dibuat untuk memenuhi tugas mata kuliah Praktikum Kecerdasan Buatan (KB) Pertemuan 5. Project ini mengimplementasikan Sistem Pakar diagnosa penyakit THT (Telinga, Hidung, dan Tenggorokan) berbasis GUI menggunakan Python.

### Deskripsi Studi Kasus
Aplikasi ini melakukan diagnosa berdasarkan data yang bersumber dari modul praktikum, yang terdiri dari:
* **Gejala**: Terdapat 37 jenis gejala (kode G1 sampai G37) seperti demam, suara serak, nyeri telinga, dan lain-lain.
* **Penyakit**: Terdapat 23 klasifikasi penyakit THT yang dideteksi berdasarkan pola kemunculan gejala tertentu.

### Teknologi yang Digunakan
* **Bahasa Pemrograman**: Python 3.x
* **Library GUI**: `tkinter` (Standard Python Interface to Tcl/Tk)
* **Metode Inferensi**: Forward Chaining (Pencocokan gejala yang diinput pengguna dengan aturan/database penyakit).

### Struktur Basis Pengetahuan
Sistem ini menggunakan struktur data dictionary untuk memetakan penyakit dengan daftar gejalanya, contohnya:
* **Tonsilitis**: Memerlukan gejala G37, G12, G5, G27, G6, dan G21.
* **Sinusitis Maksilaris**: Memerlukan gejala G37, G12, G27, G17, G33, G36, dan G29.