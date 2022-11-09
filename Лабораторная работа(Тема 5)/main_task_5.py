from random import sample

def get_random_password() -> str:
    symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password = (sample(symbols, 8)) # TODO написать функцию генерации случайных паролей
    return "".join(password)

print(get_random_password())
