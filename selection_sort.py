def selection_sort(x): #x = list/data
    n = len(x) #find num of items in list
    for i in range(n): #iterate through all 
        min_index = i #assume first item is smallest
        for j in range(i + 1, n): #itereate through rest
            if x[j] < x[min_index]: #find smaller num
                min_index = j #change min to that smaller num
        x[i], x[min_index] = x[min_index], x[i] #swap smallest with first item
    return x
