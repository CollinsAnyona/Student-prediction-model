#Importing python libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from google.colab import files
uploaded = files.upload()

import pandas as pd
student_data = pd.read_csv("student_performance.csv")
from google.colab import drive
drive.mount('/content/drive')


#Display the first five rows of the dataframe
student_data.head()
#Get the descriptive statistics of the numerical columns
student_data.describe()
#Get basic information about data types and missing values
student_data.info()