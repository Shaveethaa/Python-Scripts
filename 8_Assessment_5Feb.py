'''1. Given a complex JSON structure representing a hierarchical organization with employees and their departments, 
write a program to extract the names of all employees who hold a managerial position in any department. 
Ensure that the output is a sorted list of unique names. Extract the names of all employees holding a managerial position.
Input:
{
  "organization": {
    "departments": [
      {
        "name": "Engineering",
        "employees": [
          {"name": "Alice", "position": "Engineer"},
          {"name": "Bob", "position": "Manager"},
          {"name": "Charlie", "position": "Engineer"}
        ]
      },
      {
        "name": "Sales",
        "employees": [
          {"name": "David", "position": "Salesperson"},
          {"name": "Eve", "position": "Manager"}
        ]
      }
    ]
  }
}

Output: ['Bob', 'Eve']'''
import json
in_json = {
  "organization": {
    "departments": [
      {
        "name": "Engineering",
        "employees": [
          {"name": "Alice", "position": "Engineer"},
          {"name": "Bob", "position": "Manager"},
          {"name": "Charlie", "position": "Engineer"}
        ]
      },
      {
        "name": "Sales",
        "employees": [
          {"name": "David", "position": "Salesperson"},
          {"name": "Eve", "position": "Manager"}
        ]
      }
    ]
  }
}
# json_object = json.dumps(in_json, indent=4)
# with open("Organization5.json",'w') as file:
#     file.write(json_object)
with open("Organization5.json",'r') as file:
    py_object = json.load(file)
#print(type(py_object))
depart = py_object.get("organization").get("departments")
#print(depart)
emp = []
managers = []
for each in depart:
    emp.append(each.get("employees"))
emp = emp[0] + emp[1]
#print(emp)
for each in emp:
    if each.get("position") == "Manager":
        managers.append((each.get("name")))

print("Managers:", managers)


'''2. Given a nested JSON structure representing a file system, write a program to find the total size occupied by files in a specific directory and its subdirectories.
Input:
json_data = {
  "name": "root",
  "type": "directory",
  "size": None,
  "contents": [
    {
      "name": "folder1",
      "type": "directory",
      "size": None,
      "contents": [
        {"name": "file1.txt", "type": "file", "size": 1024},
        {"name": "file2.txt", "type": "file", "size": 512}
      ]
    },
    {
      "name": "folder2",
      "type": "directory",
      "size": None,
      "contents": [
        {"name": "file3.txt", "type": "file", "size": 256},
        {"name": "file4.txt", "type": "file", "size": 128}
      ]
    },
    {"name": "file5.txt", "type": "file", "size": 64}
  ]
}

Output:
The total size of files in the specified directory and its subdirectories is: 1984 bytes.'''

import json
json_data = {
  "name": "root",
  "type": "directory",
  "size": "None",
  "contents": [
    {
      "name": "folder1",
      "type": "directory",
      "size": "None",
      "contents": [
        {"name": "file1.txt", "type": "file", "size": 1024},
        {"name": "file2.txt", "type": "file", "size": 512}
      ]
    },
    {
      "name": "folder2",
      "type": "directory",
      "size": "None",
      "contents": [
        {"name": "file3.txt", "type": "file", "size": 256},
        {"name": "file4.txt", "type": "file", "size": 128}
      ]
    },
    {"name": "file5.txt", "type": "file", "size": 64}
  ]
}
# jsonfile = json.dumps(json_data, indent=3)
# with open("File_system.json",'w') as file:
#    file.write(jsonfile)
with open("File_system.json",'r') as file1:
   pyobj = json.load(file1)
#print(type(pyobj))
content_out = pyobj["contents"]
size = []
for each in content_out:
   size.append(each.get("size"))
   value_out = each.get("contents")
   #print(value_out)
   if value_out is not None:
     for each_value in value_out:
       if each_value is not None:
         size.append(each_value.get("size"))

remove_ele = "None"
final_size = [j for i, j in enumerate(size) if j!=remove_ele]
bytes= sum(final_size)
print(f"The total size of files in the specified directory and its subdirectories is: {bytes} bytes")


'''3. Write a program to transform a JSON structure representing a list of students and their grades into a report card, 
including the average grade for each student and the class average. ALos sort the order of average from highest to lowest inside report card
Input:
{
  "students": [
    {"name": "Alice", "grades": [90, 85, 92]},
    {"name": "Bob", "grades": [78, 88, 94]},
    {"name": "Charlie", "grades": [92, 95, 89]}
  ]
}
Output:
Report Card:
[{'name': 'Charlie', 'average_grade': 92.0}, {'name': 'Alice', 'average_grade': 89.0}, {'name': 'Bob', 'average_grade': 87.0}]
Class Average: 89'''
def faverage(li):
    return sum(li)/len(li)
inp = {
  "students": [
    {"name": "Alice", "grades": [90, 85, 92]},
    {"name": "Bob", "grades": [78, 88, 94]},
    {"name": "Charlie", "grades": [92, 95, 89]}
  ]}
report = []
x=0
student_list = inp.get("students")
for each in student_list:
  name = each.get("name")
  grade = each.get("grades")
  average_grade = round(faverage(grade),0)
  #print(name, grade, average_grade)
  out_dict = {"name":name, "average_grade":average_grade}
  report.append(out_dict)
  x = x+average_grade
x = round(x/len(student_list),0)
print("Report card: ", report)
print("Class Average: ", x)


'''4. You are given two lists: one containing names and the other containing corresponding birth years. Your task is to manipulate these lists and generate key-value pairs with the name as the key and age as the value. Calculate the age based on the given birth year and today's date. Then, create a JSON structure to represent this information. Additionally, calculate the average age of the individuals and include it in the JSON output.
Input:
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
birth_years = [1980, 1978, 1991, 1971, 1995]

Output should be in json format:
{
  "above_40": {
    "Alice": 44,
    "Bob": 46,
    "David": 53
  },
  "below_40": {
    "Charlie": 33,
    "Eve": 29
  },
  "statistics": {
    "count_above_40": 3,
    "count_below_40": 2
  }
}'''
import json
import datetime
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
birth_years = [1980, 1978, 1991, 1971, 1995]
this_year = datetime.date.today().year
age = [(this_year-year) for year in birth_years]
above_40 = {}
below_40 = {}
out_dict = {}
# print(age)
for i in range(len(names)):
    if age[i]>40:
        above_40[names[i]] = age[i]
    elif age[i]<40:
        below_40[names[i]] = age[i]
# print(c)
# print(below_40)
statistic = {"count_above_40":len(list(above_40)), "count_below_40":len(list(below_40))}
out_dict["above_40"]=above_40
out_dict["below_40"]=below_40
out_dict["statistics"]=statistic
outputinjson = json.dumps(out_dict, indent=4)
print(outputinjson)


'''5. You are provided with a JSON structure representing a list of employees in a company. 
Each employee has information such as name, department, and salary. 
Write a program to identify the highest-paid employee in each department and generate a new JSON structure with the department names and the corresponding highest-paid employee details.

Input:
{
  "employees": [
    {"name": "Alice", "department": "HR", "salary": 60000},
    {"name": "Bob", "department": "Engineering", "salary": 80000},
    {"name": "Charlie", "department": "HR", "salary": 70000},
    {"name": "David", "department": "Sales", "salary": 75000},
    {"name": "Eve", "department": "Engineering", "salary": 90000}
  ]
}
Output:
{
  "highest_paid_employees": [
    {"department": "HR", "highest_paid_employee": {"name": "Charlie", "salary": 70000}},
    {"department": "Engineering", "highest_paid_employee": {"name": "Eve", "salary": 90000}},
    {"department": "Sales", "highest_paid_employee": {"name": "David", "salary": 75000}}
  ]
}'''
import json
inp_json = {
  "employees": [
    {"name": "Alice", "department": "HR", "salary": 60000},
    {"name": "Bob", "department": "Engineering", "salary": 80000},
    {"name": "Charlie", "department": "HR", "salary": 70000},
    {"name": "David", "department": "Sales", "salary": 75000},
    {"name": "Eve", "department": "Engineering", "salary": 90000}
  ]
}
json_obj = json.dumps(inp_json, indent=3)
with open("Employees_5.json", 'w') as file:
    file.write(json_obj)
#--------------------------
with open("Employees_5.json", 'r') as file:
     py_obj = json.load(file)
employees = list(py_obj.values())
employees = employees[0]
department = [] 

for dict in employees:
     department.append(dict.get("department"))
     dept = list(set(department))

highest_paid_employees = []
for i in dept:
    dictionary = {}
    salary = []
    name = []
    for j in employees:
          if j["department"] == i:
               salary.append(j["salary"])
               name.append(j["name"])
    max_sal = max(salary)
    ename = name[salary.index(max_sal)]
    dictionary["deplartment"] = i
    dictionary["highest_paid_employee"] = {"name":ename, "salary":max_sal}
    highest_paid_employees.append(dictionary)
print(highest_paid_employees)
