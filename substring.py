S = '123'
k=[]
le = len(S)
for j in range(le):
    for length in range(le-j):
        k.append(S[j:j+1+length])
print(k)