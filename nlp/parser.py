import re
list = []
with open('city.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        list.append(re.sub("^\s+|\n|\r|\s+$", '', line))

print(list)
