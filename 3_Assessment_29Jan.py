'''1.Develop a Python program to create a dictionary from a given string, where each key represents a unique character, 
and the corresponding values denote the count of occurrences.
Input: 'kovan labs'
Output: {'k': 1, 'o': 2, 'v': 1, 'a': 2, 'n': 1, ' ': 1, 'l': 1, 'b': 1, 's': 1}
'''

def main(given_str):
    keylist = list(given_str)
    keyset = set(keylist)
    key = list(keyset)
    value = []
    dic = {}
    print("Keys: ",key)
    for x in keyset:
        value.append(keylist.count(x))
    print("Values: ", value)
    dic = {key[x]:value[x] for x in range(len(key))}
    return dic
print("------------------#1----------------")
input = input("Enter a String: ")
dic = main(input)
print("Output as dictionary:",dic)

'''
2. Create a Python program to find the key with the maximum value in a dictionary.
Input: 
my_dict = {'apple': 10, 'banana': 5, 'orange': 20, 'grapes': 15}
Output: 'orange'
'''

print("------------------#2----------------")
my_dict = {'apple': 10, 'banana': 5, 'orange': 20, 'grapes': 15}
#value = my_dict.values()
#maxvalue = value.max()
print(max(my_dict))

'''
3.Create a Python function that counts the frequency of words in a sentence and returns a dictionary.
Input: 
sentence = "This is a sample sentence. This sentence has words."
Output: {'This': 2, 'is': 1, 'a': 1, 'sample': 1, 'sentence.': 2, 'has': 1, 'words.': 1}


def trim(sentence):
    return sentence.replace(".", "").replace("!", "").lower()

def dict(sentence):
    li = sentence.split(" ")
    keyset = set(li)
    keys = list(keyset)
    value = []
    for x in keys:
        value.append(li.count(x))
    dic = {keys[i]:value[i] for i in range(len(keys))}
    return dic

inp = input("Give me a Sentence: ")
sentence = trim(inp)
output = dict(sentence)
print("------------------#3----------------")
print("Result: ", output)


4.  Write a Python function that takes a dictionary as input and returns a new dictionary where the keys are the original values, and the values are lists containing all corresponding keys.
Input: 
input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}
Output: {1: ['a', 'c'], 2: ['b', 'd'], 3: ['e']}
'''

def func(inp_dict):
    in_values = list(inp_dict.values())
    valueset = set(in_values)
    outdict = {}
    for x in valueset:
        result= ([key for key, value in inp_dict.items() if value==x])
        outdict[x] = result
    return outdict

inp_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}
out_dict = func(inp_dict)
print("------------------#4----------------")
print("Result: ", out_dict)
