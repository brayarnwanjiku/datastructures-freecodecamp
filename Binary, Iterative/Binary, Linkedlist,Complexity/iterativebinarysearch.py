"""In the Linearsearch.py we applied a brute force approach to solve our problem where we had to overturn every card in the worst case scenario. 
In retospect, the larger the N, the worse the time complexity (O(N)) - imagine N was 10^6 digits. 
Instead we could pick the card in the middle, and compare to the card on one side which tells us what direction to go based on the order of cards. 
In each iteration, we pick the middle number and compare the target number with the numbers on its sides 
"""

#The test cases for each of the possible input sequences 
from jovian.pythondsa import evaluate_test_case, evaluate_test_cases



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

"""Express the solution in plain english
    1. choose the middle number of the list/array 
    2. compare the middle number to the target number and if equal, return 
    3. if query is less than the query, search the first half of the list else: 
    4. search the second part of the list """

def iterativebinarysearch(cards, query): 
    low_index = 0 
    high_index = len(cards) - 1 
    #introduce a while loop to check whether the list is empty
    while low_index <= high_index: 
        middle_index = (high_index + low_index) // 2 #return only the quotient 
        if query == cards[middle_index]: 
            return middle_index
        elif query < cards[middle_index]: #remmember the list is in descending order
            low_index = middle_index + 1 
        else: 
            high_index = middle_index - 1
    
    return -1 #if the list is empty 

print(iterativebinarysearch(**tests[0]['input']))
#testing all the possible cases 
evaluate_test_cases(iterativebinarysearch, tests)

"""In the above function, one test case fails.
failed test case: {'cards': [13, 13, 13, 13, 8, 6, 5, 3], 'query': 13}
expected output:0 
actual output:3 
This is because after the function locates the instance of the query, it does not consider whether the occurence 
is the only one or a multiple, it just rerurns the first index found. We have to cater for many occurrences of our query 
and ensure the function returns the earliest occurence of the query.  
"""
#define a helper function that checks whether the index reurned is the first occurence of our query
def test_location(cards, query, mid): 
    if cards[mid] == query: 
        #check that we are not at the first element and if the previous index has the same value as our query
        if mid-1 >= 0 and cards[mid-1] == query: 
            return 'left'
        else: 
            return 'found'
    #instnaces where the middle number is less than the query and we have to move left 
    elif cards[mid] < query: 
        return 'left'
    #instances where the middle number is greater than the query and we have to move right(smaller entries)
    else: 
        return 'right'
def locate_card(cards, query): 
    low_index = 0 
    high_index = len(cards) -1
    while high_index >= low_index: 
        middle_index = (high_index + low_index) // 2 
        #call the test_location function 
        result = test_location(cards, query, middle_index)
        #check the return values of the function 
        if result == 'found': 
            return middle_index
        #This will cater for the multiple query apperarances instance
        #we have already found our query but not its first occurrence in this list
        elif result == 'left': 
            high_index = middle_index -1 
        elif result == 'right': 
            low_index = middle_index + 1
    return -1 

evaluate_test_cases(locate_card, tests)#all the test cases eveluate to completion since we have catered for the anomaly 
"""introduce a large test to show the upsides of applying an iterative approach"""
large_test = {
    'input': {'cards':list(range(10000000, 0, -1)), 'query':2}, 
    'output': 9999998
}
result, passed, runtime = evaluate_test_case(iterativebinarysearch, large_test, display=False)
result1, passed1, runtime1 = evaluate_test_case(locate_card, large_test, display=False)
print("Result: {}\nPassed: {}\nExecution Time: {} ms".format(result, passed, runtime))
print("Result: {}\nPassed: {}\nExecution Time: {} ms".format(result1, passed1, runtime1))
"""The functions execute in 0.015, 0.017 ms. 
This is attributed to the time complexity of the function
O(log N)"""
