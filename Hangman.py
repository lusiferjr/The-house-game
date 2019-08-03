import random
ans=[]
wrong=[]
word=""
def display(a):
    man = [" ___\n", "(", "o ", "o", ")\n", "  |\n", " / ","\ \n"]
    print(*man[:a],sep='')
    print(*ans)
    print("\nwrong guess:",*wrong)
    print("\n*______________________________________________________*")
    print("\n \n")


def data():
    global word
    actress=["ScarlettJohansson","EmmaWatson","JenniferLawrence","AnneHathaway","JenniferAniston"]
    word=random.choice(actress)
    b=len(word)

    a=[]
    for i in range(0,b):
        a.append(i)
    a=random.sample(a,3)

    for i in range (0,b):
        if a[0]!=i and a[1]!=i and a[2]!=i:
            ans.append("__ ")
        else:
            ans.append(word[i])
    return b

def man():
    global word
    b=data()
    choice=3
    flag=8
    while len(wrong)<8 and choice<b:
        display(flag)
        c=input("enter your guess: ")
        for i in range(0,b):
            if c==word[i].lower() and ans[i]=="__ ":
                ans[i]=word[i]
                choice+=1
                break
        else:
            flag=flag-1
            wrong.append(c)
    display(flag)
    if flag>0:
        print("yeeeepieeeeeeee!!!!!!!!!   You win")
    else:
        print("sorry ")
man()
