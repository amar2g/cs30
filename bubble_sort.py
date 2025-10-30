list = [89,45,68,90,29,34,17]

def bubble_sort(x): #x = list/data
    n = len(x) #find num of items in list
    for i in range(n - 1): #repeat 1 less than num of items in list
        for j in range(n - i - 1): #check on less element in list
            if x[j] > x[j + 1]: #check if current num bigger than next
                x[j], x[j + 1] = x[j + 1], x[j] #swap their places
    return x

print(bubble_sort(list))
