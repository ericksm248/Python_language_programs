def pot(a,b):
    if(b>0):
        return a*pot(a,b-1)
    return 1

r = pot(2,5)
print(r)
