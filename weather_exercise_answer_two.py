# TODO What was the temperature on Jan 9 and Jan 4
hash_table = {}
with open('Resources/nyc_weather.csv', 'r') as file:
    for line in file:
        token = line.split(',')
        day = token[0]
        # day: value
        try:
            hash_table[day] = int(token[1])
        except:
            print('Invalid Entry. Ignore Row')

print(hash_table['Jan 9'], hash_table['Jan 4'])