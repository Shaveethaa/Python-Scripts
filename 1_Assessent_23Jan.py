'''
#1 Write a code that takes a string as input and returns the reversed version of that string. 
For example expected output should be like reversed_output = "nohtyp"
'''
sample = input("Enter a String: ")
print("Given String is : " + sample)
reverse = sample[::-1]
print("Reversed String is : " + reverse)


'''
#2 Given two different lists and tuples, write a Python code to merge these two different lists and tuples and store the result in a new items called "combined_list." 
for each, expected output should be in combined lists and combined tuple format.
'''

l1 = ['Red', 'Orange', 'Pink']
l2 = ['Blue', 'Purple', 'Violet']
print("List 1: " + str(l1))
print("List 2: "+ str(l2))
tup1 = (1,2,3,4,5)
tup2 = (10,20,30,40,50)
l1.extend(l2)
combined_tuple = tup1 +tup2
print("Combined List: ", end=" ")
print(l1)
print("Tuple1: " + str(tup1))
print("Tuple2: " + str(tup2))
print("Combined Tuple: ", end=" ")
print(combined_tuple)


'''
#3 Write a code that takes a string and a target substring as input and returns the number of occurrences of the target substring in the given string. 
For example, if the input is "pythonpythonpython" and the target substring is "on," the output should be 3.
'''

String = input("Enter a String: ")
Target_substring = input ("Enter the substring: ")
a = String.count(Target_substring)
print("Number of occurences of the target substring is: " + str(a))


'''
#4 write a python code to achieve the expected output below mentioned
text  = "#orange#strawberry#grapes#banana"
result = ['orange', 'strawberry', 'grapes', 'banana']
'''
text = "#orange#strawberry#grapes#banana"
print("Given Text is :" + text)
li = text.split("#")
new_li = li[1:]
print("Result: " + str(new_li))