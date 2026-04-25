from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = 'fuzzy_bansos_secret_key_2026'

# ==================== SISTEM FUZZY: BANSOS ====================
def fuzzy_bansos(pendapatan, listrik, tanggungan):
    """Menentukan kelayakan penerima bansos menggunakan logika fuzzy"""
    
    def pendapatan_rendah(x):
        if x <= 1.5: return 1
        elif x <= 3: return (3 - x) / 1.5
        else: return 0
    
    def pendapatan_sedang(x):
        if 1.5 <= x <= 2.5: return (x - 1.5) / 1
        elif 2.5 <= x <= 4: return (4 - x) / 1.5
        else: return 0
    
    def pendapatan_tinggi(x):
        if x >= 4: return min(1, (x - 3) / 2)
        else: return 0
    
    def listrik_rendah(x):
        if x <= 900: return 1
        elif x <= 1300: return (1300 - x) / 400
        else: return 0
    
    def listrik_sedang(x):
        if 900 <= x <= 1300: return (x - 900) / 400
        elif 1300 <= x <= 2200: return (2200 - x) / 900
        else: return 0
    
    def listrik_tinggi(x):
        if x >= 1300: return min(1, (x - 900) / 1300)
        else: return 0
    
    def tanggungan_sedikit(x):
        if x <= 2: return 1
        elif x <= 4: return (4 - x) / 2
        else: return 0
    
    def tanggungan_cukup(x):
        if 2 <= x <= 3: return (x - 2) / 1
        elif 3 <= x <= 5: return (5 - x) / 2
        else: return 0
    
    def tanggungan_banyak(x):
        if x >= 4: return min(1, (x - 3) / 3)
        else: return 0
    
    p_rendah = pendapatan_rendah(pendapatan)
    p_sedang = pendapatan_sedang(pendapatan)
    p_tinggi = pendapatan_tinggi(pendapatan)
    
    l_rendah = listrik_rendah(listrik)
    l_sedang = listrik_sedang(listrik)
    l_tinggi = listrik_tinggi(listrik)
    
    t_sedikit = tanggungan_sedikit(tanggungan)
    t_cukup = tanggungan_cukup(tanggungan)
    t_banyak = tanggungan_banyak(tanggungan)
    
    r1 = min(p_rendah, l_rendah, t_banyak)
    r2 = min(p_rendah, l_rendah, t_cukup)
    r3 = min(p_rendah, l_sedang, t_banyak)
    r4 = min(p_rendah, l_sedang, t_cukup)
    r5 = min(p_sedang, l_rendah, t_banyak)
    r6 = min(p_sedang, l_rendah, t_cukup)
    r7 = min(p_sedang, l_sedang, t_sedikit)
    r8 = max(p_tinggi, l_tinggi, t_sedikit)
    r9 = min(p_tinggi, l_tinggi)
    
    rules = [(r1, 100), (r2, 80), (r3, 80), (r4, 60), (r5, 60), (r6, 40), (r7, 40), (r8, 20), (r9, 0)]
    
    total_weight = sum(w for w, _ in rules)
    if total_weight == 0:
        return 0, "Tidak Layak"
    
    kelayakan = sum(w * n for w, n in rules) / total_weight
    
    if kelayakan >= 80:
        status = "Sangat Layak"
    elif kelayakan >= 60:
        status = "Layak"
    elif kelayakan >= 40:
        status = "Cukup Layak"
    elif kelayakan >= 20:
        status = "Kurang Layak"
    else:
        status = "Tidak Layak"
    
    return round(kelayakan, 2), status

# ==================== ROUTES ====================
@app.route('/')
def index():
    return render_template('bansos.html')

@app.route('/api/fuzzy/hitung', methods=['POST'])
def hitung_fuzzy():
    data = request.get_json()
    pendapatan = max(0.5, min(10, float(data.get('pendapatan', 2.5))))
    listrik = max(450, min(2200, float(data.get('listrik', 900))))
    tanggungan = max(1, min(8, int(data.get('tanggungan', 4))))
    
    kelayakan, status = fuzzy_bansos(pendapatan, listrik, tanggungan)
    
    return jsonify({
        'success': True,
        'kelayakan': kelayakan,
        'status': status,
        'pendapatan': pendapatan,
        'listrik': listrik,
        'tanggungan': tanggungan
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)
