# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.
def measure_udacity(p):
     c=0
     for x in p:
         if x[0] == 'U':
             c += 1
     return c
    




print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2