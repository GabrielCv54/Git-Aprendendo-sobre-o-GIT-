pair=[]
odd=[]

for i in range(0,100,2):
    if i % 2 ==0:
        pair.append(i)
    else:
        odd.append(i)

print(pair)
print(odd)