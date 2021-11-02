"""We are going to be calling the defined funtion recursively each time we create the subarray """
def recursivebinarysearch(cards, query, high_index, low_index): 
    if low_index <= high_index: 
        middle_index = (high_index + low_index) //2 
        if query == cards[middle_index]: 
            return middle_index
        elif query < cards[middle_index]: 
            low_index = middle_index +1#descending list 
            return recursivebinarysearch(cards, query,high_index, low_index )
        else: 
            #where query > cards[middle_index]
            high_index = middle_index -1 
            return recursivebinarysearch(cards, query, high_index, low_index)

    else: 
        #When the list is empty 
        return -1 
tests = []
# Query occcurs in the middle(general case)
tests.append({'input':{'cards':[13, 11, 10, 9, 8, 6, 5, 3], 'query':6, 'high_index': 7, 'low_index':0}, 'output':5})
target = recursivebinarysearch(**tests[0]['input'])
print(target)
