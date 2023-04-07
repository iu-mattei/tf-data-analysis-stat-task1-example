import pandas as pd
import numpy as np


chat_id = 253630223 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x = (x / len(x)) / 10 # каждое значение делим на константу
    return x.mean() # возвращаем их среднее
