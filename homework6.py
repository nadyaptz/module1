my_dict={'Andrey':1976, 'Nadya':1977, 'Dasha':2002, 'Sasha':2007}
print('Dictionary:', my_dict)
print('Existing value:', my_dict.get('Nadya'))
print('Not existing value:', my_dict.get('Tanya'))
my_dict.update({'Tanya': 1948, 'Niels': 2010})
print('Updated Dictionary:', my_dict)
deleted_pair=my_dict.pop('Niels')
print('Deleted value:', deleted_pair)
print('Once again updated Dictionary:', my_dict)

my_set={'Andrey', 1976, True, 'male', 'Nadya', 1977, False, 'female',
        'Dasha', 2002, False, 'female', 'Sasha', 2007, True, 'male', (1, 2, 3)}
print('Set:', my_set)
my_set.add("FEMALE")
my_set.add("MALE")
my_set.remove('male')
print('Updated Set:', my_set)