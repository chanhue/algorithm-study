while(1):
    n = input()
    if n == "0":
        break
    elif len(n)==1:
        print("yes")
    for i in range(len(n)//2):
        if n[i]!=n[-(i+1)]:
            print("no")
            break
        if i == len(n)//2 -1:
            print("yes")
        