import json
from json import JSONDecodeError
import os

filename = 'favoriteNumbers.json'


def greetings():
    name = input('Hello, what is your name? ')
    data = load_data()
    if name in data:
        print(f'Hello, i know your favorite number! It\'s: {data[name]}')
    else:
        print('Oh, you are new here right?')
        remember_number(name, data)


def load_data():
    if not os.path.exists(filename):
        f = open(filename, 'w')
        f.close()
    with open(filename) as f:
        try:
            return json.load(f)
        except JSONDecodeError:
            return {}


def save_data(data):
    with open(filename, 'w') as f:
        json.dump(data, f)


def remember_number(name, data):
    number = input('Enter your favorite number: ')
    data[name] = number
    save_data(data)
    print('Cool, i remembered it now.')


greetings()