import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('meals.csv')

df['coverage_pct'] = (df['meals_served']/df['meals_required'])*100

#bar-chart
state_avg = df.groupby('state')['coverage_pct'].mean()
plt.figure(figsize=(8,5))
state_avg.plot(kind='bar', color='pink')
plt.title('Average Midday - Meal Coverage by State')
plt.ylabel('Coverage Percentage')
plt.xlabel('State')
plt.xticks(rotation=45)
plt.show()

#pie-chart
def coverage_category(pct):
    if pct>=90:
        return 'Excellent'
    elif pct>=75:
        return 'Good'
    elif pct>=50:
        return 'Average'
    else:
        return 'Poor'

df['coverage_category'] = df['coverage_pct'].apply(coverage_category)

category_counts = df['category'].value_counts()

plt.figure(figsize=(6,6))
category_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title("Distribution of Schools by Coverage Category")
plt.ylabel("")
plt.show()
