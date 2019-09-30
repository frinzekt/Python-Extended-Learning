# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'Own Files\\Ch02\02_03'))
    print(os.getcwd())
except:
    pass
# %%
from IPython import get_ipython

# %%
# %load helper.py
import pandas as pd
df = pd.read_csv("../../inputs/Environmental_Data_Deep_Moor_2015.csv")


def get_day(d):
    return df[df['date'] == d]


# %%
get_day('2015_01_01')


# %%
get_ipython().run_line_magic('cat', 'plot_numbers.py')


# %%
get_ipython().run_line_magic('run', 'plot_numbers.py 1 3 4 7 9')


# %%
get_ipython().run_line_magic(
    'time', "sum(x for x in df['Air_Temp'])/len(df['Air_Temp'])")


# %%
get_ipython().run_line_magic('time', "df['Air_Temp'].mean()")


# %%
get_ipython().run_line_magic('timeit', "df['Air_Temp'].mean()")


# %%
get_ipython().run_line_magic('system',
                             'grep 2015_01_01 ../../inputs/Environmental_Data_Deep_Moor_2015.csv | wc -l')


# %%
Out[57]


# %%
get_ipython().getoutput(
    'grep 2015_01_01 ../../inputs/Environmental_Data_Deep_Moor_2015.csv | wc -l')
