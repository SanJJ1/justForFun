import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

ages = ['a', 'b', 'a', 'c', 'd', 'e', 'e', 'e', 'e', 'f', 'g']
plt.hist(ages, edgecolor='black', )
# data = pd.read_csv('data.csv')
# ids = data['Responder_id']
# ages = data['Age']

# median_age = 29
# color = '#fc4f30'

# plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()
