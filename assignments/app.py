# Практика 8: Готовая рабочая визуализация в Streamlit
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

st.set_page_config(page_title="Research Hub", layout="wide")

st.title("📊 Интерактивный модуль диссертационного исследования")
st.markdown("### Анализ динамики изменения плотности апостериорной вероятности (Практика 8)")

st.sidebar.header("Параметры байесовского обновления")
st.sidebar.info("Передвигайте ползунки, чтобы симулировать приток новых данных в Data Lake")

alpha_input = st.sidebar.slider("Количество успешных событий (Alpha)", min_value=1, max_value=2000, value=15)
beta_input = st.sidebar.slider("Количество ложных/неудачных событий (Beta)", min_value=1, max_value=2000, value=85)

expected_value = alpha_input / (alpha_input + beta_input)
ci_lower = beta.ppf(0.025, alpha_input, beta_input)
ci_upper = beta.ppf(0.975, alpha_input, beta_input)

col1, col2, col3 = st.columns(3)
col1.metric(label="Точечная оценка Параметра (Мат. ожидание)", value=f"{expected_value:.4f}")
col2.metric(label="Нижняя граница 95% HDI", value=f"{ci_lower:.4f}")

col3.metric(label="Верхняя граница 95% HDI", value=f"{ci_upper:.4f}")
x_axis = np.linspace(max(0, expected_value - 0.15), min(1, expected_value + 0.15), 1000)
y_pdf = beta.pdf(x_axis, alpha_input, beta_input)
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(x_axis, y_pdf, color='#1f77b4', linewidth=2.5, label='Апостериорная плотность вероятности')
ax.fill_between(x_axis, 0, y_pdf, color='#1f77b4', alpha=0.15)
ax.axvline(expected_value, color='red', linestyle='--', label=f'Оценка: {expected_value:.4f}')
ax.set_title("Сжатие функции плотности при накоплении данных", fontsize=12)
ax.set_xlabel("Значение исследуемого параметра \theta", fontsize=10)
ax.set_ylabel("Плотность уверенности модели", fontsize=10)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend()
st.pyplot(fig)
