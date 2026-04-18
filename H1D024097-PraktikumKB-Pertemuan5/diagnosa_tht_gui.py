import tkinter as tk
from tkinter import messagebox

# DATA PENYAKIT & GEJALA (Berdasarkan Tabel Modul)
database_penyakit = {
    "Tonsilitis": ["G37", "G12", "G5", "G27", "G6", "G21"],
    "Sinusitis Maksilaris": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
    "Sinusitis Frontalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
    "Sinusitis Edmoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
    "Sinusitis Sfenoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
    "Abses Peritonsiler": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
    "Faringitis": ["G37", "G5", "G6", "G7", "G15"],
    "Kanker Laring": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
    "Deviasi Septum": ["G37", "G17", "G20", "G8", "G18", "G25"],
    "Laringitis": ["G37", "G5", "G15", "G16", "G32"],
    "Kanker Leher & Kepala": ["G5", "G22", "G8", "G28", "G3", "G11"],
    "Otitis Media Akut": ["G37", "G20", "G35", "G31"],
    "Contact Ulcers": ["G5", "G2"],
    "Abses Parafaringeal": ["G5", "G16"],
    "Barotitis Media": ["G12", "G20"],
    "Kanker Nafasoring": ["G17", "G8"],
    "Kanker Tonsil": ["G6", "G29"],
    "Neuronitis Vestibularis": ["G35", "G24"],
    "Meniere": ["G20", "G35", "G14", "G4"],
    "Tumor Syaraf Pendengaran": ["G12", "G34", "G23"],
    "Kanker Leher Metastatik": ["G29"],
    "Osteosklerosis": ["G34", "G9"],
    "Vertigo Postular": ["G24"]
}

# DAFTAR GEJALA (GI - G37)
semua_gejala = [
    ("G1", "Nafas abnormal"), ("G2", "Suara serak"), ("G3", "Perubahan kulit"),
    ("G4", "Telinga penuh"), ("G5", "Nyeri bicara menelan"), ("G6", "Nyeri tenggorokan"),
    ("G7", "Nyeri leher"), ("G8", "Pendarahan hidung"), ("G9", "Telinga berdenging"),
    ("G10", "Airliur menetes"), ("G11", "Perubahan suara"), ("G12", "Sakit kepala"),
    ("G13", "Nyeri pinggir hidung"), ("G14", "Serangan vertigo"), ("G15", "Getah bening"),
    ("G16", "Leher bengkak"), ("G17", "Hidung tersumbat"), ("G18", "Infeksi sinus"),
    ("G19", "Berat badan turun"), ("G20", "Nyeri telinga"), ("G21", "Selaput lendir merah"),
    ("G22", "Benjolan leher"), ("G23", "Tubuh tak seimbang"), ("G24", "Bolamata bergerak"),
    ("G25", "Nyeri wajah"), ("G26", "Dahi sakit"), ("G27", "Batuk"),
    ("G28", "Tumbuh dimulut"), ("G29", "Benjolan leher"), ("G30", "Nyeri antara mata"),
    ("G31", "Radang gendang telinga"), ("G32", "Tenggorokan gatal"), ("G33", "Hidung meler"),
    ("G34", "Tuli"), ("G35", "Mual muntah"), ("G36", "Letih lesu"), ("G37", "Demam")
]

class AplikasiPakarTHT:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Penyakit THT")
        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        self.label_tanya = tk.Label(root, text="SISTEM PAKAR DIAGNOSA THT", font=("Arial", 12, "bold"))
        self.label_tanya.pack(pady=20)

        self.btn_mulai = tk.Button(root, text="Mulai Diagnosa", command=self.mulai_tanya)
        self.btn_mulai.pack(pady=10)

        self.frame_jawaban = tk.Frame(root)
        self.btn_ya = tk.Button(self.frame_jawaban, text="YA", width=10, command=lambda: self.jawab('y'))
        self.btn_tidak = tk.Button(self.frame_jawaban, text="TIDAK", width=10, command=lambda: self.jawab('t'))
        self.btn_ya.pack(side=tk.LEFT, padx=10)
        self.btn_tidak.pack(side=tk.LEFT, padx=10)

    def mulai_tanya(self):
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        self.btn_mulai.pack_forget()
        self.frame_jawaban.pack(pady=20)
        self.tampilkan_pertanyaan()

    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(semua_gejala):
            kode, teks = semua_gejala[self.index_pertanyaan]
            self.label_tanya.config(text=f"Apakah Anda mengalami {teks}?")
        else:
            self.proses_hasil()

    def jawab(self, respon):
        if respon == 'y':
            kode = semua_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)
        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()

    # PERBAIKAN: Fungsi proses_hasil sekarang berada di dalam class
    def proses_hasil(self):
        hasil = []
        for penyakit, syarat in database_penyakit.items():
            if all(s in self.gejala_terpilih for s in syarat):
                hasil.append(f"- {penyakit}")

        kesimpulan = "\n".join(hasil) if hasil else "Penyakit tidak terdeteksi berdasarkan pola gejala."
        messagebox.showinfo("Hasil Diagnosa", f"Hasil Diagnosa THT:\n\n{kesimpulan}")

        self.frame_jawaban.pack_forget()
        self.btn_mulai.pack(pady=10)
        self.label_tanya.config(text="Diagnosa Selesai. Ingin mengulang?")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x300")
    app = AplikasiPakarTHT(root)
    root.mainloop()