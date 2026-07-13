import numpy as np
from scipy.stats import beta # noqa: F401

TRUE_THETA = 0.035  
CHUNK_SIZE = 100000
STEPS = 50

alpha_post = 1
beta_post = 1

print("Запуск инкрементального байесовского анализа...")
for step in range(STEPS):
    stream_data = np.random.binomial(1, TRUE_THETA, CHUNK_SIZE)
    
    # --- СТУДЕНТ ДОЛЖЕН НАПИСАТЬ КОД НИЖЕ ---
    successes = 0 
    failures = 0
    alpha_post += 0
    beta_post += 0
    ci_low = 0.0
    ci_high = 0.0
    
    if (step + 1) % 10 == 0:
        mean_est = alpha_post / (alpha_post + beta_post)
        print(f"Шаг {step+1}: Оценка θ = {mean_est:.5f} | Интервал: [{ci_low:.5f} - {ci_high:.5f}]")
