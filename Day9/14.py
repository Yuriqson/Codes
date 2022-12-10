person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['React', 'Node', 'MongoDB'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
if person['is_marred']==True and person['country']=='Finland':
    print('{} lives in {}.He is married.'.format(person['first_name'],person['country']),)