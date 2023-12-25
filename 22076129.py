# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the books_data dataset
df_books = pd.read_csv("books_data.csv")

# Convert 'Author_Rating' and 'Publishing Year' to numeric if not already
df_books['Author_Rating'] = pd.to_numeric(df_books['Author_Rating'], errors='coerce')
df_books['Publishing Year'] = pd.to_numeric(df_books['Publishing Year'], errors='coerce')

# Treat 'fiction' and 'genre fiction' as the same genre
df_books['genre'] = df_books['genre'].replace({'genre fiction': 'fiction'})

# Filter out rows with negative publishing years
df_books = df_books[df_books['Publishing Year'] >= 1850]

# Compute summary statistics using numpy and pandas
summary_stats_books = df_books.describe()

# Set up the matplotlib figure and axes for subplots with vertical spacing
fig_books, axes_books = plt.subplots(nrows=2, ncols=2, figsize=(12, 10), gridspec_kw={'hspace': 0.5})
fig_books.suptitle("Books Data Insights\nStudent Name: Devi Manamthanam Dhanapalan\nStudent ID: 22076129", fontsize=16)

# Plot 1: Line plot for total sales over the years
total_sales_over_years = df_books.groupby('Publishing Year')['gross sales'].sum().reset_index()

# Select 10 years from the range of minimum to maximum publishing years
selected_years = np.linspace(1850, df_books['Publishing Year'].max(), 10).astype(int)

sns.lineplot(x="Publishing Year", y="gross sales", data=total_sales_over_years, ax=axes_books[0, 0], marker='o', color='skyblue')
axes_books[0, 0].set_title("Total Sales Over the Years (after 1850)")
axes_books[0, 0].set_xticks(selected_years)
axes_books[0, 0].set_xticklabels(selected_years, ha="right")
axes_books[0, 0].text(0.5, -0.2, "Increasing trend of books sales after 1960", ha="center", transform=axes_books[0, 0].transAxes)

# Plot 2: Box plot of average book ratings by genre
sns.boxplot(x="genre", y="Book_average_rating", data=df_books, ax=axes_books[0, 1])
axes_books[0, 1].set_title("Average Book Ratings Distribution by Genre")
axes_books[0, 1].tick_params(axis='x')  
axes_books[0, 1].text(0.5, -0.2, "Average ratings among all the genres is almost the same", ha="center", transform=axes_books[0, 1].transAxes)

# Plot 3: Count plot of books by language
sns.countplot(x="language_code", data=df_books, ax=axes_books[1, 0])
axes_books[1, 0].set_title("Count of Books by Language")
axes_books[1, 0].tick_params(axis='x')  
axes_books[1, 0].text(0.5, -0.2, "Non English language books are almost insignificant", ha="center", transform=axes_books[1, 0].transAxes)

# Plot 4: Count plot of genres
sns.countplot(x="genre", data=df_books, ax=axes_books[1, 1])
axes_books[1, 1].set_title("Count of Books by Genre")
axes_books[1, 1].tick_params(axis='x')  
axes_books[1, 1].text(0.5, -0.2, "Domination of Fiction genre", ha="center", transform=axes_books[1, 1].transAxes)

# Save the infographic as a PNG file
plt.savefig("22076129.png", dpi=300)
