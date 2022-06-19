'''#sum of the digit
res = 0
x = 123
for i in range(3):
    rem = x%10
    x = x//10
    res = res+rem
'''
# reverse the digit
res = 0
x = 123

for i in range(3):
    rem = x%10
    x = x//10
    res = res*10+rem

print(res)
