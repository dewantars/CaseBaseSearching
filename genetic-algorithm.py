import matematic.math as math # Mengimpor modul matematic.math sebagai math

# Fungsi untuk mendekode nilai biner ke nilai real
def decode(binary_str, a=-10, b=10, n=10):
    return a + (int(binary_str, 2) / (2**n - 1)) * (b - a)

# Fungsi objektif untuk mengevaluasi kualitas kromosom
def fungsi_target(x1, x2):
    return -(
        (math.sin(x1) * math.cos(x2) * math.tan(x1 + x2) + (3 / 4) * math.exp(1 - math.sqrt(x1**2)))
    )

# Fungsi untuk menghitung nilai fitness
def cariFitness(total, objektif):
    return objektif / total

# Seleksi deterministik menggunakan roulette wheel dengan ambang tertentu
def deterministic_selection(data, thresholds):
    selected = []
    for t in thresholds:
        for item in data:
            lower, upper = item["Interval"]
            if lower <= t <= upper:
                selected.append(item["Kromosom"])
                break
    return selected

# Fungsi untuk melakukan crossover deterministik pada dua parent
def deterministic_crossover(parent1, parent2, point):
    return (
        parent1[:point] + parent2[point:],  # Child 1
        parent2[:point] + parent1[point:],  # Child 2
    )

# Fungsi untuk melakukan mutasi deterministik pada kromosom
def deterministic_mutate(kromosom, positions):
    kromosom = list(kromosom)
    for pos in positions:
        kromosom[pos] = '1' if kromosom[pos] == '0' else '0'
    return ''.join(kromosom)

# Fungsi untuk mengevaluasi seluruh populasi
def evaluate_population(population):
    data = []
    total_obj = 0
    for kromosom in population:
        x1 = round(decode(kromosom[:10]), 3)
        x2 = round(decode(kromosom[10:]), 3)
        f_obj = round(fungsi_target(x1, x2), 3)
        total_obj += f_obj
        data.append({"Kromosom": kromosom, "x1": x1, "x2": x2, "Fungsi Objektif": f_obj})
    
    cumulative = 0
    for item in data:
        fitness = round(cariFitness(total_obj, item["Fungsi Objektif"]), 3)
        cumulative += fitness
        item["Fitness"] = fitness
        item["Cumulative"] = round(cumulative, 3)
        item["Interval"] = (round(cumulative - fitness, 3), round(cumulative, 3))
    
    return data, total_obj

# Inisialisasi populasi 
population = [
    "01110100011000110101",
    "11100111000101101010",
    "10111010101001011111",
    "10000000001000000000",
]

# Loop algoritma genetika
best_kromosom = None
best_fitness = -float("inf")
best_generation = -1
for generation in range(20):
    print()
    print(f"Generation {generation + 1}")

    # Evaluasi populasi saat ini
    data, total_obj = evaluate_population(population)

    # Menampilkan tabel evaluasi populasi
    print("{:<4}{:<22}{:>10}{:>10}{:>15}{:>10}{:>15}{:>20}".format(
        "No.", "Kromosom", "x1", "x2", "F(x1,x2)", "Fitness", "Cumulative", "Interval"
    ))
    for i, item in enumerate(data, start=1):
        print("{:<4}{:<22}{:>10.3f}{:>10.3f}{:>15.3f}{:>10.3f}{:>15.3f}{:>20}".format(
        i, item['Kromosom'], item['x1'], item['x2'],
        item['Fungsi Objektif'], item['Fitness'],
        item['Cumulative'], str(item['Interval'])
    ))

    # Seleksi deterministik menggunakan threshold tetap
    selected = deterministic_selection(data, [0.162, 0.582]) 

    # Crossover deterministik pada kromosom yang terpilih
    crossover_point = 2
    child1, child2 = deterministic_crossover(selected[0], selected[1], crossover_point)

    # Mutasi deterministik pada anak yang dihasilkan (posisi tetap)
    mutation_positions_1 = [4, 9]  # child 1
    mutation_positions_2 = [4, 10]  # child 2
    child1 = deterministic_mutate(child1, mutation_positions_1)
    child2 = deterministic_mutate(child2, mutation_positions_2)

    # Perbarui populasi dengan anak yang baru
    population = [child1, child2]

    # Memeriksa solusi terbaik
    for item in evaluate_population(population)[0]:
        if item["Fitness"] > best_fitness:
            best_kromosom = item["Kromosom"]
            best_fitness = item["Fitness"]
            best_generation = generation + 1

# Dekode kromosom terbaik
best_x1 = round(decode(best_kromosom[:10]), 3)
best_x2 = round(decode(best_kromosom[10:]), 3)

# Output hasil akhir
print("\nKromosom Terbaik:", best_kromosom)
print(f"Nilai Fitness: {best_fitness}")
print(f"Decode nilai: x1 = {best_x1}, x2 = {best_x2}")
print(f"Ditemukan pada Generasi ke-{best_generation}")