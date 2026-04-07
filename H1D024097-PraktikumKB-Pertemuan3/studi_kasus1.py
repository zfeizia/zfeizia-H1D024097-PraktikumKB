import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
 
# 1. Definisi Antecedent (Input) dan Consequent (Output)
# Range ditentukan berdasarkan semesta pembicaraan pada soal
barang_terjual = ctrl.Antecedent(np.arange(0, 101, 1), 'barang_terjual')
permintaan = ctrl.Antecedent(np.arange(0, 301, 1), 'permintaan')
harga_item = ctrl.Antecedent(np.arange(0, 100001, 1), 'harga_item')
profit = ctrl.Antecedent(np.arange(0, 4000001, 1), 'profit')
 
stok_makanan = ctrl.Consequent(np.arange(0, 1001, 1), 'stok_makanan')
 
# 2. Membership Functions (Menggunakan fungsi segitiga/trimf sebagai standar)
# Barang Terjual [0 - 100]
barang_terjual['rendah'] = fuzz.trimf(barang_terjual.universe, [0, 0, 40])
barang_terjual['sedang'] = fuzz.trimf(barang_terjual.universe, [30, 50, 70])
barang_terjual['tinggi'] = fuzz.trimf(barang_terjual.universe, [60, 100, 100])
 
# Permintaan [0 - 300]
permintaan['rendah'] = fuzz.trimf(permintaan.universe, [0, 0, 100])
permintaan['sedang'] = fuzz.trimf(permintaan.universe, [50, 150, 250])
permintaan['tinggi'] = fuzz.trimf(permintaan.universe, [200, 300, 300])
 
# Harga per Item [0 - 100.000]
harga_item['murah'] = fuzz.trimf(harga_item.universe, [0, 0, 40000])
harga_item['sedang'] = fuzz.trimf(harga_item.universe, [30_000, 50000, 80000])
harga_item['mahal'] = fuzz.trimf(harga_item.universe, [60000, 100000, 100000])
 
# Profit [0 - 4.000.000]
profit['rendah'] = fuzz.trimf(profit.universe, [0, 0, 1_000_000])
profit['sedang'] = fuzz.trimf(profit.universe, [1_000_000, 2_000_000, 2_500_000])
profit['banyak'] = fuzz.trapmf(profit.universe, [1_500_000, 2_500_000, 4_000_000, 4_000_000])
 
# Stok Makanan (Output) [0 - 1000]
stok_makanan['sedang'] = fuzz.trimf(stok_makanan.universe, [100, 500, 900])
stok_makanan['banyak'] = fuzz.trimf(stok_makanan.universe, [600, 1000, 1000])
 
# 3. Definisi Aturan Fuzzy (Rules)
rule1 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['tinggi'] & harga_item['murah'] & profit['banyak'], stok_makanan['banyak'])
rule2 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['tinggi'] & harga_item['murah'] & profit['sedang'], stok_makanan['sedang'])
rule3 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['sedang'] & harga_item['murah'] & profit['sedang'], stok_makanan['sedang'])
rule4 = ctrl.Rule(barang_terjual['sedang'] & permintaan['tinggi'] & harga_item['murah'] & profit['sedang'], stok_makanan['sedang'])
rule5 = ctrl.Rule(barang_terjual['sedang'] & permintaan['tinggi'] & harga_item['murah'] & profit['banyak'], stok_makanan['banyak'])
rule6 = ctrl.Rule(barang_terjual['rendah'] & permintaan['rendah'] & harga_item['sedang'] & profit['sedang'], stok_makanan['sedang'])
 
# 4. Sistem Kontrol dan Simulasi
stok_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
stok_simulation = ctrl.ControlSystemSimulation(stok_ctrl)
 
# 5. Memasukkan Nilai Input Sesuai Soal
# barang terjual = 80, permintaan = 255, harga per item = Rp 25.000, dan profit = Rp 3.500.000
stok_simulation.input['barang_terjual'] = 80
stok_simulation.input['permintaan'] = 255
stok_simulation.input['harga_item'] = 25000
stok_simulation.input['profit'] = 3500000
 
# 6. Melakukan Perhitungan (Crushing/Compute)
stok_simulation.compute()
 
# 7. Output Hasil
hasil_stok = stok_simulation.output['stok_makanan']
print("--- HASIL PERHITUNGAN LOGIKA FUZZY ---")
print(f"Barang Terjual : 80")
print(f"Permintaan     : 255")
print(f"Harga per Item : 25.000")
print(f"Profit         : 3.500.000")
print(f"Jumlah Stok Makanan yang Direkomendasikan: {hasil_stok:.2f} unit")
 
# Visualisasi (Opsional, butuh matplotlib)
stok_makanan.view(sim=stok_simulation)
barang_terjual.view()
permintaan.view()
harga_item.view()
profit.view()

import matplotlib.pyplot as plt 

# plt.xticks(np.arange(0, 501, 100))
plt.show()