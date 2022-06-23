num = int(input("Enter Number : "))

ans = 0
while num>0:
    r = int(num%10)       
    num = int(num/10)
    ans = (ans*10) + r

print(ans)

# 123
# r=3
# num=12
# ans=3