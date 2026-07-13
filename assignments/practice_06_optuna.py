import optuna

def heavy_academic_function(x: float, y: float) -> float: # Добавлены типы float
    return (x - 3.14)**2 + (y - 2.71)**2

# Обязательно указываем тип trial: optuna.Trial и возвращаемое значение -> float
def objective(trial: optuna.Trial) -> float: 
    x: float = 0.0 
    y: float = 0.0
    return heavy_academic_function(x, y)

study = optuna.create_study(direction="minimize")
print("Шаблон Optuna готов.")
