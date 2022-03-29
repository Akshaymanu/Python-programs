num = (1,2,3,4,5,6,7,8,9,10)

even = 0
odd = 0
for x in (num):
    if not x % 2 :
        
        even += 1
    else:
        odd += 1

print("no of even numbers :",even)
print("no of odd numbers :",odd)