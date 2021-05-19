#  *****************  LISTS  ***********************
list1 = [10, 20, 30, 35]
for i in range(0, 4):
	list1[i] = list1[i] + 5
print(list1)

# ******************* 2D LIST  *********************
list2 = [['Sami', 'Ji'], [10, 12, 14, 16]]
print(list2)
print(list2[0])
print(list2[1])
print(list2[0][1])
print(list2[1][2])

#  *****************  LIST SLICES  *****************
list3 = ['apple', 'pear', 'grapes', 'mango']
print(list3[0:4])
print(list3[:2])
print(list3[1:3])
print(list3[0:])
print(list3[2:])
print(list3[:])

#  *****************  LIST CONCATENATION (+) AND REPLICATION (*)  ******************
list4 = list1 + list3  # List concatenation
print(list4)
list4 = list4 * 2  # List replication
print(list4)
list4 = list4 + [100, 200]
print(list4)
del list4[-1]  # delete elements form the list using index
print(list4)

#  **************** using in and not operators with lists  ********************
if 35 in list4:  # return true if 35 is in list4
	print('Element found')
if 'apple' not in list4:  # return true if specified element not present in the list
	print('Element not found in the list')

#  **************** Multiple assignment trick or tuple unpacking  ******************
list5 = ['Whale', 'Dark-Blue', '500kg']
animal, color, weight = list5  # initializing variables using list name
print(animal, color, weight)
#  **************** USING enumerate() FUNCTION WITH LISTS  *******************
for index, item in enumerate(list5):  # enumerate() returns index and item of the specified list
	print('Index ' + str(index) + ' in list5 is : ' + item)

#  **************** USING choice() and shuffle() FUNCTIONS from random MODULE  *******************
import random
people = ['Owais', 'Zubair', 'Aijaz', 'Shoub']
print(random.choice(people))  # random.choice(listName) returns a randomly selected value from the list
random.shuffle(people)  # random.shuffle() reorder the items in a list
print(people)

#  ****************  TUPLE IS SIMILAR TO A LIST BUT IT IS IMMUTABLE  LIKE STRINGS  ******************
states = ('Kashmir', 'Goa', 'Delhi', 'Blore', 'Mumbai')  # parenthesis are used in case of tuple
print(states)
print(states[3])
print(states[1:])


