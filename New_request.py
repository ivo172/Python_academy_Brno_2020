
from  requests import get
import datetime

result = get('https://api.github.com/search/repositories', params={'q': 'requests+language:python'})
json_result = result.json()
today = datetime.datetime.now()
today = today.strftime('%d.%m.%y %H:%M')
json_result['date'] = str(today)
print(json_result)
