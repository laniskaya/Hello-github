import numpy as np


def game_core_v3(number):
    number = np.random.randint(1,101)
    count = 1
    min = 1
    max = 100
    predict = (min + max) // 2
    while min <= max and number != predict:
        if number > predict:
            min = predict + 1
            predict = (min + max) // 2
        elif number < predict:
            max = predict - 1
            predict = (min + max) // 2 
        count+=1

    return count
    
    
def score_game(game_core):
    count_ls = []
    np.random.seed(0)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score
	
score_game(game_core_v3)