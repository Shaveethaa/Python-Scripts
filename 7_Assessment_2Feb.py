'''1. Write a function to eliminate all special characters for each of strings in a list and just return back alpha strings for each in a list
Input:
['nB~!@#$%^23', 'Gh&*45vD9zL', 'qW@3yU%1r+7X', 'p$*8JmVcBn6F', 'k!2oT&7sPmQ"(l']
Output:
['nB23', 'Gh45vD9zL', 'qW3yU1r7X', 'p8JmVcBn6F', 'k2oT7sPmQl']'''

def func1(input):
    output = []
    for x in input:
        output.append(("".join(y for y in x if y.isalnum())))
    return output
input = ['nB~!@#$%^23', 'Gh&*45vD9zL', 'qW@3yU%1r+7X', 'p$*8JmVcBn6F', 'k!2oT&7sPmQ"(l']
print("Output: ", func1(input))

'''2. Write a function to manipulate the values of list of dictionary. for example, if its int, multiply with 2, str means reverse it, float means, round to nearby number,
Input:
list_of_dicts = [{'a': 5, 'b': 'hello', 'c': 3.14},
    {'x': 10, 'y': 'world', 'z': 7.5}]
Output: [{'a': 10, 'b': 'olleh', 'c': 3}, {'x': 20, 'y': 'dlrow', 'z': 8}]'''

def func2(list_of_dicts):
    
    l = []
    for inp in list_of_dicts:
        d = {}
        key = list(inp.keys())
        #print(key)
        for x in key:
            if isinstance(inp.get(x), int):
                tempval = inp.get(x)*2
                d[x] = tempval
            elif isinstance(inp.get(x), str):
                tempstr = inp.get(x)[::-1]
                d[x] = tempstr
            elif isinstance(inp.get(x), float):       
                tempfloat = round(inp.get(x))
                d[x] = tempfloat
        l.append(d)
    return l
list_of_dicts=[{'a': 5, 'b': 'hello', 'c': 3.14},{'x': 10, 'y': 'world', 'z': 7.5}]
print(func2(list_of_dicts))


'''3. Write a function to manipulate the values of below input as expected
Input:
input_dict = {
    'word1': 'hello',
    'word2': 'level',
    'word3': 'example',
    'word4': 'racecar'
}
Output: {'word1': 'oll*h', 'word2': 'l*v*l - palindrome', 'word3': '*lpmax*', 'word4': 'rac*car - palindrome'}'''

def func3(input_dict):
    newdict = {}
    for key in input_dict.keys():
        newdict[key] = input_dict.get(key)[::-1]
        value = newdict[key].replace("e","*")
        if value == value[::-1]:
            value = value + " - palindrome"
        newdict[key] = value
    return newdict

input_dict = {
    'word1': 'hello',
    'word2': 'level',
    'word3': 'example',
    'word4': 'racecar'}
print(func3(input_dict))

'''4. Given a dictionary with string keys and integer values, transform it into a new dictionary where the keys are the lengths of the original keys, and the values are lists of keys of that length. 
Input: original_dict = {'apple': 5, 'banana': 6, 'orange': 6, 'kiwi': 4, 'grape': 5}
Output: transformed_dict = {4: ['kiwi'], 5: ['apple', 'grape'], 6: ['banana', 'orange']}'''

def func4(original_dict):
    value = set(original_dict.values())
    result_dict = {}
    for x in value:
        temp = [key for key,values in original_dict.items() if values == x]
        result_dict[x] = temp
    return result_dict
original_dict = {'apple': 5, 'banana': 6, 'orange': 6, 'kiwi': 4, 'grape': 5}
print(func4(original_dict))

'''5. Given a list of dictionaries representing student information, where each dictionary has keys 'name', 'subject', and 'marks', 
write a Python function to transform the list into a dictionary where each subject is a key, and the value is a list of students who scored the highest marks in that subject.
Input:
student_data = [
    {'name': 'Alice', 'subject': 'Math', 'marks': 90},
    {'name': 'Bob', 'subject': 'Math', 'marks': 85},
    {'name': 'Alice', 'subject': 'Physics', 'marks': 88},
    {'name': 'Bob', 'subject': 'Physics', 'marks': 92},
    {'name': 'Alice', 'subject': 'Chemistry', 'marks': 78},
    {'name': 'Bob', 'subject': 'Chemistry', 'marks': 88}]
Output:
highest_scorers = {
    'Math': ['Alice'],
    'Physics': ['Bob'],
    'Chemistry': ['Bob']}'''

def func5(student_data):
    tsub = []
    highest_scorers = {}
    for dict in student_data:
        tsub.append(dict.get("subject"))
        subject = set(tsub)    
    #print(list(subject))
    for i in subject:
        list1 = []
        mark_list = []
        name_list = []
        for x in range(len(student_data)):
            if student_data[x]["subject"] == i:
                mark_list.append(student_data[x]["marks"])
                name_list.append(student_data[x]["name"])
        index = mark_list.index(max(mark_list))
        #print(i,name_list[index])
        highest_scorers[i] = [name_list[index]]
    print(highest_scorers)

student_data = [
    {'name': 'Alice', 'subject': 'Math', 'marks': 90},
    {'name': 'Bob', 'subject': 'Math', 'marks': 85},
    {'name': 'Alice', 'subject': 'Physics', 'marks': 88},
    {'name': 'Bob', 'subject': 'Physics', 'marks': 92},
    {'name': 'Alice', 'subject': 'Chemistry', 'marks': 78},
    {'name': 'Bob', 'subject': 'Chemistry', 'marks': 88}]
func5(student_data)

