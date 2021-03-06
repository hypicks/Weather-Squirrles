#with open("weather_data.csv") as data_file:
#    data = data_file.readline()
#    print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in list(data)[1:]:
#         temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
#print(type(data))
#print(type(data["temp"]))

#data_dict = data.to_dict()
#print(data_dict)
#
#temp_list = data["temp"].to_list()
#print(len(temp_list))

#average = sum(temp_list) / len(temp_list)
#print(average)

#print(data["temp"].mean())
#
#print(data["temp"].max())
#print(data["temp"].min())
#
## Get Data in Columns
#print(data["condition"])
#print(data.condition)

#Get Data in Row
#print(data[data.day == "Monday"])
#print(data[data.temp == data.temp.max()])
#
#monday = data[data.day == "Monday"]
#monday_temp = int(monday.temp)
#monday_temp_f = monday_temp * 9/5 + 32
#print(monday_temp_f)


#Create a dataframe from scratch
#data_dict = {
#    "students": ["Amy", "James", "Angela"],
#    "scores": [76, 56, 65]
#}
#
#data = pandas.DataFrame(data_dict)
#data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
#print(gray_squirrels_count)
#print(black_squirrels_count)
#print(cinnamon_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Color": [gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")