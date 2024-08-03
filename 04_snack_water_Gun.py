"""
-1 water
1 snack
0 Gun
"""
import random

while True:
    computer = random.choice([-1,1,0])
    me = input("Enter 1 Quit game\n\nEnter your choice : ")
    if me == "1":
        break
    else:
        st = {"w":-1,"s":1,"g":0}
        st2 = {-1:"Water",1:"Snack",0:"Gun"}
        you = st[me]
        print(f"your choice [{st2[you]}]\ncomputer choice [{st2[computer]}]")
        if computer == you:
            print("it's same choice!")
        else:
            if computer == -1 and you == 1:
                print("[you lose]")
            elif computer == -1 and you == 0:
                print("[you win]")
            elif computer == 1 and you == -1:
                print("[you lose]")
            elif computer == 1 and you == 0:
                print("[you win]")
            elif computer == 0 and you == 1:
                print("[you lose]")
            elif computer == 0 and you == -1:
                print("[you win]")