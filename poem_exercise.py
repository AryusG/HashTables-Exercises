word_count_hash = {}
# I need find repeats
with open('Resources/poem.txt', 'r') as file:
    symbols = [',', ';', ':', '.', '\n']
    contents = file.read()
    for symbol in symbols:
        contents = contents.replace(symbol, ' ').lower()
    content_list = contents.split(' ')

for item in content_list:
    if item in word_count_hash:
        word_count_hash[item] += 1
    else:
        word_count_hash[item] = 1

print(word_count_hash)

# ANSWER
word_count = {}
with open('Resources/poem.txt', 'r') as file:
    for line in file:
        tokens = line.split(' ')
        for token in tokens:
            token = token.replace('\n', '')
            if token in word_count:
                word_count[token] += 1
            else:
                word_count[token] = 1
print(word_count)


