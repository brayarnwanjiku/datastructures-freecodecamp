"""The challenge is to find a given number from a sorted list of numbers arranged in decreasing order. 
The goal is to reduce number of turned cards i.e The number of times the list is accessed
input:sorted list, target number. 
sample input: [13, 11, 10, 9, 8, 6, 5, 3]
query: 10
sample output: 2
I will represent my test cases as a dictionary that contains two keys; input and output
example: test_case = {'input': {'cardlist': [13, 11, 10, 9, 8, 6, 5, 3], 'query':10 }, 'output':2}
It is important to note however that this is a general case and there may exist several cases of inputs and outputs: 
    i) The cardlist may be empty(edge case)
    ii) The query occurs in the beggining or the end of the list
    iii) The query is repeated in the list
    iv) The query is the only element in the cardlist
    v) The query is repeated in the cardlist
    v) The query is not in the cardlist(edge case)

we need to create test cases that cater for the different cases(dictionaries) throught of and store them in a list. 
"""
tests = []
# Query occcurs in the middle(general case)
tests.append({'input':{'cards':[13, 11, 10, 9, 8, 6, 5, 3], 'query':6}, 'output':5})
# Query occurs in the beginning of the list 
tests.append({'input':{'cards':[13, 11, 10, 9, 8, 6, 5, 3], 'query':13}, 'output':0})
# Query occurs at the end of the list
tests.append({'input':{'cards':[13, 11, 10, 9, 8, 6, 5, 3], 'query':3}, 'output':7})
# Query occurs as the only element in the list 
tests.append({'input':{'cards':[13], 'query':13}, 'output':0}) 
# Query is not found in the list
# we will specify a -1 if the query is not found in the list
tests.append({'input':{'cards':[13, 11, 10, 9, 8, 6, 5, 3], 'query':7}, 'output':-1})
# The list of cards is empty
# we will specify -1 if the list if empty
tests.append({'input':{'cards':[], 'query':13}, 'output':-1})
# Query is repeated in the cards list 
# The function should return the very first occurence of the query in the list
tests.append({'input':{'cards':[13, 13, 13, 13, 8, 6, 5, 3], 'query':13}, 'output':0})
# Numbers that are not the query repeated severally in the list 
tests.append({'input':{'cards':[13, 11, 10, 9, 8,8, 8,8,8,8,6,6,6,6, 6, 5, 3], 'query':5}, 'output':15}) 

# Implementing the linear solution 
def linear_locate_card(cards, query): 
    #create a position varaible that will be returned by the program 
    position = 0 
    #set a loop for repetition 
    # while True: replaced by while position < len(cards): 
    while position < len(cards):
        if cards[position] == query: #check whether the query is in the current location of our pointer 
            return position #return the position and exit
        position += 1 #increment our position by one if the current location is not our query 
    return -1 #This will be the go to case if the while loop does not result in a positive identification of the query
        
        
print(linear_locate_card(**tests[0]['input']) == tests[0]['output'])

# You can install a python library that uses you test libraries to test your solutions
# pip install jovian and then import it to your code 
from jovian.pythondsa import evaluate_test_case, evaluate_test_cases
# call the evlauate_test_case function to undertand your output better - for a single test case 
evaluate_test_case(linear_locate_card, tests[0])
# to evalueate several test cases, we use the evaluate_test_cases function 
evaluate_test_cases(linear_locate_card, tests)
"""The Linear_locate_card method returns an error in the 6th iteration of the lists since we are trying to access the position on an empty list
We can correct the same by rewriting the function that accomdates an empty list 
Basically we include a condition that that the position must be less than the length of the cards
i.e while position < len(cards) """

print(tests[4])
