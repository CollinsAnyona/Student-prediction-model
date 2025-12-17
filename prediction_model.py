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
student_data.info()

# Check for missing values
print("Missing values per column:/n", student_data.isnull().sum())
#Visualize the distribution of numerical columns using histograms
student_data.hist(figsize=(10, 5))
# Feature engineering and selection
# Creating meaningful features
student_data = pd.read_csv("student_performance.csv")
student_data=student_data.drop(['Resources','Extracurricular','Internet','LearningStyle','OnlineCourses','Discussions','AssignmentCompletion','EduTech','Gender','Motivation','Age'], axis=1)
student_data['TotalFinalGrade']=student_data[['StudyHours','Attendance','ExamScore','StressLevel','FinalGrade']].mean(axis=1)
col_index = student_data.columns.get_loc('FinalGrade') + 1
student_data.insert(col_index, 'TotalFinalGrade', student_data.pop('TotalFinalGrade'))
print(student_data)

# Feature Engineering and Selection
# Computing Correlation analysis
correlation_matrix = student_data.corr()
print(correlation_matrix)
# Visualizing the results
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()
