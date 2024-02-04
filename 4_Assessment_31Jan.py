'''1. Write a program to iterate the first 5 numbers, and in each iteration, print the sum of the current and previous number at the end.
Expected Output:
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5
Current Number 4 Previous Number  3  Sum:  7'''

def itr():
    for x in range(5):
        if x == 0:
            print(f'Current Number {x} Previous Number {x} Sum: {x}')
        else:
            prev = x-1
            sum = x + prev
            print(f'Current Number {x} Previous Number {prev} Sum: {sum}')
itr()

'''2. Write a Program to extract each digit from an integer in the reverse order.
or example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.'''

i=0
while i == 0:
    try:
        num = input("Enter an integer: ")
        numb = int(num)
        print("Given number is: ", num)
        i=1
    except ValueError:
        print("Enter valid integer:")
#num = input("Enter an integer: ")
print("Output is: ", " ".join(reversed(num)))

'''3. Create a list by picking an odd-index items from the first list and even index items from the second
Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.
Input:
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
Output:
Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]
Printing Final third list
[6, 12, 18, 4, 12, 20, 28]'''

def odd(li):
    for x in range(len(li)):
        if x%2!=0:
            l_odd.append(l1[x])
    return l_odd
def even(li):
    for x in range(len(li)):
        if x%2==0:
            l_even.append(l1[x])
    return l_even
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l_odd = []
l_even = []
oddlist = odd(l1)
evenlist = even(l2)
print("Odd index values from List 1: ", oddlist)
print("Odd index values from List 2: ", evenlist)
l3 = oddlist + evenlist
print("Printing Final third list", l3)

'''4. Find words with both alphabets and numbers
Write a program to find words with both alphabets and numbers from an input string.
Input:
str1 = "Emma25 is Data scientist50 and AI Expert"
Output:
Emma25
scientist50'''

def func(str):
    for x in str:
        if x.isalpha():
            continue
        elif x.isnumeric():
         continue
        else:
            print(x)
str1 = "Emma25 is Data scientist50 and AI Expert"
str = str1.split()
func(str)


'''5. Write a Python program to find the second maximum and second minimum elements in a given list of numbers. Assume that the list has at least two distinct elements.
Input:
[55, 23, 78, 12, 67, 34, 89, 9, 43]
Output:
Second Maximum: 78
Second Minimum: 12'''

# def method1():
#     inp = [55, 23, 78, 12, 67, 34, 89, 9, 43]
#     inp_sort = sorted(inp)
#     print(inp_sort)
#     print("Second Maxmimum: ", inp_sort[-2])
#     print("Second Minimum: ", inp_sort[1])

# def method2():
#     inp_str = input("Enter a list of numbers using space:")
#     str_list = inp_str.split()
#     sorted_str_list = sorted(str_list)
#     #print(sorted_str_list)
#     print("Second Maxmimum: ", str_list[-2])
#     print("Second Minimum: ", str_list[1])

def method3(list):
    # inp_sort = sorted(list)
    list.sort()
    print("Second Maxmimum: ", list[-2])
    print("Second Minimum: ", list[1])
input_string = input("Enter a list of numbers:")
# To covert to list
x=input_string.strip("[]")
y = x.split(", ")
inp_list = [eval(i) for i in y]
method3(inp_list)

