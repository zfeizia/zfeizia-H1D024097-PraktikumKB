# Tugas Praktikum KB - Pertemuan 2 
**Sistem Logika Fuzzy Penentuan Kecepatan Kipas Angin**

## Deskripsi Sistem
Program ini merupakan sistem logika fuzzy untuk menentukan kecepatan kipas angin berdasarkan kondisi lingkungan. [cite_start]Sistem dibangun menggunakan bahasa pemrograman **Python** dengan library **SciKit-Fuzzy**[cite: 51, 406].

### Ketentuan Sistem:
1. [cite_start]**2 Variabel Input (Antecedent):** - **Suhu:** Rentang 0–40 °C (Himpunan: Rendah, Normal, Tinggi)[cite: 406].
   - [cite_start]**Kelembapan:** Rentang 0–100 % (Himpunan: Kering, Lembap, Basah)[cite: 406].
2. **1 Variabel Output (Consequent):**
   - [cite_start]**Kecepatan Kipas:** Rentang 0–100 (Himpunan: Lambat, Sedang, Cepat)[cite: 406].
3. [cite_start]**Aturan Fuzzy:** Menggunakan minimal 3 aturan IF-THEN untuk pemetaan relasi antar himpunan[cite: 41, 406].
