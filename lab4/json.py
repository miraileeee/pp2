import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

print('Interface Status')
print('=' * 80)
print('DN',' ' * 49, 'Description', ' ' * 11, 'Speed', ' ' * 4, 'MTU')
print('-' * 50, ' ', '-' * 20, '  ', '-' * 6, '  ', '-' * 6)