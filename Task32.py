'''Задача 32: Определить индексы элементов массива (списка), значения 
которых принадлежат заданному диапазону (т.е. не меньше заданного минимума 
и не больше заданного максимума). Список можно задавать рандомно
На входе : [ 1, 5, 88, 100, 2, -4]
33
200
Ответ: [2, 3]'''
import os, random
os.system('cls')
def SelectionOfElemments(elements:list,min:int,max:int)->list:
    result:list=[]
    for i in range(len(elements)):
        if max>elements[i]>min:
            result.append(i)
    return result



elelement:list=[random.randint(1,15) for _ in range(random.randint(1,10))]
min=int(input('введите миниум '))
max=int(input('Введите максимум '))
print(elelement)
print(SelectionOfElemments(elelement,min,max))


    