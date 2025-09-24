data = [5, 2, 10, 1, 50, 7, 22, 73, 67, 12, 5, 3, 99, 91, 17, 50, 3, 1, 61, 45, 22, 23, 2, 84, 7] #initiate the list used for data

def seq_search(x, y, z): #x = some list; y = key; z = the instance
    count = 0 #count the times 'key' is there
    last_index = -1 #starts as -1; stores the last index 'key' was found

    for i in range(len(x)): 
        if x[i] == y: #check if current element matches key
            count += 1 #increase count + 1
            last_index = i #update last index was found
            if count == z:
                return i
    return last_index

print(seq_search(data, 50, 2))