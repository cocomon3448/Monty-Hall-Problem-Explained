#COPYRIGHT BY RAMMER3448 ALL RIGHT RESERVED

import random
from os import system

clear = lambda: system('cls')
cnt_right = 0
cnt_wrong = 0
clear()
def montihall(time):
    i = 0
    while i<time:
        global cnt_right, cnt_wrong
        lst = ["car", "2", "3"]
        pick = random.randint(0,2)
        opn = random.randint(0,2)

        while True:
            if lst[opn - 1] != lst[pick-1] and lst[opn -1] != "car":
                break
            opn = random.randint(0,2)

        lst.remove(lst[opn-1])
        lst.remove(lst[pick-1])

        if lst[0] == "car":
            cnt_right+=1
        else:
            cnt_wrong+=1
        i+=1
        if i % (time//10) == 0:
            clear()
            print("Process:", str(i) + "/" + str(time))
    print("Done!")
    print("Result:",(cnt_right/(cnt_wrong+cnt_right))*100,"\b%")
    print("More Info:", "Car =",cnt_right,"Not Car =",cnt_wrong)
    

montihall(100000) # 100000 time test
