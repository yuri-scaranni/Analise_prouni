import requests


def extract(file_name, url):
    data = requests.get(url)

    if data.status_code != 200:
        print('Erro ao extrair!')

    with open(file_name, 'wb') as f:
        f.write(data.content)

    print(f'>> [{file_name}] extraído com sucesso. <<')

