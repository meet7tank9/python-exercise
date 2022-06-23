start = int(input("Enter Starting Value : "))
end = int(input("Enter Ending Value : "))

for no in range(start,end+1):
    for i in range(2,no):
        if no%i==0:
            break
    else:
        print(no)