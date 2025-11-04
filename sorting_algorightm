from my_functions import binary_search
from selection_sort import selection_sort

my_friends = ["Dhungana","Li","Jones","Saley","Ma","Wage","Premkumar","Han","Bhattarai","Ahmed","Miller","Brown","Lee","Woo","Smith"]
#print list
print(f"Unsorted List: {my_friends}")
#sort list using selection sort
selection_sort(my_friends)
#result of the sorting 
output = "SortedList: "
#gothrough every name and index
for i, name in enumerate(my_friends):
  output += f"{name}, "
  #make them all lowercase
  my_friends[i] = name.lower()

print(output)

while True:
    user_name = input("Enter a last name to search: ").lower()

    index = binary_search(my_friends, user_name)

    if index == -1:
        print("Sorry, I did not find your name")
    else:
        print(f"This is the {index + 1}th person in the sorted list")
