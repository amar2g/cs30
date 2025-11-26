def selection_sort(x): #x = list/data
    n = len(x) #find num of items in list
    for i in range(n): #iterate through all 
        min_index = i #assume first item is smallest
        for j in range(i + 1, n): #itereate through rest
            if x[j] < x[min_index]: #find smaller num
                min_index = j #change min to that smaller num
        x[i], x[min_index] = x[min_index], x[i] #swap smallest with first item
    return x

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

output = "sorted list: " # sorted list
friends= ["kaiden","juan","richard","diego","kevin","yash","navit","peyton","ian","ethan","evan","sanjith","frederick","mateo","clinton"]

selection_sort(friends) 

for i, name in enumerate(friends): #return an index and value
  output += f"{name}, "
  friends[i] = name.lower() # make all values lowercase

print(output)

while True:
    user_name = input("search name: ").lower()

    index = binary_search(friends, user_name)

    if index == -1:
        print("sorry i didn't find your name")
    else:
        print(f"this is the {index + 1}th person in the sorted list")    
