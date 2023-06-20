n = int(input())
l = list(map(int, input().split()))
c = sum(l)/2
t = 0
r = 0

while t < c:
    d = l[r]
    t += d
    r += 1
print(r)
        
