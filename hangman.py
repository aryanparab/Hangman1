import random
names=['MUMBAI',"FRANCE",'ROME','NEW YORK']
quit=False

def showdisplay(display,lives):
    for i in display:
        print(i,end='  ')
    print('lives:' ,lives)
def getcountry():
    n=random.randrange(0,len(names))
    return names[n]
def check(display,country):
    for i in range(len(country)):
        if display[i]!=country[i]:
            return False

    else:
        return True
def guess(display,lives,country,l):
    yes = True

    inp=input().upper()
    for i in range(len(display)):
        if inp==country[i]:
            display[i]=inp
            yes=False
    if yes==True:
        lives[0] -= 1

    showdisplay(display,lives[0])
    if check(display,country)==True :
        return True
    elif lives[0]==0:
        l[0]=0
        return True
    else:
        return False


def playgame():
    country=getcountry()
    l=[len(country)]
    lives = [5]

    display=[]
    for i in range(len(country)):
        if country[i]!=' ':
            display.append("_")
        else:
            display.append(' ')
    showdisplay(display,lives[0])
    ans=False
    while ans==False :

         ans=guess(display,lives,country,l)

    if l[0]==0:
        print('You Lost....The word Was : ' , country)
    else:
        print('You Win')

while quit==False:
    inp=input('Enter to play or q to quit')

    if inp=='q':
        quit=True
    else:
        playgame()



