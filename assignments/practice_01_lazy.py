# Практика 1: Ленивые вычисления в DuckDB
import duckdb
import os

csv_path = "large_research_logs.csv"
if not os.path.exists(csv_path):
    print("Генерация исходного файла для практики...")
    duckdb.sql(f"""
        CREATE TABLE temp_gen AS 
        SELECT 
            (random() * 10000)::INT as device_id,
            CASE WHEN random() > 0.5 THEN 'SUCCESS' ELSE 'ERROR' END as status,
            random() * 100 as metric_value
        FROM repeat(1, 100000); -- Снижено для быстрой проверки на сервере
        COPY temp_gen TO '{csv_path}' (HEADER, DELIMITER ',');
        DROP TABLE temp_gen;
    """)

con = duckdb.connect(database=':memory:')

# --- СТУДЕНТ ДОЛЖЕН НАПИСАТЬ КОД НИЖЕ ---
# Напишите аналитический запрос в переменную query к 'large_research_logs.csv'
# Фильтрация по status = 'ERROR', группировка по device_id, агрегаты: count(*) и avg(metric_value)
# Добавьте HAVING по количеству ошибок > 5, сортировку по убыванию и LIMIT 10.

query = """
SELECT 1 as device_id, 1 as error_count, 1.0 as avg_error_value; -- Замените своим SQL запросом
"""

print("=== ФИЗИЧЕСКИЙ ПЛАН ВЫПОЛНЕНИЯ ===")
print(con.sql(f"EXPLAIN {query}").fetchone())
print("\n=== ВЫЧИСЛЕНИЕ РЕЗУЛЬТАТА ===")
print(con.sql(query).pl())
