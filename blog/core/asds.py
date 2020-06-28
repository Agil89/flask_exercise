m =10
for i in range(10):
    for j in range(2,10,1):
        if m%2==0:
            continue
            m = m+ 1
    m +=1
else:
    m +=1
print(m)