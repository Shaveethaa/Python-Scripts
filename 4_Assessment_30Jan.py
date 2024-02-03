'''1. Write a Python program to filter a dictionary based on values.
Input: Original Dictionary: {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
Output: Marks greater than 170: {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}'''

def func(orig_dic):
    result = {keys:values for keys, values in orig_dic.items() if values>170}
    return result

orig_dic = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
print("-------#1----------")
print("Input Dictionary: ", orig_dic)
output = func(orig_dic)
print("items greater than 170:", output)

'''
2. Write a Python program to convert more than one list to a nested dictionary.
Input : Original strings:
['S001', 'S002', 'S003', 'S004']
['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
[85, 98, 89, 92]
Output: Nested dictionary: [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
'''

def nested_dict(l1, l2, l3):
    dict = [{k1:{k2:k3} for k1,k2,k3 in zip(l1,l2,l3)}]
    print("Expected result: ", dict)

l1 = ['S001', 'S002', 'S003', 'S004']
l2 = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
l3 = [85, 98, 89, 92]
print("-------#2----------")
nested_dict(l1,l2,l3)

'''
3. Write a Python program to extract and print the phone number of a specific employee from a nested dictionary.
Input:
employee_data = {
    'Alice': {'position': 'Manager', 'phone': '123-456-7890'},
    'Bob': {'position': 'Developer', 'phone': '987-654-3210'},
    'Charlie': {'position': 'Analyst', 'phone': '555-123-4567'}
}
Expected Output: Phone number for Bob: 987-654-3210'''


employee_data = {'Alice': {'position': 'Manager', 'phone': '123-456-7890'},
                 'Bob': {'position': 'Developer', 'phone': '987-654-3210'},
                 'Charlie': {'position': 'Analyst', 'phone': '555-123-4567'}}
name = input("Enter any one employee name from the list (Alice, Bob, Charlie): ")
new = name.capitalize()
print("-------#3----------")
#if new in 'Alice' or 'Bob' or 'Charlie':
if new=='Alice' or new=='Bob' or new=='Charlie':
    print(employee_data[new]['phone'])
else:
    print("Sorry!Incorrect name.")

'''
4. You are given a nested dictionary representing a catalog of products in an online store. Each product has various attributes 
such as name, price, and availability. Write a Python program to find and print the names of products that are both affordable 
(price less than $50) and currently available.
Input:
product_catalog = {
    'Laptop': {'price': 1200, 'availability': True},
    'Headphones': {'price': 30, 'availability': True},
    'Smartphone': {'price': 600, 'availability': False},
    'Tablet': {'price': 40, 'availability': True},
    'Camera': {'price': 150, 'availability': False}
}
Expected Output: Affordable and Available Products: ['Headphones', 'Tablet']
'''

product_catalog = {'Laptop': {'price': 1200, 'availability': True},
    'Headphones': {'price': 30, 'availability': True},
    'Smartphone': {'price': 600, 'availability': False},
    'Tablet': {'price': 40, 'availability': True},
    'Camera': {'price': 150, 'availability': False}}

key = list(product_catalog.keys())
# prod = []
# for x in key:
#     if(product_catalog[x]["price"] < 50 and product_catalog[x]["availability"] == True):
#         prod.append(x)
# print("Affordable and Available Products: ", prod)
print("-------#4----------")
prod1 = [x for x in key if product_catalog[x]["price"] < 50 and product_catalog[x]["availability"] == True]
print("Affordable and Available Products: ", prod1)