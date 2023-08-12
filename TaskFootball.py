'''Задача FOOTBALL необязательная.
Напишите программу, которая принимает на стандартный вход список игр футбольных команд 
с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр. После этого идет nn строк, в которых 
записаны результаты игры в следующем формате: Перваякоманда;Забитопервойкомандой;Втораякоманда;
Забитовторойкомандой/ Вывод программы необходимо оформить следующим образом: Команда:Всегоигр Побед 
Ничьих Поражений Всегоочков Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.
Пример входа:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
Выход будет:
Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6'''
import os, re
os.system('cls')
def GameStats(gameNumber:int=1,request1:str='')->list:
    return list(input(f'Матч № {i+1}. {request1} ').split(';') for i in range(gameNumber))
def TeamStats(gamesStats:list)->dict:
    teamStatsSet:set=set(map(lambda list1:list1[0],gamesStats))
    gamesStatsList:list=gamesStats
    for i in gamesStatsList:
        if int(i[1])<int(i[3]):
            i.pop(1)
            i.insert(1,[1,0,0,1,0]) #Всегоигр Побед Ничьих Поражений Всего очков 
            i.pop(3)
            i.insert(3,[1,1,0,0,3])
        elif int(i[1])==int(i[3]):
            i.pop(1)
            i.insert(1,[1,0,1,0,1]) #Всегоигр Побед Ничьих Поражений Всего очков 
            i.pop(3)
            i.insert(3,[1,0,1,0,1])
        else:
            i.pop(1)
            i.insert(1,[1,1,0,0,3]) #Всегоигр Побед Ничьих Поражений Всего очков 
            i.pop(3)
            i.insert(3,[1,0,0,1,0])
    print(gamesStatsList)
    gamesStatsDict:dict=dict()
    list4:list=[]
    for i in teamStatsSet:
        list4:list=[]
        list5:list=[]
        for j in range(len(gamesStatsList)):
            for k in range(len(gamesStatsList[j])):
                if i==gamesStatsList[j][k]:
                    list4.append(gamesStatsList[j][k+1])
        for l in range(len(list4[0])):
            temporary:int=0
            for items in list4:
                temporary+=int(items[l])
            list5.append(temporary)
        gamesStatsDict[i]=list5            
    return gamesStatsDict



request:str='Введите наименование домашней команды; количество голов забитых \
домашней командой; наименование гостевой команды; количество голов забитых гостевой командой;'
list1=GameStats(3,request)
print(*list1)
dict:dict=TeamStats(list1)
for key,value in dict.items():
    print (key,value)




    



