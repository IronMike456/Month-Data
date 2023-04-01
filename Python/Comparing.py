""" 
Comparing data
Now that you know something about the statistical distribution of the data in your dataset, you're ready to examine your data to identify any apparent relationships between variables.

First of all, let's get rid of any rows that contain outliers so that we have a sample that is representative of a typical class of students. We identified that the StudyHours column contains some outliers with extremely low values, so we'll remove those rows. """

import pandas as pd
from matplotlib import pyplot as plt
import scipy.stats as stats
# Load data from a text file
df_students = pd.read_csv('grades.csv',delimiter=',',header='infer')

# Remove any rows with missing data
df_students = df_students.dropna(axis=0, how='any')

# Calculate who passed, assuming '60' is the grade needed to pass
passes  = pd.Series(df_students['Grade'] >= 60)

# Save who passed to the Pandas dataframe
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)


# Print the result out into this notebook
print(df_students)

df_sample = df_students[df_students['StudyHours']>1]
df_sample

"""Comparing numeric and categorical variables
The data includes two numeric variables (StudyHours and Grade) and two categorical variables (Name and Pass). 
Let's start by comparing the numeric StudyHours column to the categorical Pass column to see if there's an apparent relationship between the number of hours studied and a passing grade.

To make this comparison, let's create box plots showing the distribution of StudyHours for each possible Pass value (true and false)."""

df_sample.boxplot(column='StudyHours', by='Pass', figsize=(8,5))

# Create a bar plot of name vs grade and study hours
df_sample.plot(x='Name', y=['Grade','StudyHours'], kind='bar', figsize=(8,5))

"""A common technique when dealing with numeric data in different scales is to normalize the data so that the values retain their proportional distribution but are measured on the same scale.
 To accomplish this, we'll use a technique called MinMax scaling that distributes the values proportionally on a scale of 0 to 1. 
You could write the code to apply this transformation, but the Scikit-Learn library provides a scaler to do it for you."""

from sklearn.preprocessing import MinMaxScaler

# Get a scaler object
scaler = MinMaxScaler()

# Create a new dataframe for the scaled values
df_normalized = df_sample[['Name', 'Grade', 'StudyHours']].copy()

# Normalize the numeric columns
df_normalized[['Grade','StudyHours']] = scaler.fit_transform(df_normalized[['Grade','StudyHours']])

# Plot the normalized values
df_normalized.plot(x='Name', y=['Grade','StudyHours'], kind='bar', figsize=(8,5))

print(df_normalized.Grade.corr(df_normalized.StudyHours)) ## 0.911

""" The correlation statistic is a value between -1 and 1 that indicates the strength of a relationship. Values above 0 indicate a positive correlation (high values of one variable tend to coincide with high values of the other), while values below 0 indicate a negative correlation (high values of one variable tend to coincide with low values of the other). 
In this case, the correlation value is close to 1, showing a strongly positive correlation between study time and grade. """

# Create a scatter plot
df_sample.plot.scatter(title='Study Time vs Grade', x='StudyHours', y='Grade')

"""Note that this time, the code plotted two distinct things—the scatter plot of the sample study hours and grades is plotted as before, and then a line of best fit based on the least squares regression coefficients is plotted.

The slope and intercept coefficients calculated for the regression line are shown above the plot.

The line is based on the f(x) values calculated for each StudyHours value. Run the following cell to see a table that includes the following values:

The StudyHours for each student.
The Grade achieved by each student.
The f(x) value calculated using the regression line coefficients.
The error between the calculated f(x) value and the actual Grade value."""

