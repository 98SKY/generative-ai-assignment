import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = pd.read_csv('student_data.csv')
df.columns = df.columns.str.strip().str.lower()  # normalize columns

# --- Task 1: Relational Plot ---
sns.relplot(data=df, x='age', y='medu', hue='sex')
plt.title('Age vs Mother Education by Sex')

# --- Task 2: Line Plot ---
sns.relplot(data=df, x='age', y='g3', kind='line', marker='o')
sns.relplot(data=df, x='age', y='g3', kind='line', col='sex')

# --- Task 3: Distribution Plots ---
plt.figure()
sns.histplot(df['g3'], kde=True)

# --- Task 4: Bivariate Distribution ---
sns.displot(data=df, x='age', y='g3', kind='hist')
sns.displot(data=df, x='age', y='g3', kind='kde')

# --- Task 5: Matrix Plots ---
sns.pairplot(df[['age', 'g3', 'health']])

plt.figure()
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm')

# --- Task 6: Categorical Plots ---
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
sns.barplot(data=df, x='sex', y='medu', ax=axes[0,0])
sns.boxplot(data=df, x='sex', y='medu', ax=axes[0,1])
sns.violinplot(data=df, x='sex', y='medu', ax=axes[1,0])
sns.countplot(data=df, x='sex', ax=axes[1,1])
plt.tight_layout()

# --- Task 7: Regression ---
sns.regplot(data=df, x='age', y='g3')
sns.lmplot(data=df, x='age', y='g3', hue='sex')

# --- Task 8: Facet Grid ---
g = sns.FacetGrid(df, col="sex")
g.map(sns.scatterplot, "age", "g3")

# Dashboard-style plots
sns.relplot(data=df, x="age", y="g3", col="famrel", kind="scatter")
sns.catplot(data=df, x="sex", y="g3", kind="box")
sns.displot(data=df, x="g3", kde=True)

plt.show()