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
print(person['skills'])
the_skills=person.get('skills')

if 'JavaScript' and 'React' in the_skills and len(the_skills)==2:
    print('He is a front end developer')
elif 'Node' and 'Python' and'MongoDB' in the_skills and len(the_skills)==3:
    print('He is a backend developer')
elif 'React' and 'Node' and 'MongoDB' in the_skills and len(the_skills)==3:
    print('He is a fullstack dev')
elif 'something' in the_skills:
    print('Unknown title')
