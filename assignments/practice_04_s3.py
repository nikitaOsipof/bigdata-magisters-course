import duckdb

con = duckdb.connect(database=":memory:")

# --- СТУДЕНТ ДОЛЖЕН НАПИСАТЬ КОД НИЖЕ ---
# 1. Установите и загрузите плагин 'httpfs' в DuckDB.
# 2. Настройте конфигурационные параметры подключения к локальному S3-хранилищу (Silo/MinIO):
#    endpoint: localhost:9000, user: admin, password: SuperSecretPassword123, ssl: false.
# 3. Напишите SQL-запрос, считывающий партиционированные Parquet-файлы напрямую из S3.

print("Скрипт Практики 4 загружен. Настройте S3-подключение.")
