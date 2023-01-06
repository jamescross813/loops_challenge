#Write your function here
def exponents(bases, powers):
    newlst = []
    for base in bases:
        for power in powers:
            newlst.append(base ** power)
    return newlst

#Uncomment the line below when your function is done
#print(exponents([2, 3, 4], [1, 2, 3]))