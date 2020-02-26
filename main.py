from giati import *
from random import randint, shuffle
from time import sleep

choice = {1:"a" , 2:"b" , 3:"c"} #random metavlites
points = 0
questions = 0
input_flag = True
ls = ["a", "b", "c"]

print("EUROPEAN QUIZ") #UI
sleep(0.5)
z = input("PRESS ENTER TO CONTINUE") 
print()

country_lst = [i for i in capital_cities] #anakatema listas xwrwn kai dimiourgia listas protevouswn
shuffle(country_lst)
capital_lst = [capital_cities[i] for i in country_lst]




for i in range(20):
    temp_lst = [ capital_lst[i] , capital_lst[i-2] ,  capital_lst[i-10]] #dimiourgia pithanwn lysewn
    shuffle(temp_lst)
    temp_dc = { choice[uwu + 1] : temp_lst[uwu] for uwu in range(3)} 

    print(str(questions+1) + "." , "Which is the capital of" , country_lst[i] , "?") #i erwtisi
    for j in range(3):
        print(choice[j+1], ":" , temp_dc[ls[j]]) #dimiourgia pithanwn apantisewn
    y= input("Which is your answer?").lower() #einai case insensitive mr logisti
    
    if y in {"a","b","c"}: #elegxos sostou lathous
        if temp_dc[y] == capital_lst[i]:
            print("CORRECT")
            points += 1
            questions += 1
        else:
            print("INCORRECT")
            questions += 1
    else: #foolproof kai perimenei mexri na vrei swsto input
        print("WRONG INPUT")
        input_flag = False
        while input_flag == False: #flag elegxou
            print(str(questions+1) + ".","Which is the capital of" , country_lst[i] , "?")
            for j in range(3):
                print(choice[j+1], ":" , temp_dc[ls[j]])
            y= input("Which is your answer?").lower()
            if y in {"a","b","c"}:
                input_flag = True
                if temp_dc[y] == capital_lst[i]:
                    print("CORRECT")
                    questions += 1
                    points += 1
                else:
                    print("INCORRECT")
                    questions += 1
            else:
                print("WRONG INPUT AGAIN")
    print()


print("You have" , points, "points out of" , questions)
