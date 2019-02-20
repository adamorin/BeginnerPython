# -*- coding: utf-8 -*-
"""
Python For Beginners Exercises
"""

# STRINGS

for j in range(1,5):
    print(j)
    
    
x = 1
print("My number as a string is " + str(x))    
    
#1    
a = "cat"
v = "lettuce" 
m = "quartz"

print("Here is an animal, vegetable, mineral:")
print(a,v,m)
print(a + "--" + v + "--" + m)
for j in range (1,5):
    print(j*(a + v + m))
    
print('a: {0} \nv:{1} \nm:{2} \n'.format(a, v, m))    
    
#2
msg = "pork" #input('Type something sucka:')
print(msg)

#3
pad = 10
print(" "*pad + " " + "-"*(len(msg)+2))
print(" "*pad + "< {0} >".format(msg) )
print(" "*pad + " " + "-"*(len(msg)+2))
cat = '''        /
 /\_/\ /
( o.o )
 > ^ <

'''
print(cat)


# NUMBERS
rate = 0.51
print("Day cost: " + str(rate*24) )
print("Month cost: " + str(rate*24*30))

# CONDITIONALS
dist = 299 #float(input("Distance:"))
if dist <= 3:
    print("Walk")
elif dist < 300:
    print("drive")
else:
    print("fly")
    
    
#Functions
def MakeStory(noun: str, verb: str, adj: str):
    """Prints a funny story using inputs"""
    story = """Once upon a time there was a {0}, and it was {2}. Well one day the big bad wolf came to {1} all over the {0}, and {0} was so sad. But whatever.""".format(noun, verb, adj)
    print(story)
    
MakeStory("cow", "poop", "sexy")    
    

#Lists
def MakeShoppingList():
    item = input("First item:")
    shoppingList = [item]
    while item != "":
        item = input("Next item: ")
        shoppingList.append(item)
    for item in shoppingList:
        print(item)
#MakeShoppingList()
        