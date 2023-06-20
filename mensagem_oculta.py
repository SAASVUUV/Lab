n = int(input())
while n > 0:
    f = input().split(' ')
    r = []
    for j in f:
        if j == '':
            continue    
        else:
            r.append(j[0])
    print(''.join(r))
    n -= 1
