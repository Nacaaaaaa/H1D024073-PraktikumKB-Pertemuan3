import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Deklarasi Variabel
informasi = ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_informasi')
persyaratan = ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_persyaratan')
petugas = ctrl.Antecedent(np.arange(0, 101, 1), 'kemampuan_petugas')
sarpras = ctrl.Antecedent(np.arange(0, 101, 1), 'ketersediaan_sarpras')
kepuasan = ctrl.Consequent(np.arange(0, 401, 1), 'kepuasan_pelayanan')

# Himpunan Fuzzy
informasi['tidak_memuaskan'] = fuzz.trapmf(informasi.universe, [0, 0, 60, 75])
informasi['cukup_memuaskan'] = fuzz.trimf(informasi.universe, [60, 75, 90])
informasi['memuaskan'] = fuzz.trapmf(informasi.universe, [75, 90, 100, 100])

persyaratan['tidak_memuaskan'] = fuzz.trapmf(persyaratan.universe, [0, 0, 60, 75])
persyaratan['cukup_memuaskan'] = fuzz.trimf(persyaratan.universe, [60, 75, 90])
persyaratan['memuaskan'] = fuzz.trapmf(persyaratan.universe, [75, 90, 100, 100])

petugas['tidak_memuaskan'] = fuzz.trapmf(petugas.universe, [0, 0, 60, 75])
petugas['cukup_memuaskan'] = fuzz.trimf(petugas.universe, [60, 75, 90])
petugas['memuaskan'] = fuzz.trapmf(petugas.universe, [75, 90, 100, 100])

sarpras['tidak_memuaskan'] = fuzz.trapmf(sarpras.universe, [0, 0, 60, 75])
sarpras['cukup_memuaskan'] = fuzz.trimf(sarpras.universe, [60, 75, 90])
sarpras['memuaskan'] = fuzz.trapmf(sarpras.universe, [75, 90, 100, 100])

kepuasan['tidak_memuaskan'] = fuzz.trapmf(kepuasan.universe, [0, 0, 50, 75])
kepuasan['kurang_memuaskan'] = fuzz.trimf(kepuasan.universe, [50, 100, 150])
kepuasan['cukup_memuaskan'] = fuzz.trimf(kepuasan.universe, [150, 175, 250])
kepuasan['memuaskan'] = fuzz.trimf(kepuasan.universe, [250, 275, 350])
kepuasan['sangat_memuaskan'] = fuzz.trapmf(kepuasan.universe, [325, 350, 400, 400])

# Aturan Fuzzy
aturan1 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['tidak_memuaskan'])
aturan2 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['tidak_memuaskan'])
aturan3 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['tidak_memuaskan'])
aturan4 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['tidak_memuaskan'])
aturan5 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['tidak_memuaskan'])
aturan6 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan'])
aturan7 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['tidak_memuaskan'])
aturan8 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan'])
aturan9 = ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan'])
aturan10 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
aturan11 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan'])
aturan12 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat_memuaskan'])
aturan13 = ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat_memuaskan'])
aturan14 = ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['kurang_memuaskan'])
aturan15 = ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan'])

# Deklarasi Control System dan Simulasi
engine = ctrl.ControlSystem([aturan1, aturan2, aturan3, aturan4, aturan5, aturan6, aturan7, aturan8, aturan9, aturan10, aturan11, aturan12, aturan13, aturan14, aturan15])
system = ctrl.ControlSystemSimulation(engine)

# Simulasi Perhitungan
system.input['kejelasan_informasi'] = 80
system.input['kejelasan_persyaratan'] = 60
system.input['kemampuan_petugas'] = 50
system.input['ketersediaan_sarpras'] = 90
system.compute()

print(f"Nilai Tingkat Kepuasan Pelayanan: {system.output['kepuasan_pelayanan']:.2f}")
kepuasan.view(sim=system)
