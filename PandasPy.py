import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import FontProperties
df = pd.read_csv('remove_zero.csv')
del df['Unnamed: 0']
df.to_csv('remove_zero.csv')
zgj = df['最高价']

# zgj.plot()
plt.plot(zgj.index, zgj.values,label="最高价")
plt.legend()
plt.show()
