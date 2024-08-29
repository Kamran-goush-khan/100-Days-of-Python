programming_dictionary = {"Bug": "an error in the program that prevents the program from running as expected",
                          "Function": "A piece of code that you can easily call over and over again",
                          "Loop": "The action of doing something over and over again"}

# print(programming_dictionary["Bug"])
# print(programming_dictionary)
empty_dictionary = {}

# wiping an existing dictionary
# programming_dictionary = {}

# Editing an item in dictionary
# print(programming_dictionary["Function"])
# programming_dictionary["Function"] = "Recursive function"
# print(programming_dictionary["Function"])

# Loop through dictionary
# for key in programming_dictionary :
#     print(key + " : " + programming_dictionary[key])


# nesting_name_score_dictionary= {
#     "abc" : {
#         "Math" : 98,
#         "Science" : 97,
#         "English" : 93
#     },
#     "xyz" : {
#         "Math" : 95,
#         "Science" : 94,
#         "English" : 96
#     }
# }
#
# for name in nesting_name_score_dictionary :
#     for score in nesting_name_score_dictionary[name] :
#         print(name + " -> " + score + " -> " + str(nesting_name_score_dictionary[name][score]) )

# TRAVEL LOG EXERCISE
# travel_log = {
#     "France" : ["Paris", "Lille", "Dijon"],
#     "Germany" : ["Stuttgart", "Berlin"],
# }
#
# print(travel_log["France"][1])

# for key in travel_log :
#     for i in range(0, len(travel_log[key])) :
#         print(travel_log[key][i])

# nested_list = ["A", "B", ["C", "D"]]
#
# print(nested_list[2][1])

travel_log = {
    "France" : {
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visits" : 12,
    },
    "Germany" : {
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits" : 5
    },
}

print(travel_log["Germany"]["cities_visited"][2])

