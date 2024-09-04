# Import necessary libraries for statistical analysis
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels as sm

# Option to insert array of given data or load from a CSV file
# Example array data
data = np.array([2, 7, 9, 11, 14, 18, 25, 4, 7, 18, 22, 57, 63, 45, 33, 32, 28, 19])

# Descriptive Statistics with NumPy and pandas
mean = np.mean(data)
median = np.median(data)
variance = np.var(data)
std_dev = np.std(data)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")

# Descriptive statistics using pandas
df = pd.DataFrame(data, columns=['Values'])
summary_stats = df.describe()
print("Summary Statistics:")
print(summary_stats)

# Data Visualization with matplotlib and seaborn
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.hist(data, bins=20, alpha=0.75, color='skyblue')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Data')

plt.subplot(1, 2, 2)
sns.boxplot(data=data, color='lightgreen')
plt.title('Box Plot of Data')

plt.tight_layout()
plt.show()

# Hypothesis Testing (Independent t-test)
# Generating random data for demonstration
sample1 = np.random.normal(loc=0, scale=1, size=50)
sample2 = np.random.normal(loc=0.5, scale=1, size=50)

# Perform independent t-test
t_stat, p_value = stats.ttest_ind(sample1, sample2)

print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

if p_value < 0.05:
    print("Reject null hypothesis: There is a significant difference between the groups.")
else:
    print("Fail to reject null hypothesis: There is no significant difference between the groups.")

# Linear Regression with statsmodels
# Generating sample data for linear regression
np.random.seed(0)  # For reproducibility
x = np.random.rand(100)
y = 2 * x + 1 + np.random.normal(0, 0.5, 100)

# Fit linear regression model
X = sm.add_constant(x)  # Add intercept term
model = sm.OLS(y, X)
results = model.fit()

# Print regression results
print(results.summary())

# Plot the data and regression line
plt.scatter(x, y, label='Data', color='blue')
plt.plot(x, results.predict(X), color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()
