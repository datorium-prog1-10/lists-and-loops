names = ['Anna', 'Arturs', 'Eliza', 'Krista']
ages = [22, 19, 12, 18]

print('======================================')
print('Izvadam vārdu un vecumu')
print('======================================')
for number in range(len(names)):
    print(f'{names[number]} is {ages[number]} years old')

print('======================================')
print('Izvadam vādru un vārda garumu ar indeksiem')
print('======================================')
for i in range(len(names)):
    print(f'{names[i]} has {len(names[i])} letters in the name.')

print('======================================')
print('Izvadam vādru un vārda garumu ar mainīgo')
print('======================================')
for name in names:
    print(f'{name} has {len(name)} letters in the name.')
