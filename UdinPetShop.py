# Import Library
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Deklarasi Variabel
barang = ctrl.Antecedent(np.arange(0, 101, 1), 'barang_terjual')
permintaan = ctrl.Antecedent(np.arange(0, 301, 1), 'permintaan')
harga = ctrl.Antecedent(np.arange(0, 100001, 1), 'harga_per_item')
profit = ctrl.Antecedent(np.arange(0, 4000001, 1), 'profit')
stok = ctrl.Consequent(np.arange(0, 1001, 1), 'stok_makanan')

# Himpunan Barang
barang['rendah'] = fuzz.trapmf(barang.universe, [0, 0, 20, 50])
barang['sedang'] = fuzz.trimf(barang.universe, [30, 50, 70])
barang['tinggi'] = fuzz.trapmf(barang.universe, [50, 90, 100, 100])

# Himpunan Permintaan
permintaan['rendah'] = fuzz.trapmf(permintaan.universe, [0, 0, 50, 150])
permintaan['sedang'] = fuzz.trimf(permintaan.universe, [100, 150, 200])
permintaan['tinggi'] = fuzz.trapmf(permintaan.universe, [150, 250, 300, 300])

# Himpunan Harga
harga['murah'] = fuzz.trapmf(harga.universe, [0, 0, 20000, 60000])
harga['sedang'] = fuzz.trimf(harga.universe, [30000, 60000, 80000])
harga['mahal'] = fuzz.trapmf(harga.universe, [60000, 80000, 100000, 100000])

# Himpunan Profit
profit['rendah'] = fuzz.trapmf(profit.universe, [0, 0, 500000, 2500000])
profit['sedang'] = fuzz.trimf(profit.universe, [1500000, 2500000, 3500000])
profit['tinggi'] = fuzz.trapmf(profit.universe, [2500000, 3500000, 4000000, 4000000])

# Himpunan Stok
stok['sedang'] = fuzz.trapmf(stok.universe, [0, 0, 600, 900])
stok['banyak'] = fuzz.trapmf(stok.universe, [600, 900, 1000, 1000])

# Aturan Fuzzy
aturan1 = ctrl.Rule(barang['tinggi'] & permintaan['tinggi'] & harga['murah'] & profit['tinggi'], stok['banyak'])
aturan2 = ctrl.Rule(barang['tinggi'] & permintaan['tinggi'] & harga['murah'] & profit['sedang'], stok['sedang'])
aturan3 = ctrl.Rule(barang['tinggi'] & permintaan['sedang'] & harga['murah'] & profit['sedang'], stok['sedang'])
aturan4 = ctrl.Rule(barang['sedang'] & permintaan['tinggi'] & harga['murah'] & profit['sedang'], stok['sedang'])
aturan5 = ctrl.Rule(barang['sedang'] & permintaan['tinggi'] & harga['murah'] & profit['tinggi'], stok['banyak'])
aturan6 = ctrl.Rule(barang['rendah'] & permintaan['rendah'] & harga['sedang'] & profit['sedang'], stok['sedang'])

# Deklarasi Control System dan Simulasi
engine = ctrl.ControlSystem([aturan1, aturan2, aturan3, aturan4, aturan5, aturan6])
system = ctrl.ControlSystemSimulation(engine)

# Simulasi Perhitungan Sistem
system.input['barang_terjual'] = 80 #input_barang
system.input['permintaan'] = 255 #input_permintaan
system.input['harga_per_item'] = 25000 #input_harga
system.input['profit'] = 3500000 #input_profit
system.compute()

# Output
print(f"Stok yang diperlukan : {system.output['stok_makanan']:.2f}")
stok.view(sim=system)
