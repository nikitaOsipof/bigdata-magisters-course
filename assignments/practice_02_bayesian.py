# Практика 2: Инкрементальное Бета-Бернулли сопряжение
import numpy as np
from scipy.stats import beta # noqa: F401

TRUE_THETA: float = 0.035  
CHUNK_SIZE: int = 10000
STEPS: int = 10

alpha_post: int = 1
beta_post: int = 1

print("Запуск инкрементального байесовского анализа...")
for step in range(STEPS):
    stream_data = np.random.binomial(1, TRUE_THETA, CHUNK_SIZE)
    
    # --- СТУДЕНТ ДОЛЖЕН НАПИСАТЬ КОД НИЖЕ ---
    # 1. Рассчитайте успехи и неудачи в stream_data БЕЗ циклов for.
    successes = 0 
    failures = 0
    # 2. Обновите параметры alpha_post и beta_post.
    alpha_post += 0
    beta_post += 0
    # 3. Рассчитайте границы 95% HDI интервала с помощью квантилей beta.ppf
    ci_low = 0.0
    ci_high = 0.0
    
    if (step + 1) % 10 == 0:
        mean_est = alpha_post / (alpha_post + beta_post)
        print(f"Шаг {step+1}: Оценка θ = {mean_est:.5f} | Интервал: [{ci_low:.5f} - {ci_high:.5f}]")
