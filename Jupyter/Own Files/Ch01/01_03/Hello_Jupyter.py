# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import matplotlib.pyplot as plt

import os
try:
    os.chdir(os.path.join(os.getcwd(), 'Own Files\\Ch01\01_03'))
    print(os.getcwd())
except:
    pass
# %%
greeting = "Hello Jupyter!"
# %%
greeting

# %% [markdown]
# ## Length of Words in Greeting

# %%

words = greeting.split(" ")
word_length = list(len(w) for w in words)
plt.bar(words, word_length)
plt.show()
