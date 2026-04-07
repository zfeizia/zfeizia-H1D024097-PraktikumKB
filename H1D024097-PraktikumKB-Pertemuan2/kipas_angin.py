# Import library
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Menyiapkan himpunan Fuzzy 
suhu = ctrl.Antecedent(np.arange(0, 41), 'suhu')
kelembapan = ctrl.Antecedent(np.arange(0, 101), 'kelembapan')
kecepatan = ctrl.Consequent(np.arange(0, 101), 'kecepatan')

# Suhu: Rendah, Normal, Tinggi
suhu['Rendah'] = fuzz.trimf(suhu.universe, [0, 0, 20])
suhu['Normal'] = fuzz.trimf(suhu.universe, [15, 25, 35])
suhu['Tinggi'] = fuzz.trimf(suhu.universe, [30, 40, 40])

# Kelembapan: Kering, Lembap, Basah
kelembapan['Kering'] = fuzz.trimf(kelembapan.universe, [0, 0, 50])
kelembapan['Lembap'] = fuzz.trimf(kelembapan.universe, [30, 50, 70])
kelembapan['Basah'] = fuzz.trimf(kelembapan.universe, [50, 100, 100])

# Kecepatan Kipas: Lambat, Sedang, Cepat
kecepatan['Lambat'] = fuzz.trimf(kecepatan.universe, [0, 0, 50])
kecepatan['Sedang'] = fuzz.trimf(kecepatan.universe, [30, 50, 70])
kecepatan['Cepat'] = fuzz.trimf(kecepatan.universe, [50, 100, 100])

# Membuat aturan Fuzzy 
aturan1 = ctrl.Rule(suhu['Rendah'] | kelembapan['Basah'], kecepatan['Lambat'])
aturan2 = ctrl.Rule(suhu['Normal'], kecepatan['Sedang'])
aturan3 = ctrl.Rule(suhu['Tinggi'] & kelembapan['Kering'], kecepatan['Cepat'])

engine = ctrl.ControlSystem([aturan1, aturan2, aturan3])
sistem_kipas = ctrl.ControlSystemSimulation(engine)

sistem_kipas.input['suhu'] = 28
sistem_kipas.input['kelembapan'] = 37
sistem_kipas.compute()
print(f"Hasil Kecepatan Kipas: {sistem_kipas.output['kecepatan']}")

# Menampilkan grafik 
suhu.view()
kelembapan.view()
kecepatan.view(sim=sistem_kipas)

import matplotlib.pyplot as plt
plt.show()