n = int(input())
fact = 1
cnt = 0 
for i in range(1,n+1):
    fact *= i
for i in range(1,len(str(fact))):
    if str(fact)[-i]=="0":
        cnt +=1
    else:
        break
print(cnt)