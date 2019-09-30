# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'Own Files\\Ch02\\02_02'))
    print(os.getcwd())
except:
    pass
# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# %%
df = pd.read_csv('../../inputs/Environmental_Data_Deep_Moor_2013.csv')


# %%
df_week1 = df[df['date'].between('2013_01_01', '2013_01_07')]


# %%
plt.plot(df_week1['Air_Temp'])


# %%
