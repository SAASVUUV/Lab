x0a, y0a, x1a, y1a = map(int, input().split())
x0b, y0b, x1b, y1b = map(int, input().split())
if x1a >= x0b and y1a >= y0b and x0a <= x1b and y0a <= y1b:
    print(1)
else:
    print(0)
