# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'Own Files\\Ch01\01_02'))
    print(os.getcwd())
except:
    pass

# %%
print("Hello Jupyter")


# %%

# %% [markdown]
""" ## Heading
    Some random paragraphs and latex
"""
# %% latex
""" 
"""

# %%
