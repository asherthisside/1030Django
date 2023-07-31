import json

fp = open('data.json', 'r')
data = json.load(fp)
# for i in data:
#     print(i['name'], i['username'])

fp.close()
students = {
    "Student1": {
        "name": "Roushan Sharma",
        "class": 12,
        "age": 34,
        "subjects": ["Hindi", "English", "Maths"],
        "address": "Noida, UP",
        "present_today": False
    },
    
    "Student2": {
        "name": "Jyoti",
        "class": 10,
        "age": 24,
        "subjects": ["Hindi", "English", "Maths"],
        "address": "GZB, UP" ,
        "present_today": True
    },

    "Student3": {
        "name": "Abhishek",
        "class": 11,
        "age": 28,
        "subjects": ["Hindi", "English", "Maths"],
        "address": "Dehradun, UK",
        "present_today": True
    },

}
# print(type(students))
fp = open('students.json', 'w')
json.dump(students, fp)
# print(data)