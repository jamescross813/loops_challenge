#Write your function here
def add_greetings(names):
    lst = []
    for x in names:
        lst.append('Hello, '+x)
    return lst
#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))