num = 12345

i = 0

def reverse_num(no):
    global i
    if no==0:
        return 1
    else:
        r = no%10
        i = (i *10) + r
        reverse_num(no//10)
        return i

print(reverse_num(num))