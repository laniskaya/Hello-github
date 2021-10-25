"""Два игрока по очереди делают ход: вводят "0" и "х" в сектор поля (в данном случае 3*3)
в формате n - номер строки, m - номер столбца. Пересечением двух коодинат будет являться 
"клетка" игрового поля.
По умолчанию первый "нечетный" ход делает "х", следовательно "четный" ход достается "0"  
 Игра имеет три исхода:
  Побеждает "х"
  Побеждает "0"
  Ничья
Условия победы - совпадение комбинаций "х х х" или "0 0 0" по горизонтали, вертикали, 
диагонали
Условия ничьей - сделано 9 ходов, заполнены все клетки, нет искомых совпадений.

"""
def hello():
    print(" *********************************** ")
    print(f" |               ИГРА             | ")
    print(f" |         КРЕСТИКИ-НОЛИКИ        | ")
    print(f" |                                | ")
    print(f" ********************************** ")
    print(f" ---------------------------------- ")
    print(f" | Образец ввода координат: n, m  | ")
    print(f" |     n - первая координата      | ")
    print(f" |     m - вторая координата      | ")
    print(f" ---------------------------------- ")



field = []
for i in range(3):
    field.append([" "] * 3) # создаем пустой двухмерный список
    
def create_field():
    """The function draws a playing field 3*3"""
    print()
    print("    0   1   2    ")
    print("  -------------")
    for i, j in enumerate(field):
        j_str = " | ".join(j)
        print(f"{i} | {j_str} |  ")
        print("  -------------")
    print()




def request():
    """Функция запрашивает ввод коодинат и проверяет условия"""
  
    while True:
        
        player_move = input(f"Введите координаты : ").split()
        
        if len(player_move) != 2:
            print("Введите две координаты : ")
            continue
        
        n, m = player_move
    
        if not(n.isdigit()) or not(m.isdigit):
            print("Некорректный ввод! Введите число: ")
            continue
       
        n, m = int(n), int(m)          
        
        
        if (n < 0 or n > 2) or (m < 0 or m > 2):
            print("Диапазоны превышены")
            continue
        
        if field[n][m] != " ":
            print("Эта клетка занята! Попробуйте снова!")
            continue
       
            
        return n, m  # возрвращает кортеж из двух координат
           



def check_win():
    """ Функция сравнивает выигравшие координаты и возвращает Falsе, если 
    нет совпадения"""
    win_coords = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                  ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)), 
                  ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2))]
    for cord in win_coords:
        a, b, c = cord[0], cord[1], cord[2]
        
        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] == 'x':
            create_field()
            print(f"x Выиграл !")
            return True
           
        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] == '0':
            create_field()
            print(f"0 Выиграл !")
            return True
        
            
            
        
    return False

field = []
for i in range(3):
    field.append([" "] * 3)
    
hello()
counter = 0   # счетчик ходов
for player_move in range(1,10):
    counter += 1
    create_field()
    if counter % 2 == 1:   # нечетный ход для 'x', четный для '0'
        print("    Крестик, ваш ход!")
    else:
        print("    Нолик, ваш ход!")
    
    
    n, m = request()           # n, m = (0,0)
    
    
    if counter % 2 == 1:      # записываем в игровое поле 'x' или '0'
        field[n][m] = "x"
    else:
        field[n][m] = "0"
    
    
    if counter > 4:           # проверяем выигрышные комбинации
        call = check_win()
        if call:              # если call == True выход из цикла 
            print(f"Игра окончена!")
            break
    
    if counter == 9:          
        print("Ничья!")
        break
  