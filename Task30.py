'''
InputIntOnRequest, ArithmeticProgression

Задача 30:  Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.'''
import os, random
os.system('cls')
def InputIntOnRequest (request:str):
    return int(input(request))
def ArithmeticProgression (firsNumber:int,difference:int,numberOfElement:int)->list:
    list1:list=[]
    for i in range(1,numberOfElement+1):
        list1.append(firsNumber+(i-1)*difference)
    return list1



firstnumber:int=InputIntOnRequest('Введите первый элемент ')
difference:int=InputIntOnRequest('Введите разность ')
numberOfElement:int=InputIntOnRequest('Введите количество элементов ')
print(ArithmeticProgression(firstnumber,difference,numberOfElement))