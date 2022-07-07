#creation of digital watch
from time import sleep
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
secCount,minCount,hrCount,dayCount,monthCount,yrCount= 0,0,0,0,0,0
while hrCount!=24:
    for i in range(0,60,1):
        sleep(1)
        clear()
        print('Hour:',hrCount,' Minut:',minCount,' Sec:',i,end='')
        if i == 59:
            minCount += 1
            if minCount==60:
                hrCount +=1
                minCount =0
                if hrCount == 24:
                    dayCount += 1
                    hrCount = 0
                    if dayCount ==31:
                        monthCount +=1
                        dayCount =0
                        if monthCount ==12:
                            yrCount +=1
                            monthCount = 0
