ans = 0
def sum_of_num(n):
    if n==1:
        return 1
    else:
        ans = n + sum_of_num(n-1)
        return ans

num = int(input("Enter number : "))

print(sum_of_num(num))