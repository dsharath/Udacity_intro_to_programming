# The range of a set of values is the maximum value minus the minimum
# value. Define a procedure, set_range, which returns the range of three input
# values.

# Hint: the procedure, biggest which you coded in this unit
# might help you with this question. You might also like to find a way to
# code it using some built-in functions.

def set_range(a,b,c):
    # Your code here
     if (a>b and a>c):
         if (b>c and b<a):
             return a-c
         else:
             return a-b
     elif (b>a and b>c):
         if (a>c and a<b):
             return b-c
         else:
             return b-a
     elif (c>a and c>b):
         if (a>b and a<c):
             return c-b
         else:
              return c-a
     elif (a==b and a>c):
         return a-c
     elif (b==c and b>a):
         return b-a
     elif (a==c and a>b):
         return a-b
     elif (a==b and b==c):
         return 0
         
     
print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6