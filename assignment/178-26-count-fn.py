def count(str, substr):
    splitted = str.split(substr)
    return len(splitted) - 1


print(count('1asda', 'asd'))
