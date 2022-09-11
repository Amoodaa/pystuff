import pandas as pd

my_str = 'dbc deb abed ggade'
chars = list("".join(my_str.split(' ')))
# least frequent is 'c'

df = pd.DataFrame(chars)


least_frequent_char = str(df.value_counts().index[-1][0])

new_str = least_frequent_char.join(my_str.split(' '))

print(new_str)
