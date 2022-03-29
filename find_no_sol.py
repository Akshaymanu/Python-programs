#  Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700

n1 = []
for s in range (1500,2700):
    if (s&7==0) and (s%5==0):
        n1.append(str(s))

print(",".join(n1))

