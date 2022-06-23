no = int(input("Enter Number : "))

ans = 1
for i in range(no,0,-1):
    ans = ans* i
else:
    print("Factorial :",ans)