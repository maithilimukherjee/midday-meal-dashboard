import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('meals.csv')

df['coverage_pct'] = (df['meals_served']/df['meals_required'])*100

#bar-chart
state_avg = df.groupby('state')['coverage_pct'].mean()
plt.figure(figsize=(8,5))
state_avg.plot(kind='bar', color='pink')
plt.title('Average Midday - Meal Coverage by State')
