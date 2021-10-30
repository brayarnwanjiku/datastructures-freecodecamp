"""In the Linearsearch.py we applied a brute force approach to solve our problem where we had to overturn every card in the worst case scenario. 
In retospect, the larger the N, the worse the time complexity (O(N)) - imagine N was 10^6 digits. 
Instead we could pick the card in the middle, and compare to the card on one side which tells us what direction to go based on the order of cards. 
In each iteration, we pick the middle number and compare the target number with the numbers on its sides 
"""

#The test cases for each of the possible input sequences 
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
def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
        
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1  
        elif mid_number > query:
            lo = mid + 1
    
    return -1

print(locate_card(**tests[0]['input']) == tests[0]['output'])