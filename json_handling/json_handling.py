import json
#--------------------------------------
#Working with JSON strings
#--------------------------------------

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

# Convert JSON string to Python object
data = json.loads(people_string)

#we can check the data type conversion between json and python
#object converts to dict and array to list
print(type(data))                   # dict   
print(type(data['people']))         # list

#we can access the data in list individually using for loop
for person in data['people']:
    pass
    #print(person['name'])

#To remove the phone numbers and convert it to json again
for person in data['people']:
    del person['phone']

# Convert Python object back to JSON
new_string = json.dumps(data, indent=4, sort_keys=True)

#print(new_string)


#-------------------------------------------------------
# Working with JSON files
#-------------------------------------------------------


#loading a file

file_path = r'enter your file path here'
with open(file_path) as file:
    file_data = json.load(file)

# Remove area codes
for state in file_data['states']:
    del state['area_codes']

# Write cleaned data to new file
with open('new_states.json','w') as f:
    json.dump(file_data, f, indent=3)

print("JSON cleaning completed successfully")
