from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'expert_stunting_secret_key_2026'

# ==================== SISTEM PAKAR: STUNTING ====================
database_kondisi = {
    "Stunting Berat + Malnutrisi": {
        "gejala": ["usia_0_60", "tb_sangat_pendek", "bb_sangat_kurang", "asi_tidak_eksklusif", "mpasi_terlambat", "frekuensi_makan_jarang", "imunisasi_tidak_lengkap", "sakit_berulang", "lingkungan_kumuh", "penghasilan_rendah", "ortu_pendek", "kebersihan_buruk"],
        "solusi": [
            "SEGERA KONSULTASI KE DOKTER ANAK",
            "Berikan makanan padat gizi seimbang setiap hari (karbohidrat, protein, lemak, vitamin, mineral)",
            "Pantau pertumbuhan setiap minggu di Posyandu",
            "Evaluasi kemungkinan infeksi kronis atau penyakit penyerta",
            "Perbaiki sanitasi lingkungan rumah",
            "Berikan ASI eksklusif jika masih dalam masa ASI"
        ],
        "tingkat_risiko": "Sangat Tinggi"
    },
    "Stunting (Pendek)": {
        "gejala": ["usia_0_60", "tb_sangat_pendek", "bb_normal", "mpasi_terlambat", "frekuensi_makan_jarang", "penghasilan_rendah"],
        "solusi": [
            "Tingkatkan asupan protein hewani (telur, ikan, ayam, hati)",
            "Berikan ASI eksklusif jika usia kurang dari 6 bulan",
            "Suplementasi vitamin A dan zinc sesuai dosis",
            "Konsultasi rutin ke Posyandu setiap bulan",
            "Berikan MPASI tepat waktu (mulai usia 6 bulan)"
        ],
        "tingkat_risiko": "Tinggi"
    },
    "Risiko Stunting": {
        "gejala": ["usia_0_60", "tb_pendek", "bb_normal", "mpasi_terlambat", "penghasilan_rendah"],
        "solusi": [
            "Lakukan intervensi gizi sejak dini",
            "Tambahkan 1 butir telur per hari ke dalam menu",
            "Pantau berat badan setiap 2 minggu",
            "Berikan vitamin D dan kalsium secara teratur",
            "Edukasi orang tua tentang gizi seimbang"
        ],
        "tingkat_risiko": "Sedang"
    },
    "Gizi Kurang (Underweight)": {
        "gejala": ["usia_0_60", "tb_normal", "bb_kurang", "frekuensi_makan_jarang", "nafsu_makan_buruk"],
        "solusi": [
            "Berikan makanan dengan kepadatan gizi tinggi",
            "Tambah frekuensi makan menjadi 4-5 kali sehari",
            "Berikan camilan sehat di antara waktu makan (buah, biskuit, puding susu)",
            "Konsultasikan ke ahli gizi untuk menu khusus",
            "Berikan multivitamin sesuai anjuran dokter"
        ],
        "tingkat_risiko": "Sedang"
    },
    "Gangguan Nafsu Makan": {
        "gejala": ["usia_0_60", "nafsu_makan_buruk", "asi_tidak_eksklusif"],
        "solusi": [
            "Berikan makanan dalam porsi kecil tapi sering (5-6 kali/hari)",
            "Variasi menu dan tampilan makanan agar menarik",
            "Hindari memberi snack atau jajan sebelum jam makan",
            "Ciptakan suasana makan yang menyenangkan tanpa paksaan",
            "Libatkan anak dalam proses memasak jika memungkinkan"
        ],
        "tingkat_risiko": "Rendah"
    },
    "Normal": {
        "gejala": ["usia_0_60", "tb_normal", "bb_normal", "asi_eksklusif", "mpasi_tepat", "imunisasi_lengkap", "lingkungan_bersih", "penghasilan_cukup"],
        "solusi": [
            "Pertahankan pola makan sehat dan seimbang",
            "Berikan stimulasi tumbuh kembang aktif setiap hari (bermain, bernyanyi, membaca)",
            "Lakukan kontrol rutin ke posyandu setiap bulan",
            "Lanjutkan pemberian ASI sampai usia 2 tahun",
            "Pastikan imunisasi lengkap sesuai jadwal"
        ],
        "tingkat_risiko": "Rendah"
    }
}

pertanyaan_list = [
    {"kode": "usia", "pertanyaan": "Apakah usia balita kurang dari 60 bulan (5 tahun)?"},
    {"kode": "tb", "pertanyaan": "Apakah tinggi badan balita terlihat lebih pendek dibandingkan teman sebayanya?"},
    {"kode": "tb_sangat", "pertanyaan": "Apakah tinggi badan balita jauh lebih pendek (jika dibandingkan standar usianya, termasuk sangat pendek)?"},
    {"kode": "bb", "pertanyaan": "Apakah berat badan balita terlihat sangat kurus untuk usianya?"},
    {"kode": "bb_kurang", "pertanyaan": "Apakah berat badan balita terlihat kurang ideal (agak kurus) untuk usianya?"},
    {"kode": "nafsu_makan", "pertanyaan": "Apakah balita sulit makan atau pilih-pilih makanan (picky eater)?"},
    {"kode": "asi", "pertanyaan": "Apakah balita mendapatkan ASI eksklusif selama 6 bulan pertama?"},
    {"kode": "mpasi", "pertanyaan": "Apakah MPASI (Makanan Pendamping ASI) diberikan tepat waktu yaitu mulai usia 6 bulan?"},
    {"kode": "frekuensi_makan", "pertanyaan": "Apakah balita makan kurang dari 3 kali dalam sehari?"},
    {"kode": "sakit", "pertanyaan": "Apakah balita sering sakit (demam, diare, ISPA) dalam 3 bulan terakhir?"},
    {"kode": "imunisasi", "pertanyaan": "Apakah imunisasi balita lengkap sesuai jadwal?"},
    {"kode": "lingkungan", "pertanyaan": "Apakah kondisi lingkungan rumah bersih dan memiliki akses air bersih?"}
]

def diagnosa_stunting(jawaban):
    gejala_terpilih = []
    if jawaban.get('usia') == 'Ya': gejala_terpilih.append("usia_0_60")
    
    if jawaban.get('tb') == 'Ya' and jawaban.get('tb_sangat') == 'Ya': gejala_terpilih.append("tb_sangat_pendek")
    elif jawaban.get('tb') == 'Ya': gejala_terpilih.append("tb_pendek")
    else: gejala_terpilih.append("tb_normal")
    
    if jawaban.get('bb') == 'Ya': gejala_terpilih.append("bb_sangat_kurang")
    elif jawaban.get('bb_kurang') == 'Ya': gejala_terpilih.append("bb_kurang")
    else: gejala_terpilih.append("bb_normal")
    
    if jawaban.get('nafsu_makan') == 'Ya': gejala_terpilih.append("nafsu_makan_buruk")
    if jawaban.get('asi') == 'Tidak': gejala_terpilih.append("asi_tidak_eksklusif")
    else: gejala_terpilih.append("asi_eksklusif")
    if jawaban.get('mpasi') == 'Tidak': gejala_terpilih.append("mpasi_terlambat")
    else: gejala_terpilih.append("mpasi_tepat")
    if jawaban.get('frekuensi_makan') == 'Ya': gejala_terpilih.append("frekuensi_makan_jarang")
    if jawaban.get('sakit') == 'Ya': gejala_terpilih.append("sakit_berulang")
    if jawaban.get('imunisasi') == 'Tidak': gejala_terpilih.append("imunisasi_tidak_lengkap")
    else: gejala_terpilih.append("imunisasi_lengkap")
    if jawaban.get('lingkungan') == 'Tidak': gejala_terpilih.append("lingkungan_kumuh")
    else: gejala_terpilih.append("lingkungan_bersih")
    
    diagnosis_prioritas = ["Stunting Berat + Malnutrisi", "Stunting (Pendek)", "Risiko Stunting", "Gizi Kurang (Underweight)", "Gangguan Nafsu Makan", "Normal"]
    
    for diagnosis in diagnosis_prioritas:
        if diagnosis in database_kondisi:
            required = database_kondisi[diagnosis]["gejala"]
            if all(g in gejala_terpilih for g in required):
                return {
                    'diagnosis': diagnosis,
                    'solusi': database_kondisi[diagnosis]["solusi"],
                    'tingkat_risiko': database_kondisi[diagnosis]["tingkat_risiko"],
                    'gejala_terdeteksi': len([g for g in required if g in gejala_terpilih]),
                    'total_gejala': len(required)
                }
    
    best_match = None
    best_score = 0
    for diagnosis, data in database_kondisi.items():
        if diagnosis == "Normal": continue
        required = data["gejala"]
        match_count = sum(1 for g in required if g in gejala_terpilih)
        if match_count > best_score and match_count >= len(required) * 0.6:
            best_score = match_count
            best_match = diagnosis
    
    if best_match:
        return {
            'diagnosis': best_match + " (Kecenderungan)",
            'solusi': database_kondisi[best_match]["solusi"],
            'tingkat_risiko': database_kondisi[best_match]["tingkat_risiko"],
            'gejala_terdeteksi': best_score,
            'total_gejala': len(database_kondisi[best_match]["gejala"])
        }
    
    return {
        'diagnosis': 'Normal (Tumbuh Kembang Baik)',
        'solusi': database_kondisi["Normal"]["solusi"],
        'tingkat_risiko': 'Rendah',
        'gejala_terdeteksi': 0,
        'total_gejala': 0
    }

# ==================== ROUTES ====================
@app.route('/')
def index():
    session.pop('jawaban', None)
    return render_template('stunting.html')

@app.route('/api/pakar/step', methods=['POST'])
def pakar_step():
    data = request.get_json()
    step = data.get('step', 0)
    jawaban_user = data.get('jawaban')
    
    if 'jawaban' not in session: session['jawaban'] = {}
    kode = pertanyaan_list[step]['kode']
    session['jawaban'][kode] = jawaban_user
    session.modified = True
    
    if step + 1 >= len(pertanyaan_list):
        hasil = diagnosa_stunting(session['jawaban'])
        return jsonify({'success': True, 'finished': True, 'result': hasil})
    else:
        return jsonify({
            'success': True,
            'finished': False,
            'next_step': step + 1,
            'next_question': pertanyaan_list[step + 1]
        })

@app.route('/api/pakar/reset', methods=['POST'])
def pakar_reset():
    session.pop('jawaban', None)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, port=5002)
