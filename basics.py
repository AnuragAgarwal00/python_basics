# Question 1

# using basic approach
def sum():
    total = 0
    for number in list(range (1, 11)):
            total += number
    print(total)

sum()


# QUESTION 2 DICTIONARY
# solution we cannot sort dict using sort() function
# so sorted() fuction takes iterable which is dic user
# on each user time lambad will return marks

users = {
        "1": 90,
        "2": 60,
        "4": 40,
        "5": 100
}

sorted_dic = sorted(users.items(), key=lambda kv: kv[1], reverse=True)
print(sorted_dic[0])


# QUESTION 3
list1 = [0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]
count = 0
occurrences = []
for number in list1:
    if number == 1:
        count += 1
    else: 
        count = 0
    occurrences.append(count)
print(max(occurrences))

