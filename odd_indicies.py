#Write your function here
def odd_indices(lst):
    new_lst =[]
    index = 0
    for x in lst:
        if index %2 != 0:
            new_lst.append(x)
        index +=1
    return new_lst

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))