'''
def multipliers():
    return [lambda x: i * x for i in range(4)]
    #return [i for i in range(4)]
#print(multipliers())
print([m(1) for m in multipliers()])
'''

#斐波那契数列
a,b = 0, 1
while b:
    print(b)
    a, b = b, a + b
