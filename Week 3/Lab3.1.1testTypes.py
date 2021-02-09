#
#   Types
#   
#   1. Create a file called testTypes.py, in the file create 5 variables one for each of
#      the following types:
#       • int
#       • float
#       • boolean
#       • str
#       • list (look at w3schools.com)
#
#   2. Use the type() function to check that the variables are of that type.
#

i = 3 # interger
fl = 3.5 # float
isa = True # boolean
memo = 'how now brown cow' # string
lots = [] # list

print ('variable {} is of type: {} and value: {}'.format('i', type(i), i))
print ('variable {} is of type: {} and value: {}'.format('fl', type(fl), fl))
print ('variable {} is of type: {} and value: {}'.format('isa', type(isa), isa))
print ('variable {} is of type: {} and value: {}'.format('memo', type(memo), memo))
print ('variable {} is of type: {} and value: {}'.format('lots', type(lots), lots))