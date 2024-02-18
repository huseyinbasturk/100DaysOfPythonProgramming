# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
#
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data.condition)
#
# # get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)
#
# # create a data frame
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores":[76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels)
print(red_squirrels)
print(black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")
