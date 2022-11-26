import random

s="null"
a=0
count=0
score_u=0
score_c=0
name=str(input("Enter your name: "))
print("")
print(name,"Lets play rock paper scissor")
ready=0
while ready==0:
    print("Are you ready?(y for yes / n for no)")
    ch=input()
    if ch == 'y':
        ready+=1
        while a==0:
            sr=str(input("What is your call (\"Rock\", \"Paper\" or \"Scissor\" ?): "))
            count+=1
            print("")
            if(sr=="Rock" or sr=="rock" or sr=="Paper" or sr=="paper" or sr=="Scissor" or sr=="scissor"):
                i=random.randint(0,2)
                if i==0:
                    s="Rock"
                    print(name+"'s call = "+sr+"\nCPU call = "+s )
                    print("")
                elif i==1:
                    s="Paper"
                    print(name+"'s call = "+sr+"\nCPU call = "+s )
                    print("")
                elif i==2:
                    s="Scissor"
                    print(name+"'s call = "+sr+"\nCPU call = "+s )
                    print("")        
                if sr.lower()=="rock" and s.lower()=="rock":
                    print("Match Drawn")
                    print("")
                elif sr.lower()=="rock" and s.lower()=="paper":
                    print("CPU Wins !!")
                    print("")
                    score_c+=1
                elif sr.lower()=="rock" and s.lower()=="scissor":
                    print(name+" wins ")
                    print("")
                    score_u+=1
                if sr.lower()=="paper" and s.lower()=="paper":
                    print("Match Drawn")
                    print("")
                elif sr.lower()=="paper" and s.lower()=="scissor":
                    print("CPU Wins !!")
                    print("")
                    score_c+=1
                elif sr.lower()=="paper" and s.lower()=="rock":
                    print(name+" wins ")
                    print("")
                    score_u+=1
                if sr.lower()=="scissor" and s.lower()=="scissor":
                    print("Match Drawn")
                    print("")
                elif sr.lower()=="scissor" and s.lower()=="rock":
                    print("CPU Wins !!")
                    print("")
                    score_c+=1
                elif sr.lower()=="scissor" and s.lower()=="paper":
                    print(name+" wins ")
                    print("")
                    score_u+=1
                play=0
                while play==0:
                    c=input("Do you wanna Play again (y for yes / n for no)\n")
                    if c=='y':
                        pass
                        play+=1
                    elif c=='n':
                        play+=1
                        a+=1
                        print("Total count: ",count,"\n")
                        # print(" ")
                        print("Your Score is: ",score_u,"\n")
                        # print("")
                        print("CPU's Score is: ",score_c,"\n")
                        # print("")
                        if score_c>score_u:
                            print("Winner is CPU")
                            print("")
                        elif score_u>score_c:
                            print("Winner is "+name)
                            print("")
                        else:
                            print("Final result is Drawn !!!")
                    else:
                        print("Please Enter a valid input")
                        print("")
            else:
                print("Please Enter a valid input ")
                print("")
    elif ch == 'n':
        print("\nOkay. See you next time")
        print("")
        ready+=1
    else:
        print("please enter a valid input\n")




