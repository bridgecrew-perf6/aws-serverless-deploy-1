import requests
import yaml
import json

from exceptions import InvalidResultError

with open('config.yml', 'r') as f:
    config = yaml.load(f, yaml.Loader)

def lambda_handler(event, context):
    statusCode = 200
    result = requests.get(config['base-address']+config['api']['endpoint'])

    if result.status_code == 200:
        data = result.json()
        books = data['results']
        response = {}
        for book in books[:5]:
            response[book['title']] = {
                'copyright' : book['copyright'],
                'download_count': book['download_count']
            }

    else:
        raise InvalidResultError

    return {
        'statusCode' : statusCode,
        'body' : json.dumps(response)
    }



def main():
    event = {}
    context = None

    response = lambda_handler(event, context)

    print(response)

if __name__ == '__main__':
    main()