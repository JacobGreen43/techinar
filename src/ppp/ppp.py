import pandas as pd

import math

pizzas_path = ('data/pizzas.csv')
pizzas = pd.read_csv(pizzas_path)

pizzas['Area'] = ((pizzas['Size'] / 2) ** 2 * math.pi)
pizzas['Price_Per_SqInch'] = (pizzas['Price'] / pizzas['Area'])

df = pd.DataFrame(pizzas)
pizzas_df = df.sort_values(by=['Price_Per_SqInch'], ascending=True)
print(pizzas_df)
