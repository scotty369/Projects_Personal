## Descriptive Statistics with NumPy and pandas!

import numpy as np
import pandas as pd

# Create a sample dataset
data = np.random.normal(loc=0, scale=1, size=100)  # Generate random data

# Calculate mean, median, variance, standard deviation
mean = np.mean(data)
median = np.median(data)
variance = np.var(data)
std_dev = np.std(data)

print("Mean:", mean)
print("Median:", median)
print("Variance:", variance)
print("Standard Deviation:", std_dev)

# Using pandas for descriptive statistics
df = pd.DataFrame(data, columns=['Values'])
summary_stats = df.describe()
print(summary_stats)

## Hypothesis Testing with scipy!

from scipy import stats

# Create two samples for independent t-test
sample1 = np.random.normal(loc=0, scale=1, size=50)
sample2 = np.random.normal(loc=0.5, scale=1, size=50)

# Perform independent t-test
t_stat, p_value = stats.ttest_ind(sample1, sample2)

print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Reject null hypothesis: There is a significant difference between the groups.")
else:
    print("Fail to reject null hypothesis: There is no significant difference between the groups.")


## Linear Regression with statsmodels!

import statsmodels.api as sm
import matplotlib.pyplot as plt

# Create sample data for linear regression
x = np.random.rand(100)
y = 2 * x + 1 + np.random.normal(0, 0.5, 100)

# Fit linear regression model
X = sm.add_constant(x)  # Add intercept term
model = sm.OLS(y, X)
results = model.fit()

# Print regression results
print(results.summary())

# Plot the data and regression line
plt.scatter(x, y, label='Data')
plt.plot(x, results.predict(X), color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()

## Data Visualization with matplotlib and seaborn to create histograms/box plots!

import matplotlib.pyplot as plt
import seaborn as sns

# Create a dataset
data = np.random.normal(loc=0, scale=1, size=100)

# Histogram
plt.hist(data, bins=20, alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Data')
plt.show()

# Box Plot
sns.boxplot(data=data)
plt.title('Box Plot of Data')
plt.show()
