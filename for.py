import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

#sodium_df_1 = pd.read_csv('sodium.csv')

# x = sodium_df_1.column_name

# name_of_x = Counter(x)

class Meal:
    def __init__(self, carb, fiber, protein, sodium):
        self.carb = carb
        self.fiber = fiber
        self.protein = protein
        self.sodium = sodium
        self.calories = 0
        carb_2 = carb

    def eating(self,carb):
        self.calories += 4*carb

carb_number = 20
Pasta = Meal(carb_number,10,5,1)
Pasta.eating(carb_number)
