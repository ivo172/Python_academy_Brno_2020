#
# from  requests import get
# import datetime
#
# result = get('https://api.github.com/search/repositories', params={'q': 'requests+language:python'})
# json_result = result.json()
# today = datetime.datetime.now()
# today = today.strftime('%d/%m/%y %H:%M')
# json_result['date'] = str(today)
# print(json_result)

import numpy as np
import matpolotlib.pyplot as plt

def func(x):
    y = 2 * x + 2
    return y

x = np.arange(0, 10)
y = func(x)

plt.title('Nadpis')
plt.xlabel('x label a')
plt.plot(x, y)
plt.show()

