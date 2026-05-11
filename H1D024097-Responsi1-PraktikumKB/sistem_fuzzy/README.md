# Sistem Fuzzy: Penentuan Kelayakan Bansos

Sistem ini dirancang untuk mensimulasikan proses pengambilan keputusan manusia dalam menentukan apakah sebuah keluarga layak menerima Bantuan Sosial (Bansos) menggunakan **Logika Fuzzy**.

## Variabel Input
Sistem menggunakan 3 variabel input utama:
1.  **Pendapatan (Juta):** Rentang 0.5 - 10 (Rendah, Sedang, Tinggi)
2.  **Daya Listrik (VA):** Rentang 450 - 2200 (Rendah, Sedang, Tinggi)
3.  **Jumlah Tanggungan:** Rentang 1 - 8 (Sedikit, Cukup, Banyak)

## Logika Fuzzy
Sistem ini mengimplementasikan:
-   **Fuzzifikasi:** Mengubah nilai tegas (crisp) menjadi nilai linguistik menggunakan fungsi keanggotaan (Linear & Segitiga).
-   **Inference Engine:** Menggunakan 9 aturan (rules) dasar untuk menentukan bobot kelayakan.
-   **Defuzzifikasi:** Menggunakan metode **Weighted Average** untuk menghasilkan skor kelayakan (0-100).

## Contoh Aturan (Rules)
-   `IF Pendapatan Rendah AND Listrik Rendah AND Tanggungan Banyak THEN Sangat Layak`
-   `IF Pendapatan Tinggi AND Listrik Tinggi THEN Tidak Layak`

## Output Status
-   **Sangat Layak:** >= 80
-   **Layak:** >= 60
-   **Cukup Layak:** >= 40
-   **Kurang Layak:** >= 20
-   **Tidak Layak:** < 20

---
[ Kembali ke Utama](../README.md)
