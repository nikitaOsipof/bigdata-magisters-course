# Практика 5: Инкрементальное мультиноминальное распределение Дирихле
import numpy as np

TRUE_PROPORTIONS: list[float] = [0.60, 0.25, 0.10, 0.04, 0.01]
CATEGORIES: list[str] = ["INFO", "WARN", "ERROR", "CRITICAL", "FATAL"]
CHUNK_SIZE: int = 10000
STEPS: int = 10

alpha_vector = np.ones(len(CATEGORIES))

print("Запуск многомерного байесовского анализа...")
for step in range(STEPS):
    chunk_data = np.random.choice(CATEGORIES, size=CHUNK_SIZE, p=TRUE_PROPORTIONS)
    
    # --- СТУДЕНТ ДОЛЖЕН НАПИСАТЬ КОД НИЖЕ ---
    # 1. Посчитайте количество встреченных событий категорий в чанке без циклов.
    # 2. Обновите вектор весов alpha_vector.
    # 3. Рассчитайте ожидаемые пропорции категорий.
    
    if (step + 1) % 10 == 0:
        print(f"Шаг {step+1}: Выведите текущую оценку многомерного распределения")
