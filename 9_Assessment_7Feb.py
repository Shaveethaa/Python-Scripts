'''1. Given a JSON structure representing employees and their skills, write a Python program to generate a new JSON structure mapping each skill to the employees possessing that skill.

Input:
{
  "employees": [
    {"name": "Alice", "skills": ["Python", "Java"]},
    {"name": "Bob", "skills": ["C++", "Python", "JavaScript"]},
    {"name": "Charlie", "skills": ["Java", "JavaScript"]},
    {"name": "David", "skills": ["Python", "C#"]},
    {"name": "Eve", "skills": ["JavaScript", "HTML", "CSS"]}
  ]
}

Output:
{
  "skill_mapping": {
    "Python": ["Alice", "Bob", "David"],
    "Java": ["Alice", "Charlie"],
    "C++": ["Bob"],
    "JavaScript": ["Bob", "Charlie", "Eve"],
    "C#": ["David"],
    "HTML": ["Eve"],
    "CSS": ["Eve"]
  }
}'''
import json
inp = {
  "employees": [
    {"name": "Alice", "skills": ["Python", "Java"]},
    {"name": "Bob", "skills": ["C++", "Python", "JavaScript"]},
    {"name": "Charlie", "skills": ["Java", "JavaScript"]},
    {"name": "David", "skills": ["Python", "C#"]},
    {"name": "Eve", "skills": ["JavaScript", "HTML", "CSS"]}
  ]
}

for emp in inp.get("employees"):
    name = emp.get("name")
    skill = emp.get("skills")
empl = {name:skill for name, skill in zip(name, skill)}
#print(empl)
skills = list(set(sum(skill, [])))
output_dict = {}
skill_mapping = {}
for each in skills:
    skill_mapping_name = []
    for x in name:
        if each in empl.get(x):
            skill_mapping_name.append(x)
        else:
            continue
    skill_mapping[each] = skill_mapping_name
output_dict["skill_mapping"] = skill_mapping
json_ob = json.dumps(output_dict, indent = 3)
print("Output: ", json_ob)


'''2a) Given the JSON data provided, write a function that returns the total number of completed projects across all departments.
Expected output: Total number of completed projects: 2'''

inp_company = {
  "company": "InnovateTech",
  "location": "Metropolis",
  "departments": [
    {
      "name": "Engineering",
      "manager": "Amit Sharma",
      "employees": [
        {
          "id": 1,
          "name": "Sunita Patel",
          "position": "Software Engineer",
          "salary": 95000,
          "projects": [
            {
              "name": "AI Chatbot Development",
              "status": "In Progress"
            },
            {
              "name": "Data Analytics Dashboard",
              "status": "Completed"
            }
          ]
        },
        {
          "id": 2,
          "name": "Rahul Singh",
          "position": "DevOps Engineer",
          "salary": 105000,
          "projects": [
            {
              "name": "Continuous Integration Pipeline",
              "status": "In Progress"
            }
          ]
        },
        {
          "id": 3,
          "name": "Deepa Sharma",
          "position": "Frontend Developer",
          "salary": 90000,
          "projects": [
            {
              "name": "User Interface Redesign",
              "status": "Completed"
            }
          ]
        }
      ]
    },
    {
      "name": "Marketing",
      "manager": "Neha Verma",
      "employees": [
        {
          "id": 4,
          "name": "Aryan Khan",
          "position": "Marketing Manager",
          "salary": 110000,
          "campaigns": [
            {
              "name": "Product Launch Campaign",
              "status": "In Progress"
            }
          ]
        },
        {
          "id": 5,
          "name": "Neha Gupta",
          "position": "Digital Marketer",
          "salary": 80000,
          "campaigns": [
            {
              "name": "Social Media Campaign",
              "status": "Completed"
            }
          ]
        }
      ]
    }
  ]
}

def completed_proj(depart):
    count = 0
    for each in depart:
        emp.append(each.get("employees"))
        empl = sum(emp,[])
    for each in empl:
        proj.append(each.get("projects"))
        if each.get("projects") is not None:
            projects = sum(proj, [])
    for each in projects:
        if each["status"] == "Completed":
            count = count+1
        else:
            continue
    print("Total number of completed projects: ", count)
emp = []
proj = []

completed_proj(inp_company["departments"])

'''b) Using the JSON data, generate a report that lists all employees along with their positions and salaries, sorted in descending order of salaries.
Expected Output: 
Employee Report:
Name: Aryan Khan, Position: Marketing Manager, Salary: 110000
Name: Rahul Singh, Position: DevOps Engineer, Salary: 105000
Name: Sunita Patel, Position: Software Engineer, Salary: 95000
Name: Deepa Sharma, Position: Frontend Developer, Salary: 90000
Name: Neha Gupta, Position: Digital Marketer, Salary: 80000'''

def emp_report(depart):
    for each in depart:
        emp.append(each.get("employees"))
        empl = sum(emp,[])
    for each in empl:
        #print(each)
        #li.append(f"Name: {each.get("name")}, Position: {each.get("position")}, Salary: {each.get("salary")}")
        dict = {"Name": each.get("name"), "Position":each.get("position"), "Salary":each.get("salary")}
        li.append(dict)
    sorted_list = sorted(li, key=lambda x: x['Salary'], reverse = True)
    print("Emplyee Report:")
    for each in sorted_list:
        print(f"Name: {each.get("Name")}, Position: {each.get("Position")}, Salary: {each.get("Salary")}")
    #print(sorted_list)
emp = []
li=[]
emp_report(inp_company["departments"])

'''c) Extend the JSON data to include a new department called "Finance" with a manager named "Rajesh Kumar". 
Then, write a function to update the JSON with a new employee in the Finance department. The new employee's details are:

Name: Priya Mehta
Position: Financial Analyst
Salary: 95000
Expected output: given details should be added to existing json and print the updated json in terminal.'''
import json

def update_json(company, new_emp):
    existing_dep_list = company.get("departments")
    for each in existing_dep_list:
        #print(type(each))
        if each.get("name") == "Finance":
            each["employees"] = new_emp
    #print(type(existing_dep_list))
    company["departments"] = existing_dep_list
    return company

new_dept = {"name": "Finance", "manager": "Rajesh Kumar"}
new_emp = {"name": "Priya Mehta", "position": "Financial Analyst", "salary": 95000}

inp_company["departments"].append(new_dept)
comp = json.dumps(inp_company, indent = 3)
updated_company_dict = update_json(inp_company, new_emp) #calling function
updated_company_json = json.dumps(updated_company_dict, indent = 3)
#print(updated_company_json)
#print(type(updated_company_dict))
'''d) Utilizing the provided JSON, create a report that lists all ongoing projects, along with the department they belong to and their respective managers.

Expected Output:
Ongoing Projects Report:
Project: AI Chatbot Development, Department: Engineering, Manager: Amit Sharma
Project: Continuous Integration Pipeline, Department: Engineering, Manager: Amit Sharma
Project: Product Launch Campaign, Department: Marketing, Manager: Neha Verma'''

def ongoing_proj(depart):
    for eachdep in depart:
        for eachemp in eachdep.get("employees"):
            if isinstance(eachemp, dict):
                if "projects" in eachemp.keys():
                    for eachproj in eachemp.get("projects"):
                        if eachproj.get("status") == 'In Progress':
                            print(f"Project: {eachproj.get("name")}, Department: {eachdep.get("name")}, Manager: {eachdep.get("manager")}")
                        else:
                            continue
                if "campaigns" in eachemp.keys():
                    for eachproj in eachemp.get("campaigns"):
                        if eachproj.get("status") == "In Progress":
                            print(f"Project: {eachproj.get("name")}, Department: {eachdep.get("name")}, Manager: {eachdep.get("manager")}")
                        else:
                            continue

# updated_company_pythonformat = json.load(updated_company_dict)
# print(type(updated_company_pythonformat))
print("Ongoing Projects Report:")
ongoing_proj(updated_company_dict["departments"])

'''e) Given the JSON structure, write a function that calculates the average salary for each department.
Expected Output:
Average Salaries for Each Department:
Engineering: 96833.33333333333
Marketing: 95000.0
Finance: 95000.0'''

def average(sal):
    return sum(sal)/len(sal)

for dep in updated_company_dict["departments"]:
  if dep["name"] == 'Finance':
     finsal = dep["employees"]["salary"]
     print(dep["name"], average(finsal))
  else:
    sal = []
    for emp in dep["employees"]:
      if type(emp) == dict:
        sal.append(emp.get("salary"))
      else:
        continue
    if len(sal) !=0:
      print(dep["name"], average(sal))

    