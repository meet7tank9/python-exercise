lst=[0,1,2,3,4,5,6,7,8]
ptrn = 0

def pattern():
    for i in range(0,9):
        if i==2 or i==5 or i==8:
            print(lst[i])
        else:
            print(lst[i], end=" ")

def check_pattern(no):
    global ptrn
    if lst[0]=='X' and lst[1]=='X' and lst[2]=='X':
        ptrn = 1
    elif lst[0]=='X' and lst[4]=='X' and lst[8]=='X':
        ptrn = 1
    elif lst[0]=='X' and lst[3]=='X' and lst[6]=='X':
        ptrn = 1
    elif lst[2]=='X' and lst[4]=='X' and lst[6]=='X':
        ptrn = 1
    elif lst[1]=='X' and lst[4]=='X' and lst[7]=='X':
        ptrn = 1
    elif lst[2]=='X' and lst[5]=='X' and lst[8]=='X':
        ptrn = 1
    elif lst[3]=='X' and lst[4]=='X' and lst[5]=='X':
        ptrn = 1
    elif lst[6]=='X' and lst[7]=='X' and lst[8]=='X':
        ptrn = 1

    elif lst[0]=='o' and lst[1]=='o' and lst[2]=='o':
        ptrn = 2
    elif lst[0]=='o' and lst[4]=='o' and lst[8]=='o':
        ptrn = 2
    elif lst[0]=='o' and lst[3]=='o' and lst[6]=='o':
        ptrn = 2
    elif lst[2]=='o' and lst[4]=='o' and lst[6]=='o':
        ptrn = 2
    elif lst[1]=='o' and lst[4]=='o' and lst[7]=='o':
        ptrn = 2
    elif lst[2]=='o' and lst[5]=='o' and lst[8]=='o':
        ptrn = 2
    elif lst[3]=='o' and lst[4]=='o' and lst[5]=='o':
        ptrn = 2
    elif lst[6]=='o' and lst[7]=='o' and lst[8]=='o':
        ptrn = 2

def winner():
    if(ptrn==1):
        print("User 1 winner")
        return 1
    elif(ptrn==2):
        print("user 2 winner")
        return 2

pattern()

for i in range(9):
    if i%2==0:
        user1=int(input("user 1 : "))

        lst[user1]='X'
        check_pattern(user1)
        res=winner()
        if res==1:
            pattern()
            break
        pattern()
    elif i%2!=0:
        user2=int(input("user 2 : "))

        lst[user2]='o'
        check_pattern(user2)
        res=winner()
        if res==2:
            pattern()
            break
        pattern()
    else:
        print("game over")