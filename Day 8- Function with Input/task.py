# def greet(name) :
#     print(f"Hello, {name}")
#     print(f"How are you? {name}")
#     print(f"Hey {name} Isn't the weather is nice?")
#
# greet("abc")
from operator import truediv

from numpy.core.defchararray import lower


# total_weeks = 90 * 52
# def life_in_weeks(age) :
#     week_live = age * 52
#     return total_weeks - week_live
#
# real_age = int(input())
#
# x = life_in_weeks(real_age)
#
# print(f"You have {x} weeks left.")

# Function with two parameter
# def greet_with(name, location) :
#     print(f"Hello, {name}")
#     print(f"Do you visit {location}?")
#
# greet_with("Kamran", "Satna")
# greet_with("Satna", "Kamran")
# greet_with(location="Satna", name="Kamran")

def calculate_love_score(name1, name2) :
    word1 = "true"
    word2 = "love"
    score1 = 0
    score2 = 0

    for i in range(0, len(word1)) :
        for j in range(0, len(name1)) :
            if word1[i] == name1[j].lower() :
                score1 += 1
        for k in range(0, len(name2)) :
            if word1[i] == name2[k].lower() :
                score1 += 1

    for i in range(0, len(word2)) :
        for j in range(0, len(name1)) :
            if word2[i] == name1[j].lower() :
                score2 += 1
        for k in range(0, len(name2)) :
            if word2[i] == name2[k].lower() :
                score2 += 1

    ans = str(score1) + str(score2)
    print(ans)

calculate_love_score("", "")