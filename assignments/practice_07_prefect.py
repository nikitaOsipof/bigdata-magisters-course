# Практика 7: Оркестрация DataOps пайплайнов в Prefect
from prefect import task, flow
import polars as pl

@task
def extract():
    return pl.DataFrame({"metric": [1.2, 1.5, None, 1.3]})

@task
def validate_quality(df):
    # --- СТУДЕНТ ДОЛЖЕН НАПИСАТЬ КОД НИЖЕ ---
    # Если в колонке 'metric' есть пропуски (null), вызовите исключение ValueError
    return df

@flow(name="academic_pipeline")
def run_pipeline():
    df = extract()
    _valid_df = validate_quality(df)
    print("Пайплайн выполнен успешно.")

if __name__ == "__main__":
    run_pipeline()
