ls = list(map(int,input().split()))
asc = False
des = False
mix = False
for i in range(7):
    if ls[i] == ls[i+1]+1:
        des = True
        if asc == True:
            mix = True
            break
    elif ls[i] == ls[i+1]-1:
        asc = True
        if des == True:
            mix = True
            break
    else:
        mix = True
        break
if mix == True:
    print("mix")
elif asc == True:
    print("ascending")
else:
    print("descending")
