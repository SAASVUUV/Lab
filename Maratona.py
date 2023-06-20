n, m = map(int, input().split())
p = list(map(int, input().split()))
r = 'S'
for postos in range(1, n):
    if p[postos] - p[postos-1] > m:
        r = 'N'
        break
    else:
        continue
if 42195 - p[n- 1] > m:
    r = 'N'
print(r)
