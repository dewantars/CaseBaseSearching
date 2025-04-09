import random
import math

# Fungsi yang akan diminimalkan
def fitness_function(x1, x2):
    return -(
        math.sin(x1) * math.cos(x2) * math.tan(x1 + x2) +
        (3 / 4) * math.exp(1 - math.sqrt(x1**2))
    )

# Parameter GA
POP_SIZE = 20
CHROM_LENGTH = 16  # Panjang kromosom (8 bit per variabel)
GEN_MAX = 100
P_C = 0.8
P_M = 0.1
DOMAIN = (-10, 10)

# Fungsi utilitas
def decode_chromosome(chrom):
    half = len(chrom) // 2
    x1_bin = chrom[:half]
    x2_bin = chrom[half:]
    x1 = DOMAIN[0] + int("".join(map(str, x1_bin)), 2) * (DOMAIN[1] - DOMAIN[0]) / (2**half - 1)
    x2 = DOMAIN[0] + int("".join(map(str, x2_bin)), 2) * (DOMAIN[1] - DOMAIN[0]) / (2**half - 1)
    return x1, x2

def create_population():
    return [[random.randint(0, 1) for _ in range(CHROM_LENGTH)] for _ in range(POP_SIZE)]

def calculate_fitness(pop):
    fitness = []
    for chrom in pop:
        x1, x2 = decode_chromosome(chrom)
        fitness.append(fitness_function(x1, x2))
    return fitness

def select_parents(pop, fitness):
    total_fitness = sum(fitness)
    selection_probs = [f / total_fitness for f in fitness]
    return random.choices(pop, weights=selection_probs, k=2)

def crossover(parent1, parent2):
    if random.random() < P_C:
        point = random.randint(1, CHROM_LENGTH - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    return parent1, parent2

def mutate(chrom):
    return [bit if random.random() > P_M else 1 - bit for bit in chrom]

def replace_population(pop, fitness, new_pop):
    combined = list(zip(pop, fitness)) + list(zip(new_pop, calculate_fitness(new_pop)))
    combined.sort(key=lambda x: x[1])  # Sort by fitness (ascending)
    return [chrom for chrom, _ in combined[:POP_SIZE]]

# Main GA loop
population = create_population()
for gen in range(GEN_MAX):
    fitness = calculate_fitness(population)
    new_population = []
    while len(new_population) < POP_SIZE:
        parent1, parent2 = select_parents(population, fitness)
        offspring1, offspring2 = crossover(parent1, parent2)
        new_population.append(mutate(offspring1))
        if len(new_population) < POP_SIZE:
            new_population.append(mutate(offspring2))
    population = replace_population(population, fitness, new_population)

# Output hasil terbaik
final_fitness = calculate_fitness(population)
best_chromosome = population[final_fitness.index(max(final_fitness))]
best_x1, best_x2 = decode_chromosome(best_chromosome)
print("Kromosom terbaik:", best_chromosome)
print("Nilai x1 dan x2:", best_x1, best_x2)
print("Nilai minimum fungsi:", fitness_function(best_x1, best_x2))
