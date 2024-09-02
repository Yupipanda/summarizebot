from news.ixbt import ixbtparse
from news.rprivacy import parserprivacy
from news.hknews import parse_hknews
from news.techcrunch import parsetech
from news.habr import parsehabr
import random

'''
функция generate_numbers принимает два аргумента:
В итоге вы даете сумму и количество элементов в массиве, функция на выходе дает вам список чисел такой длины, которую вы указали в num_count, и сумма этих чисел будет равна target_sum.
Причем каждый раз эти числа всегда будут рандомными, и величина каждого числа распределяется тоже рандомным образом.
'''
def generate_numbers(target_sum, num_count):
    target_sum = int(target_sum)
    if target_sum < num_count:
        raise ValueError("Сумма должна быть не менее количества чисел")

    numbers = []
    remaining_sum = target_sum

    for i in range(num_count - 1):
        num = random.randint(1, remaining_sum - (num_count - i - 1))
        numbers.append(num)
        remaining_sum -= num
    numbers.append(remaining_sum)  
    random.shuffle(numbers) 
    return numbers

'''
runews -- функция получает массив чисел и потом запускает парсеры и добавляет запрошенное количество постов в базу данных.
'''
async def runews(limit):
    sl = generate_numbers(limit, 5)
    parse_hknews(sl[0])
    parserprivacy(sl[1])
    parsetech(sl[2])
    parsehabr(sl[3])
    ixbtparse(sl[4])

