import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("books.csv")

# Set visual style
sns.set(style="whitegrid")


# VISUAL 1: Price Distribution

plt.figure(figsize=(8,5))
sns.histplot(df['Price'], bins=30, kde=True)
plt.title("Distribution of Book Prices")
plt.xlabel("Price")
plt.ylabel("Number of Books")
plt.show()


# VISUAL 2: Boxplot for Outliers

plt.figure(figsize=(6,4))
sns.boxplot(x=df['Price'])
plt.title("Boxplot of Book Prices (Outlier Detection)")
plt.show()


# VISUAL 3: Stock Availability

plt.figure(figsize=(6,4))
sns.countplot(x='Stock', data=df)
plt.title("Stock Availability of Books")
plt.xlabel("Stock Status")
plt.ylabel("Count")
plt.show()


# VISUAL 4: Price Density

plt.figure(figsize=(8,5))
sns.kdeplot(df['Price'], fill=True)
plt.title("Price Density of Books")
plt.xlabel("Price")
plt.show()


# VISUAL 5: Price Category Analysis

df['Price_Range'] = pd.cut(
    df['Price'],
    bins=[0, 20, 40, 60],
    labels=['Low', 'Medium', 'High']
)

plt.figure(figsize=(6,4))
sns.countplot(x='Price_Range', data=df)
plt.title("Books by Price Range")
plt.xlabel("Price Category")
plt.ylabel("Number of Books")
plt.show()
