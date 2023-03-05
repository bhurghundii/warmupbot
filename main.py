import pandas as pd
from enum import Enum
import random

# CONFIG ENUM 
class Genre(Enum):
    Art =  3
    Stills = 1 
    Programming = 1 

df = pd.read_csv("kata.csv")
unique_genres = df["Genre"].unique()

for genre in unique_genres:
    selected_pd = (df.loc[df['Genre'] == genre])
    print("\n \n ## Task for ", genre)

    for value in (selected_pd.sample(Genre[genre].value).values):
        print (value[0])
        print ("Source: " + value[1])
        if ((value[3]) == "Collection"):
            print("Pick number: ", random.randint(1, value[4]))
