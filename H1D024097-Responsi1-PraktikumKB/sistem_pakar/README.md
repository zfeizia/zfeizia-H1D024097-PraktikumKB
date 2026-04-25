# 🩺 Sistem Pakar: Diagnosa Stunting

Sistem ini merupakan aplikasi berbasis pengetahuan (knowledge-based system) yang membantu orang tua mendiagnosa risiko stunting pada balita berdasarkan gejala fisik dan faktor pendukung lainnya.

## 🧠 Metode Reasoning
Sistem menggunakan metode **Forward Chaining**, di mana sistem akan mencocokkan gejala yang dimasukkan pengguna dengan basis pengetahuan yang ada untuk menarik kesimpulan.

## 📚 Basis Pengetahuan (Knowledge Base)
Sistem dapat mendiagnosa beberapa kategori kondisi:
1.  **Stunting Berat + Malnutrisi:** Kondisi kritis yang membutuhkan penanganan medis segera.
2.  **Stunting (Pendek):** Kondisi tinggi badan di bawah standar kronis.
3.  **Risiko Stunting:** Indikasi awal gangguan pertumbuhan.
4.  **Gizi Kurang (Underweight):** Masalah pada berat badan balita.
5.  **Gangguan Nafsu Makan:** Masalah perilaku makan.
6.  **Normal:** Tumbuh kembang sesuai standar.

## 📋 Fitur Utama
-   **Konsultasi Interaktif:** Tanya jawab bertahap untuk mempermudah pengguna.
-   **Saran Pakar:** Memberikan solusi medis dan nutrisi praktis sesuai hasil diagnosa.
-   **Visualisasi Risiko:** Menggunakan indikator warna untuk menunjukkan tingkat keparahan (Rendah, Sedang, Tinggi, Sangat Tinggi).

## 🛡️ Komponen Diagnosa
Input yang dinilai meliputi:
-   Tinggi Badan (TB) & Berat Badan (BB)
-   Pemberian ASI Eksklusif & MPASI
-   Riwayat Penyakit & Imunisasi
-   Kondisi Sanitasi Lingkungan

---
[ Kembali ke Utama](../README.md)
