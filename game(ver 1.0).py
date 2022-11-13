def draw_field(field: list[list]) -> None:
    """
    Отрисовка поля
    :param field: инициализаированное поле.
    :return: отрисованное игровое поле для консли.
    """
    for row in field:
        for cell in row:
            print(f"|{cell}", end="")
        print("|")


def is_win(field: list[list], size: int) -> bool:
    """
    Проверка победы X или 0 или ничейного исхода.
    :param field: инициализаированное поле.
    :param size: размер поля.
    :return: True в случае победы одного из игроков, False в случае ничейного исхода.
    """
    # горизонталь
    for row in field:
        if (row.count("X") or row.count("0")) == size:
            return True
    # вертикаль
    for col in range(size):
        vertical = [field[0][col], field[1][col], field[2][col]]
        if vertical == ["X"] * size or vertical == ["0"] * size:
            return True
    # главная диагональ
    main_diagonal = [field[0][0], field[1][1], field[2][2]]
    if main_diagonal == ["X"] * size or main_diagonal == ["0"] * size:
        return True
    # побочная диагональ
    second_diagonal = [field[0][2], field[1][1], field[2][0]]
    if second_diagonal == ["X"] * size or second_diagonal == ["0"] * size:
        return True
    return False


def check_int_val(text: str, max_val=None) -> int:
    """
    Проверка введенного значения
    :param text: диалоговый текст для игроков
    :param max_val: граница области куда можно устанавливать Х или 0
    :return: значение которок ввел игрок
    """
    while True:
        val = input(text)
        if not val.isdigit():
            print("Не число, введите число")
            continue
        else:
            val = int(val)
            if max_val is not None and not 0 <= val <= max_val - 1:
                print(f"Вышел за рамки [0, {max_val}]")
                continue
        return val


def check_player_in_fild(field: list[list], size: int) -> tuple [int, int]:
    """
    Проверка занятости ячейки
    :param field: инициализаированное поле.
    :param size: размер поля.
    :return: индекс строк/столбцов
    """
    while True:
        ind_row = check_int_val("Введи номер строки куда хотите поставить символ:\n", max_val=size)
        ind_col = check_int_val("Введи номер куда хотите поставить символ:\n", max_val=size)
        if field[ind_row][ind_col] != " ":
            print("Ячейка занята")
            continue
        return ind_row, ind_col


def game(field: list[list], player: str, size: int) -> None:
    """
    Игра
    :param field: инициализаированное поле.
    :param player: символ игрока.
    :param size: размер поля.
    :return: Игра и ее рузультат.
    """
    count = 0  # счетчик ходов
    draw_field(field)
    while count < size * size:
        ind_row, ind_col = check_player_in_fild(field, size)
        field[ind_row][ind_col] = player
        draw_field(field)
        count += 1
        if is_win(field, size):
            print(f"Выиграл {player}")
            return
        player = "X" if player == "0" else "0"
    print("Ничья")


def app():
    size = 3
    player = "X"
    field = [[" " for _ in range(size)] for _ in range(size)]
    game(field, player, size)


if __name__ == "__main__":
    print("Игра КРЕСТИКИ НОЛИКИ c полем 3х3:(пока что)")
    app()
