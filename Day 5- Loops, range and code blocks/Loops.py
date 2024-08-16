# fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]
# for fruit in fruits :
#     print(fruit)
from six import integer_types

# Program -  Sum of the score in the list

# student_score = [98, 34, 90, 57, 19, 90, 91, 83, 44, 99, 100]
# print(s(student_score))
#
# s = 0
# for score in student_score :
#     s += score
# print(s)

# Program for finding the Max element in the list
student_score = [180, 124, 165, 173, 189, 169, 146]

# 1st way
print(max(student_score))

# 2nd way
maximum = student_score[0]

for score in student_score :
    if maximum < score :
        maximum = score
print(maximum)
