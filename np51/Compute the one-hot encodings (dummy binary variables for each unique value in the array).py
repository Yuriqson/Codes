import numpy as np
np.random.seed(101)
arr = np.random.randint(1,4, size=6)
print(arr)
print((arr[:, None] == np.unique(arr)).view(np.int8))

"""
most Machine Learning algorithms cannot work with categorical data and needs to be converted into 
numerical data. Sometimes in datasets, we encounter columns that contain categorical features 
(string values) for example parameter Gender will have categorical parameters like Male, Female. 
These labels have no specific order of preference and also since the data is string labels, machine 
learning models misinterpreted that there is some sort of hierarchy in them.
 One approach to solve this problem can be label encoding where we will assign a numerical value to 
 these labels for example Male and Female mapped to 0 and 1. But this can add bias in our model as it
  will start giving higher preference to the Female parameter as 1>0 and ideally both labels are equally 
  important in the dataset. To deal with this issue we will use One Hot Encoding technique.
"""