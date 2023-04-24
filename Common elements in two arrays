'''Coding challenge:

Write a function that takes two arrays of integers as arguments, 
and returns an array of integers containing only the elements that are present in both arrays. 
The input arrays are unsorted.

For example, if the first arrays is [3,1,4,2] and the second array is 
[2,4,6,8,1], the function should return [1,2,4].

The function should return an empty array if there are no common elements between the two arrays.
'''


Array1 = [] #Empty arrays for the user to fill
Array2 = [] 

while True: #Make sure that an integer is entered, give error message if not.
    try:
        n1 = int(input("Enter number of elements in the first array: ")) #User inputs size of array
        break
    except ValueError:
        print("Please enter an integer.")


for i in range(0,n1): # Fill the empty arrays with integers entered by the user, starting from position 0 to n1-1.
    while True: # Make sure that an integer is entered, give error message if not.
        try:
            ele = int(input("Enter element " + str(i) + ": ")) 
            break
        except ValueError:
            print("Please enter an integer.")
    Array1.append(ele) #Adds the element into the array.

#Same as the first array
while True: #Make sure that an integer is entered, give error message if not.
    try:
        n2 = int(input("Enter number of elements in the first array: ")) #User inputs size of array
        break
    except ValueError:
        print("Please enter an integer.")

for i in range(0,n2): #Same as first array
    while True: # Make sure that an integer is entered, give error message if not.
        try:
            ele = int(input("Enter element " + str(i) + ": ")) 
            break
        except ValueError:
            print("Please enter an integer.")
    Array2.append(ele) 

#Function to check elements that are in both arrays
def array_match(Array1,Array2):
    result = []
    for element1 in Array1: #Check each element in Array 1 with each element in Array2
        for element2 in Array2:
            if element1 == element2: #If the elements match, are in both arrays, the element is put into result
                result.append(element1)  
                break #Skip other comparision after first match
    result.sort() #Sort the list
    return result #Return result




print(array_match(Array1,Array2)) #Call the function and print the result
