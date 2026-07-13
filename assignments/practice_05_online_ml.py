import numpy as np

TRUE_PROPORTIONS = [0.60, 0.25, 0.10, 0.04, 0.01]
CATEGORIES = ["INFO", "WARN", "ERROR", "CRITICAL", "FATAL"]
CHUNK_SIZE = 50000
STEPS = 40

alpha_vector = np.ones(len(CATEGORIES))

print("Запуск многомерного байесовского анализа...")
for step in range(STEPS):
    chunk_data = np.random.choice(CATEGORIES, size=CHUNK_SIZE, p=TRUE_PROPORTIONS)
    
    # --- СТУДЕНТ ДОЛЖЕН НАПИСАТЬ КОД НИЖЕ ---
    if (step + 1) % 10 == 0:
        print(f"Шаг {step+1}: Выведите текущую оценку многомерного распределения")
