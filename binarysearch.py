L = [3, 14, 27, 31, 39, 42, 55, 70, 74, 81, 85, 93, 98] #13 items; length = 12 

def binary_search(x, y): #x = list/data; y = value to be found

    lowerbound = 0 #set start point of search at first index
    upperbound = len(x) - 1 #set end of search at last index
    
    while lowerbound <= upperbound: #search until range is valid
        midpoint = (lowerbound + upperbound) // 2 #calc middle index of range
        if x[midpoint] == y:
            return midpoint #return pos of item
        elif x[midpoint] < y:
            lowerbound = midpoint + 1 #rm left half; lower bound now 1 step right of midpoint
        elif x[midpoint] > y:
            upperbound = midpoint - 1 #rm right half; upper bound now 1 step left of midpoint
    
    return -1 #loop breaks if item not found

print(binary_search(L, 98))