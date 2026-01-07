def r_tri(a, b, c):
    if max(a,b,c) == a:
        if a**2 == b**2 + c**2:
            print('right')
        else:
            print('wrong')
    elif max(a,b,c) == b:
        if b**2 == a**2 + c**2:
            print('right')
        else:
            print('wrong')
    else:
        if c**2 == a**2 + b**2:
            print('right')
        else:
            print('wrong')

while(1):
    a,b,c = map(int, input().split())
    if a==0 and b==0 and c==0:
        break
    else:
        r_tri(a,b,c)