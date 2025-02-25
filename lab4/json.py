import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

print('Interface Status')
print('=' * 85)
print('DN',' ' * 45,'Description',' ' * 8,'Speed','    ','MTU')
print('-' * 45, '  ', '-' * 18, ' ', '-' * 7, '  ', '-' * 4)

for imdata in data['imdata']:
    for physif, value in imdata.items():
        dn = value['attributes']['dn']
        speed = value['attributes']['speed']
        mtu = value['attributes']['mtu']

        print(f'{dn:<48} {' ':<20} {speed:<10} {mtu}')
