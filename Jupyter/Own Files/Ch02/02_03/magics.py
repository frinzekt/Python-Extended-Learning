# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'Own Files\\Ch02\\02_03'))
    print(os.getcwd())
except:
    pass

# %%
# %load helper.py
import helper

# %%
query = helper.get_day('2015_01_01')


# %%
# %cat plot_numbers.py

# %%
# %run plot_numbers.py 1 3 4 7 9
os.system("plot_numbers 1 3 4 7 9")

# %%
df = helper.get_df()

# %%
%time sum(x for x in df['Air_Temp'])/len(df['Air_Temp'])

# %%
%time df['Air_Temp'].mean()


# %%
%timeit df['Air_Temp'].mean()


# %%
