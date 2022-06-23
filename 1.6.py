num = int(input("Enter any number : "))

i=0
while num>0:
    num = int(num/10)
    i += 1

print(i)
