# get average temp for week 1
arr = []

with open('Resources/nyc_weather.csv', 'r') as file:
    for line in file:
        token = line.split(',')
        try:
            temp = int(token[1])
            arr.append(temp)
        except:
            print("Invalid Temperature. Ignore the row")

total_temp = 0
for temp in arr:
    total_temp += temp

avrg_temp = total_temp / len(arr)
print(avrg_temp)

# get max temp for first 10 days
print(max(arr[0:10]))





