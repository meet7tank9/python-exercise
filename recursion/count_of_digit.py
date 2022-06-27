num = int(input("Enter Number : "))

def total_digit(no):
    if no==0:
        return 0
    else:
        ans = 1+total_digit(no//10)
        return ans
        
print(total_digit(num))