#Write your function here
def larger_sum(lst1, lst2):
    sum1=0
    sum2=0
    for x in lst1:
        sum1+=x
    for y in lst2:
        sum2+=x
    if sum2>sum1:
        return lst2
    else:
        return lst1
#Uncomment the line below when your function is done
#print(larger_sum([1, 9, 5], [2, 3, 7]))