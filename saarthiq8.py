d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}


for k in d1:
    if k in d2:
        d2[k] = d2[k] + d1[k]
    else:
        d2[k] = d1[k]

print(d2)
