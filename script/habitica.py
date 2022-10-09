import requests


def get_data(user_id: str, token: str, url: str, tag: str) -> list:
    data = requests.get(url, headers={'x-api-user': user_id, 'x-api-key': token})
    json_data = data.json()['data']

    tasks = list()

    for row in json_data:
        if row['type'] == 'todo' and tag in row['tags']:
            tasks.append(row['text'])

    return tasks
