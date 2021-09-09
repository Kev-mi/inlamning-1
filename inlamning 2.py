import pandas as pd
import numpy as np

url = 'https://github.com/NordAxon/ec-python-course/blob/master/assignments/01_inlamningsuppgift_2_data.csv?raw=true'
df = pd.read_csv(url,index_col=0)
