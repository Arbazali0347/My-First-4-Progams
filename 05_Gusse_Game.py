import random

computer = random.randint(1,100)
a = -1
b = 1
while (a != computer):
    a = int(input("Enter your Number: "))
    if computer > a :
        print("higher number please!")
        b += 1
    elif computer < a :
        print("Lower Number please!")
        b += 1
print(f"You Win and your Number [{computer}] and your gusse [{b}]")