import random
import math

# Fungsi target
def fungsi_target(x1, x2):
    return -(
        math.sin(x1) * math.cos(x2) * math.tan(x1 + x2) + (3 / 4) * math.exp(1 - math.sqrt(x1**2))
    )

# Parameter GA
populasi_size = 20
batas_x1 = [-10, 10]
batas_x2 = [-10, 10]
jumlah_generasi = 100
mutasi_rate = 0.1

def inisialisasi_populasi():
    return [
        {
            "x1": random.uniform(batas_x1[0], batas_x1[1]),
            "x2": random.uniform(batas_x2[0], batas_x2[1]),
        }
        for _ in range(populasi_size)
    ]

def hitung_fitness(kromosom):
    x1, x2 = kromosom["x1"], kromosom["x2"]
    return -fungsi_target(x1, x2)  # Maksimasi fitness -> minimasi fungsi target

def seleksi_orangtua(populasi, fitness):
    total_fitness = sum(fitness)
    probabilitas = [f / total_fitness for f in fitness]
    terpilih = random.choices(populasi, weights=probabilitas, k=2)
    return terpilih

def crossover(ortu1, ortu2):
    alpha = random.random()
    anak1 = {
        "x1": alpha * ortu1["x1"] + (1 - alpha) * ortu2["x1"],
        "x2": alpha * ortu1["x2"] + (1 - alpha) * ortu2["x2"],
    }
    anak2 = {
        "x1": alpha * ortu2["x1"] + (1 - alpha) * ortu1["x1"],
        "x2": alpha * ortu2["x2"] + (1 - alpha) * ortu1["x2"],
    }
    return anak1, anak2

def mutasi(kromosom):
    if random.random() < mutasi_rate:
        kromosom["x1"] = random.uniform(batas_x1[0], batas_x1[1])
    if random.random() < mutasi_rate:
        kromosom["x2"] = random.uniform(batas_x2[0], batas_x2[1])
    return kromosom

def generasi_baru(populasi):
    fitness = [hitung_fitness(kromosom) for kromosom in populasi]
    populasi_baru = []
    while len(populasi_baru) < populasi_size:
        ortu1, ortu2 = seleksi_orangtua(populasi, fitness)
        anak1, anak2 = crossover(ortu1, ortu2)
        populasi_baru.append(mutasi(anak1))
        if len(populasi_baru) < populasi_size:
            populasi_baru.append(mutasi(anak2))
    return populasi_baru

def ga_minimization():
    populasi = inisialisasi_populasi()
    generasi_terbaik = None
    fitness_terbaik = float('-inf')

    for generasi in range(jumlah_generasi):
        populasi = generasi_baru(populasi)
        # Cari kromosom terbaik di generasi ini
        fitness = [hitung_fitness(kromosom) for kromosom in populasi]
        terbaik = populasi[fitness.index(max(fitness))]
        print(f"Generasi {generasi + 1}: x1 = {terbaik['x1']}, x2 = {terbaik['x2']}, Fitness = {max(fitness)}")
        
        if max(fitness) > fitness_terbaik:
            generasi_terbaik = (generasi + 1, terbaik, max(fitness))
            fitness_terbaik = max(fitness)
    
    # Tampilkan generasi terbaik
    print(f"\nGenerasi Terbaik: {generasi_terbaik[0]} dengan kromosom x1 = {generasi_terbaik[1]['x1']}, x2 = {generasi_terbaik[1]['x2']}, Fitness = {generasi_terbaik[2]}")
    
    # Cari kromosom terbaik setelah selesai
    fitness = [hitung_fitness(kromosom) for kromosom in populasi]
    terbaik = populasi[fitness.index(max(fitness))]
    return terbaik

# Menjalankan GA
hasil = ga_minimization()
print("\nHasil Akhir:")
print(f"x1 = {hasil['x1']}, x2 = {hasil['x2']}")
print(f"Nilai Minimum: {fungsi_target(hasil['x1'], hasil['x2'])}")
