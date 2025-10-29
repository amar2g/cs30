def binary_search(x, y): #x = list/data; y = value to be found

    lowerbound = 0 #set start point of search at first index
    upperbound = len(x) - 1 #set end of search at last index
    
    while lowerbound <= upperbound: #search until range is valid
        midpoint = (lowerbound + upperbound) // 2 #calc middle index of range
        if x[midpoint].lower() == y.lower(): #lower function for case sensitivity
            return midpoint #return pos of item
        elif x[midpoint].lower () < y.lower():
            lowerbound = midpoint + 1 #rm left half; lower bound now 1 step right of midpoint
        else:
            upperbound = midpoint - 1 #rm right half; upper bound now 1 step left of midpoint
    
    return -1 #loop breaks if item not found

sea_creatures = ['Angel Shark', 'Bat Ray', 'Big Skate', 'Catshark', 'Cownose Ray', 'Electric Ray', 'Elephant Fish', 'Horn Shark', 'Leopard Shark', 'Reef Shark']

creature_type = ['Ray', 'Fish', 'Shark', 'Ray', 'Shark', 'Fish', 'Shark', 'Shark', 'Fish', 'Ray']

endangered = [True, True, False, False, True, False, False, True, True, False]

print("here are the creatures: ") 

for i in sea_creatures: 
    print(i) #show all creatures in list
print("type 'exit' to quit")

while True: 
    
    user_input = input("enter name of creature: ").strip() #strip functino to remove whitespace
        
    if user_input.lower() == 'exit':
        break #stop loop
        
    result = binary_search(sea_creatures, user_input) #call binary function to search through list
        
    if result == -1: #if binary search function doesnt find item 
        print('creature not in list') 
    else:
        print(f"{sea_creatures[result]} is a {creature_type[result]}") #show the item found
      
    if endangered[result]: #show endangered status
        print("species' endangered")
    else:
        print("species' not endangered") 
        
