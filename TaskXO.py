'''Сделайте игру крестики - нолики, человек должен играть с ботом, поле 3*3.
Конечно, бот не должен ходить на занятые поля
Если есть желание, то можете наделить бота псевдоинтеллектом,чтоб он ходил как можно ближе к своим занятым клеткам
После каждого хода на экран должна выводиться текущая обстановка на поле.
Например,

|     |  Х | 
|     |  O |
|     |  O |
При ходе пользователя у надо спрашивать номер строки и столбца, куда он хочет сделать ход'''
import os, random, numpy
os.system('cls')
def EnterXY(numberMin:int=1,numberMax:int=4)->list:
    valueX:int=int(input("Введите номер строки в которую хотите потсавить Х (от 1 до 3) "))
    while numberMin>valueX>=numberMax:
        valueX=int(input("Вы ввели неверный номер. Введите номер строки в \
                                 которую хотите потсавить Х (от 1 до 3) "))
    valueY:int=int(input("Введите номер столбца в который хотите потсавить Х (от 1 до 3) "))
    while numberMin>valueY>=numberMax:
        valueY=int(input("Вы ввели неверный номер.\
                             Введите номер столбца в который хотите потсавить Х (от 1 до 3) "))
    return [valueX,valueY]    
def XO (fieldtemporary:list=[],xOr0:str='0')->list:
    field:list=fieldtemporary  
    if field==[]:
        for i in range(4):
            field.insert(i,[])
            for j in range(4):
                if i==0:
                   print(' ',end='  ')
                   field[i].insert(j,' ')
                else:
                    field[i].insert(j,' ')
                    print(' ',end=' | ')
            print()
    else:
        winCombinationX:list=[]
        winCombinationX.append(field[1][1]=='X'==field[2][2]==field[3][3])
        winCombinationX.append(field[3][1]=='X'==field[2][2]==field[1][3])
        winCombinationX.append(field[1][1]=='X'==field[2][2]==field[3][3])
        winCombinationX.append(field[1][1]=='X'==field[1][2]==field[1][3])
        winCombinationX.append(field[1][1]=='X'==field[2][1]==field[3][1])
        winCombinationX.append(field[1][2]=='X'==field[2][2]==field[3][2])
        winCombinationX.append(field[1][3]=='X'==field[2][3]==field[3][3])
        winCombinationX.append(field[2][1]=='X'==field[2][2]==field[2][3])
        winCombinationX.append(field[3][1]=='X'==field[3][2]==field[3][3])
        winCombinationX.append(field[3][1]=='X'==field[2][2]==field[1][3])
        winCombination0:list=[]
        winCombination0.append(field[1][1]=='0'==field[2][2]==field[3][3])
        winCombination0.append(field[3][1]=='0'==field[2][2]==field[1][3])
        winCombination0.append(field[1][1]=='0'==field[2][2]==field[3][3])
        winCombination0.append(field[1][1]=='0'==field[1][2]==field[1][3])
        winCombination0.append(field[1][1]=='0'==field[2][1]==field[3][1])
        winCombination0.append(field[1][2]=='0'==field[2][2]==field[3][2])
        winCombination0.append(field[1][3]=='0'==field[2][3]==field[3][3])
        winCombination0.append(field[2][1]=='0'==field[2][2]==field[2][3])
        winCombination0.append(field[3][1]=='0'==field[3][2]==field[3][3])
        winCombination0.append(field[3][1]=='0'==field[2][2]==field[1][3])
        if True in winCombinationX:
            print('Вы победили')
            return field
        elif True in winCombination0:
            print('Вы проигали')
            return field
        elif ' ' not in (field[1][1:]and field[2][1:] and field[3][1:]):
            print('Ничья')
            return field
        else:
            if xOr0=='X':
                xY:list=EnterXY(1,len(field))
                valueX:int=xY[0]
                valueY:int=xY[1]
                while field[valueX][valueY]!=' ':
                    print('На эту позицию нельзя ставить Х')
                    xY:list=EnterXY()
                    valueX:int=xY[0]
                    valueY:int=xY[1]
                field[valueX].pop(valueY) 
                field[valueX].insert(valueY,'X')
                os.system('cls')
                for i in range(4):
                    for j in range(4):
                        if i==0:
                            print(field[i][j],end='  ')
                        else:
                            print(field[i][j],end=' | ')
                    print()
                xOr0='0'
            else:
                valueX=random.randint(1,len(field)-1)
                valueY=random.randint(1,len(field)-1)
                while field[valueX][valueY]!=' ':
                    valueX=random.randint(1,len(field)-1)
                    valueY=random.randint(1,len(field)-1)
                field[valueX].pop(valueY)
                field[valueX].insert(valueY,'0')
                os.system('cls')
                for i in range(4):
                    for j in range(4):
                        if i==0:
                            print(field[i][j],end='  ')
                        else:
                            print(field[i][j],end=' | ')
                    print()
                xOr0='X'
    return XO(field,xOr0)




field5=XO()
#field5=XO(field5)



