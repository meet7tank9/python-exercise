no=[12,75,150,180,145,525,50]

for i in no:
    if i%5==0:
        if i>150:
            continue
        elif i> 500:
            break
        else:
            print(i)