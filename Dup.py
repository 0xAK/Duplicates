some_list = ['d','d','u','p','l','i','c','c','t','e','s','s','s']
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)
