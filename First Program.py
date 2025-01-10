#region imports
# this imports the math module that contains many functions like sine and cosine, etc.
# importing a module gives you access to the functions of that module, but does nothing else
# see https://docs.python.org/3/library/math.html#module-math for detailed help
import math
#endregion

#region main program
a = 5  # create a variable called 'a' and assign it the integer value 5
print(a)  # print the value stored in the variable 'a', NOT the variable name 'a'
b = 7.3  # create a variable called 'b' and assign it the floating point value 7.3
c = a + b  # create a variable called 'c' and assign it the algebraic sum of 'a + b'
d = c + 2 * a  # create a variable called 'd' and assign it the value of 'c + 2 * a'
mommy = c / d  # create a variable called 'mommy' and assign it the value of 'c / d'
# I am using a breakpoint on the next line to pause the program and check value of variables
a = 12.0  # 'a' has already been created.  Here we reassign its value to be '12.0'
print(f'the value of a is: {a:.4f}')  # build a string using formatting and print it to cli
print(f'mommy = {mommy:0.3f}')
print('tan({:0.2f}) = {:0.3f}'.format(d, math.tan(d)))
print('pi = {diam_over_circ:0.6f}, e = {euler_number:0.5f}'.format(euler_number=math.e, diam_over_circ=math.pi))
print('e = %0.4f' % math.e)  # this is the old way of formatting a string
# This next line does three things:
#   1. use the compare operator '==' to give a true or false answer if e is equal to pi (clearly it is not)
#   2. 'cast' the answer to the form of a string
#   3. 'concatenate' the string and print it to the cli
print('e = pi is ' + str(math.e == math.pi))
# In the next line, 5! means 5 factorial, '5! !=' means 5 factorial is not equal to...
print('5! = %d, 5! != %0.3f  ' % (math.factorial(5), math.factorial(5)))
#endregion