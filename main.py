# numbers = [1,2,3]
# doubled = [num+1 for num in numbers]

# name = "joelle"
# list_letters = [letter for letter in name]
# # print(list_letters)

# # range does first number to one before last number
# doubled = [num*2 for num in range(1,5)]
# print(doubled)

# # conditional list comprehension: only perform code IF test passes
# # new_list = [new_item for item in list if test]
# names = ["alex", "beth", "caroline", "dave", "eleanor", "freddie"]
# short_names = [name for name in names if (len(name) < 5)]
# print(short_names)
# long_names = [name.upper() for name in names if (len(name) > 5)]
# print(long_names)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared = [pow(num,2) for num in numbers]
# print(squared)
# result = [num**2 for num in numbers if num%2 == 0]
# print(result)

# import random
# # create new dictionary, loop through list
# names = ["alex", "beth", "caroline", "dave", "eleanor", "freddie"]
# student_scores = {student:random.randint(1,100) for student in names}
# print(student_scores)

# # create new dictionary from a dictionary, loop through values and keys
# passed_students = {student:score for (student,score) in student_scores.items() if score>50}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word) for word in sentence.split()}
# print(result)
# # cnat do this: result = {word:len(word) for word in sentence_list}
# # because that is all one string and will separate by characters

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # (day,temp) is in () because it is a tuple 
# weather_f = {day:temp*9/5+32 for (day,temp) in weather_c.items()}
# print(type(weather_c))
# print(type(weather_c.items()))
# print(weather_c.items())
# print(weather_f)

import pandas

student_dict = {
  "student": ["angela", "james", "lily"],
  "score": [56, 76, 98],
}
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# # not super useful because loops through columns
# for (key,value) in student_data_frame.items():
#   print(key)
#   print(value)

# lopo through rows of a dataframe instead of by column
for (index, row) in student_data_frame.iterrows():
  print(row)
# each row is a panda series object, so you can go into a row and get value in a column
  if row.student == "angela":
    print(row.score)
