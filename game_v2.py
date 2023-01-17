'''Игра Угадай число 2
компьютер сам загадывает и сам угадывает число
'''

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток
    """
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) # предполагаемoе число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)
   
        
def score_game(random_predict) -> int:
    """За какое среднее количество попыток в среднем за 1000 проходов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # фиксируем сид (seed) для воспроизовдимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список из 1000 чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Алгоритм угадывает числов в среднем за: {score} попыток.')
    return(score)
    
if __name__ == '__mine__':
    # RUN
    score_game(random_predict)
