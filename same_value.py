#Write your function here
def same_values(lst1, lst2):
    match_list = []
    for x in lst1:
        for y in lst2:
            if x==y:
                match_list.append(y)
    return match_list
#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))