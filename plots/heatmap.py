from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



data = pd.read_table('HeatMapTable', header=0, index_col=0, delim_whitespace=True)

print(data.columns, data.iloc[0])


plt.hist2d(np.arange(len(data.columns)), data.iloc[0], bins=40, norm=LogNorm())

plt.colorbar()
plt.show()