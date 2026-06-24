def log_operacion(func):
    def wrapper(*args, **kwargs):
        print(f"-- ejecutando: {func.__name__}")
        resultado = func(*args, **kwargs)
        return resultado
    return wrapper