# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.
i=[1,2,3]
j=[4,5,6]
def union(a,b):
    for i in b:
        if i not in a:
            return a.append(i)
            
print j




# To test, uncomment all lines 
# below except those beginning with >>>.

#a = [1,2,3]
#b = [2,4,6]
#union(a,b)
#print a 
#>>> [1,2,3,4,6]
#print b
#>>> [2,4,6]
