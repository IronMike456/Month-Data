""" What is NumPy?
NumPy is a Python library that provides functionality comparable to mathematical tools such as MATLAB and R. While NumPy significantly simplifies the user experience, it also offers comprehensive mathematical functions.

What is Pandas?
Pandas is an extremely popular Python library for data analysis and manipulation. Pandas is like a spreadsheet application for Python—providing easy-to-use functionality for data tables. 

Testing hypotheses
Data exploration and analysis is typically an iterative process, in which the data scientist takes a sample of data and performs the following kinds of tasks to analyze it and test hypotheses:

-Clean data to handle errors, missing values, and other issues.
-Apply statistical techniques to better understand the data and how the sample might be expected to represent the real-world population of data, allowing for random variation.
-Visualize data to determine relationships between variables, and in the case of a machine learning project, identify features that are potentially predictive of the label.
-Revise the hypothesis and repeat the process.
""" 

import numpy as np
import pandas as pd
data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
grades = np.array(data)
print(grades)
print (type(data),'x 2:', data * 2)
print('---')
print (type(grades),'x 2:', grades * 2)
print(grades.shape)
""" Now that you know your way around a NumPy array, it's time to perform some analysis of the grades data.

You can apply aggregations across the elements in the array, so let's find the simple average grade (in other words, the mean grade value). """
x = grades.mean() # Average 
print(x) 

# Define an array of study hours
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

# Create a 2D array (an array of arrays)
student_data = np.array([study_hours, grades])

# display the array
print(student_data) 

# Show the first element of the first element
print(student_data[0][0])
# Get the mean value of each sub-array
avg_study = student_data[0].mean()
avg_grade = student_data[1].mean()

print('Average study hours: {:.2f}\nAverage grade: {:.2f}'.format(avg_study, avg_grade))

""" Exploring tabular data with Pandas
NumPy provides a lot of the functionality and tools you need to work with numbers, such as arrays of numeric values. 
However, when you start to deal with two-dimensional tables of data, the Pandas package offers a more convenient structure to work with: the DataFrame.

Run the following cell to import the Pandas library and create a DataFrame with three columns. The first column is a list of student names, and the second and third columns are the NumPy arrays containing the study time and grade data."""

df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                            'StudyHours':student_data[0],
                            'Grade':student_data[1]})

print(df_students) 
# RESULT 
"""         Name  StudyHours  Grade
0         Dan       10.00   50.0
1       Joann       11.50   50.0
2       Pedro        9.00   47.0
3       Rosie       16.00   97.0
4       Ethan        9.25   49.0
5       Vicky        1.00    3.0
6    Frederic       11.50   53.0
7      Jimmie        9.00   42.0
8      Rhonda        8.50   26.0
9    Giovanni       14.50   74.0
10  Francesca       15.50   82.0
11      Rajab       13.75   62.0
12    Naiyana        9.00   37.0
13       Kian        8.00   15.0
14      Jenny       15.50   70.0
15     Jakeem        8.00   27.0
16     Helena        9.00   36.0
17      Ismat        6.00   35.0
18      Anila       10.00   48.0
19       Skye       12.00   52.0
20     Daniel       12.50   63.0
21      Aisha       12.00   64.0"""

""" 
Note that in addition to the columns you specified, the DataFrame includes an index to uniquely identify each row. We could have specified the index explicitly 
and assigned any kind of appropriate value (for example, an email address). However, because we didn't specify an index, one has been created with a unique integer value for each row."""

""" Finding and filtering data in a DataFrame
You can use the DataFrame's loc method to retrieve data for a specific index value, like this. """

# Get the data for index value 5
print(df_students.loc[5])
""" Name          Vicky
StudyHours      1.0
Grade           3.0 """
# Get the rows with index values from 0 to 5
print(df_students.loc[0:5])
"""    Name  StudyHours  Grade
0    Dan       10.00   50.0
1  Joann       11.50   50.0
2  Pedro        9.00   47.0
3  Rosie       16.00   97.0
4  Ethan        9.25   49.0
5  Vicky        1.00    3.0 """

# Get data in the first five rows
print(" LOC ")
print(df_students.iloc[0:5]) 

# Get data in the first five rows
print(" iLOC ")
print(df_students.iloc[0:5]) 

""" The loc method returned rows with index label in the list of values from 0 to 5, which includes 0, 1, 2, 3, 4, and 5 (six rows). However, the iloc method returns the rows in the positions included in the range 0 to 5. 
Since integer ranges don't include the upper-bound value, this includes positions 0, 1, 2, 3, and 4 (five rows).

iloc identifies data values in a DataFrame by position, which extends beyond rows to columns. So, for example, you can use it to find the values for the columns in positions 1 and 2 in row 0, like this:"""

print(df_students.iloc[0,[1,2]]) 

print(df_students.loc[0,'Grade']) 

print(df_students.loc[df_students['Name']=='Aisha'])

"""Actually, you don't need to explicitly use the loc method to do this. You can simply apply a DataFrame filtering expression, like this:"""

print(df_students[df_students['Name']=='Aisha'])

""" And for good measure, you can achieve the same results by using the DataFrame's query method, like this: """
print(df_students.query('Name=="Aisha"'))

""" Loading a DataFrame from a file
We constructed the DataFrame from some existing arrays. However, in many real-world scenarios, data is loaded from sources such as files. Let's replace the student grades DataFrame with the contents of a text file."""


df_students = pd.read_csv('grades.csv',delimiter=',',header='infer')
print(df_students.head())

# Handling missing values
df_students.isnull()

""" 
Of course, with a larger DataFrame, it would be inefficient to review all of the rows and columns individually, so we can get the sum of missing values for each column like this: """

df_students.isnull().sum()

""" 
So now we know that there's one missing StudyHours value and two missing Grade values.

To see them in context, we can filter the DataFrame to include only rows where any of the columns (axis 1 of the DataFrame) are null. """

df_students[df_students.isnull().any(axis=1)]

df_students.StudyHours = df_students.StudyHours.fillna(df_students.StudyHours.mean())
print(df_students)

"""
Alternatively, it might be important to ensure that you only use data you know to be absolutely correct. In this case, you can drop rows or columns that contain null values by using the dropna method. 
For example, we'll remove rows (axis 0 of the DataFrame) where any of the columns contain null values:"""

df_students = df_students.dropna(axis=0, how='any')
df_students

# Get the mean study hours using to column name as an index
mean_study = df_students['StudyHours'].mean()

# Get the mean grade using the column name as a property (just to make the point!)
mean_grade = df_students.Grade.mean()

# Print the mean study hours and mean grade
print('Average weekly study hours: {:.2f}\nAverage grade: {:.2f}'.format(mean_study, mean_grade))

# Get students who studied for the mean or more hours
df_students[df_students.StudyHours > mean_study]

# What was their mean grade?
df_students[df_students.StudyHours > mean_study].Grade.mean()

""" Let's assume that the passing grade for the course is 60.

We can use that information to add a new column to the DataFrame that indicates whether or not each student passed.

First, we'll create a Pandas Series containing the pass/fail indicator (True or False), and then we'll concatenate that series as a new column (axis 1) in the DataFrame. """

passes  = pd.Series(df_students['Grade'] >= 60)
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)

print(df_students) 

"""DataFrames are designed for tabular data, and you can use them to perform many of the same kinds of data analytics operations you can do in a relational database, such as grouping and aggregating tables of data.

For example, you can use the groupby method to group the student data into groups based on the Pass column you added previously and to count the number of names in each group. In other words, you can determine how many students passed and failed."""

print(df_students.groupby(df_students.Pass).Name.count())

## You can aggregate multiple fields in a group using any available aggregation function. For example, you can find the mean study time and grade for the groups of students who passed and failed the course. 

# Create a DataFrame with the data sorted by Grade (descending)
df_students = df_students.sort_values('Grade', ascending=False)

# Show the DataFrame
print(df_students)


