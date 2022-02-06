

import matplotlib.pyplot as plt
import pandas as pd

dt=pd.read_csv("breastcancer.csv")
dt

fig=plt.scatter(dt.loc[:,"perimeter_mean"],dt.loc[:,"area_mean"])
plt.savefig('test.png')

plt.show()
