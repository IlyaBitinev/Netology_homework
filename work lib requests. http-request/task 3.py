import datetime
import requests
from pprint import pprint


def get_questions():
    current_time = datetime.datetime.now()
    url = 'https://api.stackexchange.com/2.3/questions/'
    dict_q = []
    params = {'fromdate': int(current_time.timestamp() - 86400 * 2),
              'todate': int(current_time.timestamp()),
              'tagged': 'python',
              'site': 'stackoverflow',
              'order': 'desc',
              'sort': 'activity'}
    response = requests.get(url, params=params).json()
    for item in response['items']:
        dict_q.append(item['title'])

    return f'всего количесвто запросов за два дня составляет {len(dict_q)}'


if __name__ == '__main__':
    pprint(get_questions())
