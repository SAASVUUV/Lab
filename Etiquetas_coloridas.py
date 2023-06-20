R = int(input(), base=16)
G = int(input(), base=16)
B = int(input(), base=16)
red = 1
green = R//G
blue = G//B
green *= green
blue *= blue
blue *= green
s = red + blue + green
print(hex(s)[2:])
