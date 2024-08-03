def gamecoder():
    me = input("Enter your Scrite Code: ")
    me = me.split(" ")
    code = input("Enter 1 coding\nEnter 2 dicoding\nEnter your choice : ")
    coding = True if code == "1" else False
    if (coding):
        new = []
        for word in me:
            if len(word)>=3:
                s1 = "dsf"
                s2 = "gds"
                words = s1 + word[1:] + word[0] + s2
                new.append(words)
            else:
                new.append(word[::-1])
        print(" ".join(new))
    else:
        new = []
        for word in me:
            if len(word)>=3:
                words = word[3:-3]
                worder = words[-1] + words[:-1]
                new.append(worder)
            else:
                new.append(word[::-1])
        print(" ".join(new))
while True:
    gamecoder()
