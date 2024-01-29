'''
1.Turn every item of a list into its square .Given a list of numbers write a program to turn every item of a list into its square. 
Try to write it in function using both list comprehension, for loop methods separately.
Input : numbers = [1,2,3,4,5] 
Expected Output : [1, 4, 9, 16, 25]'''

li = [1,2,3,4,5]
print("#1")
print("Given list is: ", end=" ")
print(li)
new_li= []
for x in li:
    new_li.append(x*x)
print("New list using for loop:", end=" ")
print(new_li)

#Using comprehension list:
new_li2 = [(x*x) for x in li]
print("New list using Comprehension list:", end=" ")
print(new_li2)


'''
2. Concatenate two lists in the following order
Input:
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
Output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']'''

list1 = ["Hello", "take"] # considered without space in input and added space while append
list2 = ["Dear", "Sir"]
print("#2")
print("List1: ", end=" ")
print(list1)
print("List2: ", end=" ")
print(list2)
new_list = []
for i in range(len(list1)):
    for j in range(len(list2)):
        new_list.append(list1[i]+" "+list2[j]) 
print ("Concatenated output list: ", end=" ")
print(new_list)

'''
3. Remove empty strings from the list of strings
Input:    ["Mike", "", "Emma", "Kelly", "", "Brad"]
output: ['Mike', 'Emma', 'Kelly', 'Brad']'''

list3 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print("#3")
print("Given list: " +str(list3))
#list3.remove("") ## Removes only the first occurance
while "" in list3:
    list3.remove("")
print("Output: " +str(list3))

list3a = ["Mike", "", "Emma", "Kelly", "", "Brad"]
#newli = []
print("Input list:" + str(list3a))
newli = list(filter(None, list3a))
print("Filtered List: " +str(newli))

'''
4. Convert two lists into a dictionary
Input : 
keys = ['Ten', 'Twenty', 'Thirty'] 
values = [10, 20, 30]'''

keys = ['Ten', 'Twenty', 'Thirty'] 
values = [10, 20, 30]
dic = {}
dic = {keys[i]:values[i] for i in range(len(keys))}
print("#4")
print("Lists converted to Dictionary:" +str(dic))

'''
5.  Delete a list of keys from a dictionary
Input : 
sample_dict = {"name": "Kelly",     "age": 25,     "salary": 8000,     "city": "New York"}
Output: {'age': 25, 'city': 'New York'}'''

sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
print("#5")
print("Input Dictionary: "+ str(sample_dict))
#sample_dict.pop("name")
#sample_dict.pop("salary")
del sample_dict["name"]
del sample_dict["salary"]
print("Output Dictionary:" + str(sample_dict))