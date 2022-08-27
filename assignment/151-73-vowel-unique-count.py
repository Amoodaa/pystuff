from typing import OrderedDict


vowels = ('a', 'e', 'o', 'u', 'i')

str = input("Enter one of five grades: ")


sanitized_str = set(str)

vowel_unique_count = len(sanitized_str.intersection(vowels))


print(vowel_unique_count)
