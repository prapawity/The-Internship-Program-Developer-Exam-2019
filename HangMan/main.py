""" This is The Internship Program Developer Exam 2019 """
import ast,random,math
def selectCatagory():
    """ This Function for Select catagory """
    print('-------------------------------------------------\nPlease select number for choose catagory :\n\
        1. Team football in Premiere League England\n\
        2. Character in Marvel Cinematic Universe ( MCU )\n\
        3. Who is he in football world?\n\
        4. Famous Hollywood actor/actress\n\
        5. What is this country?')
    while True:
        print("Select catagory ( Interger 1 - 5): ",end="")
        cat = input()
        if(cat.isdigit() and 1<=int(cat)<=5):
            break
        else: print("\n-- Please input by number ( 1 - 5 ) --\n")
    return int(cat)

def getCatagoty(index):
    """ Function get Catagory """
    print("Selected : ",end="")
    if(index==1):
        file = open("catagory/england.json",'r')
        print("- Team football in Premiere League England -")
    elif(index==2):
        file = open("catagory/mcu.json",'r')
        print("- Character in Marvel Cinematic Universe ( MCU ) -")
    elif(index==3):
        file = open("catagory/football.json",'r')
        print("- Who is he in football world? -")
    elif(index==4):
        file = open("catagory/hollywood.json",'r')
        print("- Famous Hollywood actor/actress -")
    elif(index==5):
        file = open("catagory/country.json",'r')
        print("- What is this country? -")
    print("--------------------------------------------------")
    question = file.read()
    question = ast.literal_eval(question)
    question = decodeAnswer(question)
    return question

def decodeAnswer(decode):
    """ decode of question """
    state = 0
    for i in decode:
        sentense = ""
        rad = [1,3,5,7,9]
        for j in range(len(i)):
            if(j%2==0 and i[j] != " "):
                sentense += chr(ord(i[j])-rad[j%4])
            else:
                sentense += i[j]
        decode[state] = sentense
        state += 1
    return decode
def randomQuestion(question,index):
    """ random Question """
    number_random = random.randint(0,len(question)-1)
    hint = gethint(index)

    return question[number_random],hint[number_random]

def gethint(index):
    """ Hint Function """
    if(index==1): return ["The invisible", "Roman Abramovich", "Red Deveil", "The Sky Blues", "The Miracle of Istanbul", "Chicken in London"]

    elif(index==2): 
        return ["Millionaires", "I AM .....", "Vibranium", "Snap", "King", "Original by Tobey Maguire", "You are not god of Hammer",\
        "no trick","quantum realm","The Strongest Hero in Universe", "black suit","Ronin"]

    elif(index==3): 
        return ["PFA 2014-2015", "2019 Barcelona Captain", "Fergy's Son", "God of Goalkeeper", "Creator Free-Kick", "The Slip Effect", \
        "The peace man in Ivory Coast", "England's Striker at this time","Messi in Thailand","comeback to Thailand", "The last wall","Dortmund",\
        '2019 Chelsea Captain',"Secret"]
        
    elif(index==4):
        return ["Sherlock Holmes and Iron Man", "Agent H and Captain Mitch Nelson", "The Wasp and Tauriel in The Hobbit",\
         "Nathan Drake amd Peter Parker", "Mother F*cker", "Donjon and Lucy", "Spoil Man and Big guy", "Mission Impossible",\
         "comeback to Thailand", "The last wall","Dortmund",'Agent J and Deadshot']
        
    elif(index==5): 
        return ["The capital name is Bangkok", "Statue of Liberty", "Country of Beer", "PISA", "The Metador", "Queen Elizabeth"]
        
def defineQuestion(question,hint):
    """ make question """
    sentense = ""
    print("Question : ",end="")
    for i in question:
        if(97<=ord(i)<=122 or 65<=ord(i)<=90):
            print("_",end="")
            sentense += "_"
        else: 
            print(i,end="") 
            sentense += i
    print('\nHint : " %s "'%(hint))
    return sentense

def gameStart(question,hint,ans_now):
    """ loop game """
    point = 0
    wrong_point = 5
    print("%s   score: %d, remaining wrong guess: %d" %(ans_now,point,wrong_point))
    while(True):
        if(wrong_point == 0 or point == 100): break
        print("Input a Character : ",end="")
        cases = input().strip(" ")
        if(len(cases) != 1):
            print("-- Please input only 1 Character --")
            continue 
        elif(cases.isalpha()==False or ord(cases) > 122 or ord(cases) < 65):
            print("-- Please input by Character --")
            continue
        elif(cases.lower() in ans_now.lower()):
            print(" This Character is in Answer")
        elif(cases[0].lower() not in question and cases[0].upper() not in question):
            wrong_point -= 1
            point -= 5
            print("Question: %s   score: %d, remaining wrong guess: %d , Wrong guessed: %s" %(ans_now,point,wrong_point,cases)) if(point>=0) else print("Question: %s   score: %d, remaining wrong guess: %d , Wrong guessed: %s" %(ans_now,0,wrong_point,cases))
            if(wrong_point <3): print('\nHint : " %s "'%(hint))

        else:
            sentense = ""
            for i in range(len(question)):
                if(question[i].lower() == cases.lower()):
                    sentense += question[i]
                    point += 100/(len(question.replace(" ", "")))
                else: sentense += ans_now[i]
            ans_now = sentense
            print("Question: %s   score: %d, remaining wrong guess: %d" %(ans_now,math.ceil(point),wrong_point)) if(point<=100) else print("Question: %s   score: %d, remaining wrong guess: %d" %(ans_now,point,wrong_point))
        drawPic(wrong_point) if wrong_point != 5 else 0
        if(ans_now==question): return point,wrong_point
        elif(wrong_point==0): return point,0
def drawPic(wrong_point):
    """ Draw HangMan """
    print(" |-------------------")
    print(" |") if(wrong_point > 4) else print(" |                  |")
    print(" |") if(wrong_point > 3) else print(" |                  O")
    print(" |") if(wrong_point > 2) else print(" |                 /|\\")
    print(" |") if(wrong_point > 1) else print(" |                  |")
    print(" |") if(wrong_point > 0) else print(" |                 / \\")
    print(" |") if(wrong_point > 0) else print(" |                ARGHAA!")
    print(" |")
    print(" |")
    print("/ \\")
    print("--------------------------------------------------")
def printAnswer(point,wrong_point):
    """ print the answer """
    if(point<0):point=0
    if(wrong_point==0):
        print("-- You Lose, Try Again for beat your limit --")
    else: print("\n**** congratulation you pass this question your score is : %d ****\n" %(math.ceil(point))) if(point <= 100) else print("\n**** congratulation you pass this question your score is : %d ****\n" %(point))

def main():
    """ This is Main Function """
    index = selectCatagory()
    question = getCatagoty(index)
    question,hint = randomQuestion(question,index)
    ans_now = defineQuestion(question,hint)
    point,wrong_point = gameStart(question,hint,ans_now)
    printAnswer(point,wrong_point)

def homePage():
    """ home page """
    game_on = True
    while (game_on):
        main()
        while (game_on):
            print("Play Again ?  (y/n) : ", end="")
            ans = input()
            if(ans.lower() == 'y'):
                break
            elif(ans.lower() == 'n'):
                game_on = False
                break
homePage()








