currentBook = {'title':'Marching Powder', 'author':'Rusty Young', 'price':21.80}

# print out the dictionary objects
print(currentBook)
print('\n')

# print author from dictionary
print(currentBook['author'])

#include ISBN into dictionary
currentBook['ISBN'] = '031233034'

print('\n')
#print all values of dictionary
print("the current book has these attributes:")
for key in currentBook:
    print(currentBook[key])

print('\n')
#print all values of dictionary
print ("the current book has these values:")
for value in currentBook.values():
 print (" => {}".format(value))

print('\n')
# creating a dictorary using a constrictor
student = dict(firstname = "joe", lastname="bloggs")
print(student)

