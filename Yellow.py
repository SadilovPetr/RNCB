import requests
import pandas as pd
url = 'https://ws-public.interpol.int/notices/v1/yellow'
header = ['entity_id', 'nationalities', 'name', 'forename', 'date_of_birth', 'photo']
result = []
while True:
    resp = requests.get(url)
    data = resp.json()
    for item in data['_embedded']['notices']:
        person = []
        person.append(item['entity_id'])
        person.append(item['nationalities'])
        person.append(item['name'])
        person.append(item['forename'])
        person.append(item['date_of_birth'])
        if item['_links'].get('thumbnail'):
            person.append(item['_links']['thumbnail'].get('href'))
        else:
            person.append('Нет фото')
        result.append(person)
    if data['_links'].get('next'):
        url = data['_links']['next']['href']
    else:
        break
df = pd.DataFrame(result, columns=header)
df.to_csv('/PycharmProjects/YellowNotices/YellowNotices_data.csv', sep=':', encoding='utf8')
print(result)