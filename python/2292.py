n = int(input())
total = 1
line = 0
if n ==1:
    print("1")
else:
    while(1):
        total += line*6
        line +=1
        if n-total <=0:
            print(line)
            break
