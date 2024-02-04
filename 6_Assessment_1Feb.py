'''1. Write a function in Python to read lines from a text file "notes.txt". 
Your function should find and display the occurrence of the word "the".
For example: If the content of the file is:
India is the fastest-growing economy. India is looking for more investments around the globe. 
The whole world is looking at India as a great market. Most of the Indians can foresee the heights that India is capable of reaching.'''

# def create_write_file():
#     file = open("Samplefile.txt", "w")
#     file.write("India is the fastest-growing economy. India is looking for more investments around the globe. The whole world is looking at India as a great market. Most of the Indians can foresee the heights that India is capable of reaching.")
# create_write_file()
def str_occurance():
    file = open("Samplefile.txt", "r")
    content = file.read()
    print("File content: ", content)
    li = content.split()
    count = 0
    #count = (count+1 for i in li if i.lower=='the')
    for i in li:
        if i.lower() =='the':
            count = count+1
    return count

cnt = str_occurance()
print(f'The word "the" occurs {cnt} times')

'''2. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.
Input:
A boy is playing there.
There is a playground.
An aeroplane is in the sky.
Alphabets & numbers are allowed in password.
This is Path Walla Website.
Output :-
Word with length smaller than 3 :-'''
# def create_write_file():
#     file = open("story.txt", "w")
#     file.write("A boy is playing there. There is a playground. An aeroplane is in the sky. Alphabets & numbers are allowed in password. This is Path Walla Website.")
# create_write_file()
def display_words():
    with open("story.txt", 'r') as file:
        final_list = []
        content = file.read()
        print("File content:\n", content)
        li1=content.split("\n")
        for li in li1:
            li2 = li.split()
            for x in li2:
                if len(x)<4:
                    final_list.append(x)
        return final_list

final_list = display_words()
print("Words with less than 4 characters:\n", final_list)


'''3.Write a Python program to add the subject_mark and update for every students in the list of dictionary format.
Input:  [{"name":"Arun","subject_mark":{"maths":98,"Science":89,"Social":79,"Tamil":98,"English":67}}, 
        {"name":"Bhuvan","subject_mark":{"maths":90,"Science":97,"Social":89,"Tamil":78,"English":60}},
        {"name":"Rajesh","subject_mark":{"maths":70,"Science":94,"Social":99,"Tamil":85,"English":80}}]
Output: [{'name': 'Arun', 'subject_mark': {'maths': 98, 'Science': 89, 'Social': 79, 'Tamil': 98, 'English': 67}, 'Total_mark': 431}, 
         {'name': 'Bhuvan', 'subject_mark': {'maths': 90, 'Science': 97, 'Social': 89, 'Tamil': 78, 'English': 60}, 'Total_mark': 414},
         {'name': 'Rajesh', 'subject_mark': {'maths': 70, 'Science': 94, 'Social': 99, 'Tamil': 85, 'English': 80}, 'Total_mark': 428}]'''

def func(input):
    list1 = []
    for i in input:
        total = 0
        subjects = list(i["subject_mark"].keys())
        for j in subjects:
            total = total + (i["subject_mark"][j])
        i["Total_mark"] = total
        list1.append(i)
    return list1
input = [{"name":"Arun","subject_mark":{"maths":98,"Science":89,"Social":79,"Tamil":98,"English":67}}, 
        {"name":"Bhuvan","subject_mark":{"maths":90,"Science":97,"Social":89,"Tamil":78,"English":60}},
        {"name":"Rajesh","subject_mark":{"maths":70,"Science":94,"Social":99,"Tamil":85,"English":80}}]
output = func(input)
print("Output: ", output)

'''4. Write a Python function called generate_random_passwords that takes two parameters: 
num_passwords (an integer representing the number of passwords to generate) and length (an integer representing the length of each password). 
The function should generate random passwords with the following criteria:

Passwords starting with numbers 100 to 105 should follow a specific pattern: the number followed by a mix of uppercase letters, lowercase letters, and digits.
For the remaining passwords, generate them randomly with a mix of uppercase letters, lowercase letters, and digits.

Expected Output:
Password 1: 100TwGDg
Password 2: 101F5j3v
Password 3: 102Kp7uL
Password 4: 103Fv2A1
Password 5: 104dRm9z'''

import random, string

def generate_random_passwords(num_passwords, length):
    rlist = []
    rletter = string.ascii_letters + string.digits
    len = length-3
    for i in range(num_passwords):
        r1 = str(random.choice(range(100,106)))
        r2 = ""
        for j in range(len):
            r2 = r2 + str(random.choice(rletter))
        print(f'Password {i+1}:', r1+r2)

num_passwords = int(input("Enter the number of passwords to generate: "))
length = int(input("Enter the length of each password: "))
generate_random_passwords(num_passwords, length)

'''5. Write a Python code to transform a list of lists in given input, into a dictionary of dictionaries named people_dict_of_dicts where each person is assigned a unique index, and a separate dictionary named people_indexed that categorizes individuals by their gender, listing the corresponding indices for males and females?
Input:
people_list_of_lists = [
    ['John', 25, 'Male'],
    ['Jane', 30, 'Female'],
    ['Alex', 22, 'Male'],
    ['Emily', 28, 'Female'],
    ['Michael', 35, 'Male'],
    ['Sophia', 26, 'Female'],
    ['Daniel', 31, 'Male'],
    ['Olivia', 29, 'Female'],
    ['William', 27, 'Male'],
    ['Ava', 32, 'Female'],
]
 
Output:
a) people_dict_of_dicts = {"1":{"name": "John", "age": 25, "gender": "Male"},"2":{"name": "Jane", "age": 30, "gender": "Female"},"3":{"name": "Alex", "age": 22, "gender": "Male"},"4":{"name": "Emily", "age": 28, "gender": "Female"},"5":{"name": "Michael", "age": 35, "gender": "Male"},"6":{"name": "Sophia", "age": 26, "gender": "Female"},"7":{"name": "Daniel", "age": 31, "gender": "Male"},"8":{"name": "Olivia", "age": 29, "gender": "Female"},"9":{"name": "William", "age": 27, "gender": "Male"},"10":{"name": "Ava", "age": 32, "gender": "Female"}}

b) people_indexed = {"male":[1,5,7,9],"female":[2,4,6,8,10]}'''

people_list_of_lists = [
    ['John', 25, 'Male'],
    ['Jane', 30, 'Female'],
    ['Alex', 22, 'Male'],
    ['Emily', 28, 'Female'],
    ['Michael', 35, 'Male'],
    ['Sophia', 26, 'Female'],
    ['Daniel', 31, 'Male'],
    ['Olivia', 29, 'Female'],
    ['William', 27, 'Male'],
    ['Ava', 32, 'Female'],
]

people_dict_of_dicts = {}
people_indexed = {}
male = []
female = []
for i in range(len(people_list_of_lists)):#10
    #for j in range(len(people_list_of_lists[i])):#3
    name = ""
    name = (people_list_of_lists[i][0])
    age = people_list_of_lists[i][1]
    gender = people_list_of_lists[i][2]
    people_dict_of_dicts[(i+1)] = {"name":name, "age":age, "gender":gender}
    if gender == "Male":
        male.append(i+1)
    elif gender == "Female":
        female.append(i+1)
    #print("people_dict_of_dicts = ", people_dict_of_dicts)
print("people_dict_of_dicts:\n", people_dict_of_dicts)
people_indexed["male"] = male
people_indexed["female"] = female
print("people_indexed:\n", people_indexed)


