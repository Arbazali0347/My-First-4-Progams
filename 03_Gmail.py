def gmailcode():
    a = 0
    b = 0
    c = 0
    me = input("Enter Your Gmail : ")
    if len(me)>=6:
        if me[0].isalpha():
            if me[-4]== ".":
                if ("@" in me )and (me.count("@")==1):
                    for i in me:
                        if i==i.isspace():
                            a = 1
                        elif i.isalpha():
                            if i==i.upper():
                                b = 1
                        elif i.isdigit():
                            continue
                        elif i == "@" or i == "." or i == "_":
                            continue
                        else:
                            c = 1
                    if a == 1 or b == 1 or c == 1:
                        print("Rong Gmail !")
                    else:
                        print("RIGHT GMAIL ARBAZ ALI")
                else:
                    print("Rong Gmail !")
            else:
                print("Rong Gmail !")
        else:
           print("Rong Gmail !") 
    else:
        print("Rong Gmail !")
while True:
    gmailcode()