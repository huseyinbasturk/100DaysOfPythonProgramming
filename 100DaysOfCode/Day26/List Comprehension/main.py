# numbers = [1,1,2,3,4,5,13,21,34,55]
#
# squared_numbers = [item*item for item in numbers ]
# print(squared_numbers)

# list_of_strings = input().split(',')
#
# numbers = [int(num) for num in list_of_strings]
# result = [num for num in numbers if num % 2 == 0]
# print(result)

# with open("file1.txt") as file1:
#     list1 = file1.readlines()
#
# with open("file2.txt") as file2:
#     list2 = file2.readlines()
#
# result = [int(num) for num in list1 if num in list2]
# print(result)


# sentence = input()
# result = {word: len(word) for word in sentence.split()}
# print(result)


# weather_c = {"Monday": 4, "Tuesday":5, "Wednesday": 10, "Thursday": 11, "Friday": 12}
#
# weather_f = {day: temp* 9/5 + 32 for (day, temp) in weather_c.items()}
#
# print(weather_f)


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56,67,89]
}

for(key,value) in student_dict.items():
    print(value)


import pandas

student_data_frame = pandas.DataFrame(student_dict)

# for (key, value) in student_data_frame.items():
#     print(value)

for(index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)





