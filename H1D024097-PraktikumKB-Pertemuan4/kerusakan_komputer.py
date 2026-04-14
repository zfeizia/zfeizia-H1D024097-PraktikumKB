import tkinter as tk
from tkinter import messagebox, ttk

# 1. KNOWLEDGE BASE (Minimal 5 Kerusakan)
# Struktur data Dictionary digunakan untuk menyimpan aturan (Rules) [cite: 329, 330]
knowledge_base = {
    "RAM Rusak atau Kotor": {
        "gejala": ["bip_berulang", "layar_blank", "sering_bsod"],
        "solusi": "Lepas RAM, bersihkan pin emasnya dengan penghapus karet, lalu pasang kembali dengan kuat."
    },
    "Power Supply (PSU) Lemah": {
        "gejala": ["sering_restart", "pc_mati_mendadak", "bau_hangus"],
        "solusi": "Cek kabel power atau ganti PSU dengan unit yang memiliki sertifikasi 80+ untuk kestabilan daya."
    },
    "Overheat (Prosesor)": {
        "gejala": ["performa_lambat", "suhu_tinggi", "kipas_berisik"],
        "solusi": "Bersihkan debu pada heatsink dan ganti thermal paste pada prosesor Anda."
    },
    "VGA/GPU Bermasalah": {
        "gejala": ["layar_bergaris", "artifak_visual", "warna_tidak_normal"],
        "solusi": "Re-seat (cabut-pasang) kartu grafis atau update driver GPU ke versi terbaru."
    },
    "Harddisk Corrupt/Bad Sector": {
        "gejala": ["booting_sangat_lama", "bunyi_tik_tik", "data_sering_hilang"],
        "solusi": "Gunakan perintah 'chkdsk' untuk perbaikan software atau segera ganti ke SSD jika sudah rusak fisik."
    }
}

# 2. DAFTAR PERTANYAAN (Mapping Kode ke Pertanyaan) [cite: 337, 338]
pertanyaan_list = [
    ("bip_berulang", "Apakah terdengar bunyi bip berulang saat menyalakan PC?"),
    ("layar_blank", "Apakah layar monitor tetap hitam meskipun PC menyala?"),
    ("sering_bsod", "Apakah sering muncul layar biru (Blue Screen of Death)?"),
    ("sering_restart", "Apakah komputer sering restart sendiri tanpa sebab?"),
    ("pc_mati_mendadak", "Apakah PC tiba-tiba mati total saat sedang digunakan?"),
    ("bau_hangus", "Apakah tercium bau hangus atau panas berlebih dari CPU?"),
    ("performa_lambat", "Apakah performa melambat drastis setelah pemakaian lama?"),
    ("suhu_tinggi", "Apakah suhu area prosesor terasa sangat panas menyengat?"),
    ("kipas_berisik", "Apakah suara kipas terdengar sangat kencang dan kasar?"),
    ("layar_bergaris", "Apakah muncul garis-garis aneh atau kotak kecil di layar?"),
    ("artifak_visual", "Apakah tampilan gambar terlihat pecah-pecah/artifak?"),
    ("warna_tidak_normal", "Apakah warna pada layar terlihat pudar atau berubah?"),
    ("booting_sangat_lama", "Apakah proses loading Windows memakan waktu sangat lama?"),
    ("bunyi_tik_tik", "Apakah terdengar bunyi 'tik-tik' mekanik dari dalam casing?"),
    ("data_sering_hilang", "Apakah file atau folder sering corrupt atau hilang?")
]

class ExpertSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diagnosa Kerusakan Komputer")
        self.root.geometry("480x350")
        
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        
        # UI Setup [cite: 365, 369, 370]
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(expand=True, fill="both")
        
        self.lbl_judul = ttk.Label(self.main_frame, text="Diagnosa Kerusakan Komputer", font=("Helvetica", 14, "bold"))
        self.lbl_judul.pack(pady=10)
        
        self.lbl_tanya = ttk.Label(self.main_frame, text="Tekan tombol di bawah untuk mulai diagnosa.", wraplength=400, font=("Helvetica", 11))
        self.lbl_tanya.pack(pady=30)
        
        self.btn_start = ttk.Button(self.main_frame, text="Mulai Diagnosa", command=self.mulai)
        self.btn_start.pack()
        
        self.btn_frame = ttk.Frame(self.main_frame)
        self.btn_ya = ttk.Button(self.btn_frame, text="Ya", command=lambda: self.jawab(True))
        self.btn_tidak = ttk.Button(self.btn_frame, text="Tidak", command=lambda: self.jawab(False))

    def mulai(self):
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        self.btn_start.pack_forget()
        self.btn_frame.pack(pady=10)
        self.btn_ya.pack(side="left", padx=10)
        self.btn_tidak.pack(side="left", padx=10)
        self.tampilkan_pertanyaan()

    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(pertanyaan_list):
            _, teks = pertanyaan_list[self.index_pertanyaan]
            self.lbl_tanya.config(text=teks)
        else:
            self.proses_inferensi()

    def jawab(self, kondisi):
        if kondisi:
            kode, _ = pertanyaan_list[self.index_pertanyaan]
            self.gejala_terpilih.append(kode)
        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()

    # 3. MESIN INFERENSI [cite: 437, 439, 440]
    def proses_inferensi(self):
        hasil = []
        for kerusakan, data in knowledge_base.items():
            # Cek apakah semua gejala dalam aturan terpenuhi (Logic AND)
            if all(g in self.gejala_terpilih for g in data["gejala"]):
                hasil.append((kerusakan, data["solusi"]))
        
        # 4. OUTPUT HASIL [cite: 465, 467, 470]
        if hasil:
            format_hasil = ""
            for k, s in hasil:
                format_hasil += f"KERUSAKAN: {k}\nSOLUSI: {s}\n\n"
            messagebox.showinfo("Hasil Diagnosa", format_hasil)
        else:
            messagebox.showwarning("Hasil Diagnosa", "Maaf, gejala tidak cocok dengan kerusakan apa pun dalam database kami.")
            
        self.reset_ui()

    def reset_ui(self):
        self.btn_frame.pack_forget()
        self.btn_start.pack(pady=10)
        self.lbl_tanya.config(text="Diagnosa selesai. Ingin mencoba lagi?")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpertSystemApp(root)
    root.mainloop()