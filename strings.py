# Program to demonstrate use of strings and lists
list1 = ['kashmir', 'syria', 'afganistan']
print(list1)
list1.sort()
print("The sorted list is as : ")
print(list1)
motorcycles = []
motorcycles.append('Enfield')
motorcycles.append('Pulsar')
motorcycles.append('Avenger')
print(motorcycles)
print(motorcycles[-1])  # Showing the last element of an array
message = f"My first bike was :  {motorcycles[1].title()}."  # title() makes the element at specified location to the title case
print(message)
motorcycles.insert(2, 'Apache') # insert element at a specific location using using insert() function
print(motorcycles.pop())  # use pop() to remove an item from any position in a list by including the index
print(motorcycles)
motorcycles.append('Avenger')
motorcycles.remove('Pulsar')  # use remove() when you know the value of the item to be removed
print(motorcycles)
motorcycles.sort(reverse=True)
print(motorcycles)
#  Lists introduction
list2 = []
for x in range(0, 9):
	list2[x] = x

print(list2)


#motorcycles.pop()

