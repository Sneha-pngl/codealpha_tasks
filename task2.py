import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# STEP 1: Load the dataset

df = pd.read_csv("books.csv")


# STEP 2: Remove unnecessary column

# 'Unnamed: 0' is an auto-generated index column
df.drop(columns=['Unnamed: 0'], inplace=True)


# STEP 3: Understand the dataset

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())


# STEP 4: Check data quality

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())


# STEP 5: Ask meaningful questions
# Q1: What is the price distribution of books?
# Q2: Are all books in stock?
# Q3: Are there price outliers?



# STEP 6: Price distribution

plt.figure(figsize=(8,5))
sns.histplot(df['Price'], bins=30)
plt.title("Distribution of Book Prices")
plt.xlabel("Price")
plt.ylabel("Number of Books")
plt.show()


# STEP 7: Stock analysis

plt.figure(figsize=(6,4))
sns.countplot(x='Stock', data=df)
plt.title("Stock Availability")
plt.show()


# STEP 8: Detect outliers using boxplot

plt.figure(figsize=(6,4))
sns.boxplot(x=df['Price'])
plt.title("Price Outliers")
plt.show()

# STEP 9: Insights

print("\nAverage Book Price:", df['Price'].mean())
print("Minimum Price:", df['Price'].min())
print("Maximum Price:", df['Price'].max())


# STEP 10: Save cleaned dataset

df.to_csv("books.csv", index=False)
print("\nCleaned dataset saved successfully.")
