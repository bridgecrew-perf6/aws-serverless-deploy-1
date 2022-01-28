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
        num_books = data['count']
        print(f'Number of books: {num_books}')
        response = {
            'num_books': num_books
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

    lambda_handler(event, context)

if __name__ == '__main__':
    main()