import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df=pd.read_csv('C:\Sheeba C\Prodigy Infotech\Tasks\gender_submission.csv')
  # Display the first few rows
df.head()
# Get a concise summary of the DataFrame
df.info()  
 # Get statistical summaries of numerical columns
df.describe()
#Identify null values
df.isnull().sum()

# Calculate mean value
mean_value = df['PassengerId'].mean()

# Fill missing values and assign back to the DataFrame
df['PassengerId'] = df['PassengerId'].fillna(mean_value)
#remove duplicates
df.drop_duplicates(inplace=True)

df['PassengerId'].hist()  
plt.xlabel('Survived')
plt.ylabel('Passenger')
plt.title('Titanic Dataset')

df['Survived'].value_counts().plot(kind='bar')  # Example for sex column
plt.xlabel('Survived')
plt.ylabel('PassengerId')
plt.title('Titanic Dataset')

sns.boxplot(x='PassengerId', y='Survived', data=df)  # Example: Age distribution by passenger class
plt.title('Passenger Survival Rate')
plt.show()


