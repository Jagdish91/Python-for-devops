import json

people_string = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "123-456-7890",
            "emails": ["john.smith@example.com", "smith.john@example.com"],
            "has_license": false
        },
        {
            "name": "Travis Thompson",
            "phone": "878-123-7890",
            "emails": ["travis.thompson@example.com", "thompson.travis@example.com"],
            "has_license": true
        }
    ]
}
'''

data = json.loads(people_string)

#we can check the data type conversion between json and python
#object converts to dict and array to list
print(type(data))
print(type(data['people']))

#we can access the data in list individually using for loop
for person in data['people']:
    pass
    #print(person['name'])

#To remove the phone numbers and convert it to json again
for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=4, sort_keys=True)

#print(new_string)


#loading a file
with open(r'C:\Users\jagdi\Python for Devops\states.json') as file:
    file_data = json.load(file)


for state in file_data['states']:
    print(state['name'], state['area_codes'])


