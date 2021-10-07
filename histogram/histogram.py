import pandas as pd
from matplotlib import pyplot as plt
from statistics import median
plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ages = data['Age']

print(median(ages))
# bins = [5*i for i in range(1,21)]
bins = [i for i in range(1,101)]
plt.hist(ages, bins=bins, edgecolor='black', log=False)

median_age = 29
color = '#fc4f30'

plt.axvline(median_age, color=color, label='Age Median', linewidth=2)

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()
