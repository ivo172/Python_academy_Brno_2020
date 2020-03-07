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
import matplotlib.pyplot as plt

x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()


# def func(x):
#     y = 2 * x + 2
#     return y

# x = np.arange(0, 10)
# y = func(x)

# plt.title('Funkce')
# plt.xlabel('x label a')
# plt.plot(x, y)
# plt.show()