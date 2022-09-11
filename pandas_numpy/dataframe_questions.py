import pandas as pd

df = pd.DataFrame()

# 1) How to check if a dataframe has any missing values?
df.isnull()

# 2) How to replace missing values of multiple numeric columns with the mean?

df.fillna(df.mean())
# 3) Given a dictionary, convert it into corresponding dataframe and display it
d = dict()
pd.DataFrame().from_dict(d).head()

# 4) Given a dataframe, sort it by title columns
df.sort_values(by=['title'], inplace=True)
