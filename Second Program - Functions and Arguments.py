# region function definitions

# Notes:
#  1. The 'signature' for defining a function is:  def Function_Name(arguments):
#  2. The body of the function is defined by tab/spacing level.
#  3. A function MUST have a body.  If it does nothing, just write 'pass'.
#  4. The function may or may not return a value or values.
#  5. The functions can be defined in any order.
#  6. Nothing in a function is executed until it is used/called.
#  7. Arguments come in two flavors:  positional and keyword
#       positional arguments have no default value
#       keyword arguments have a default value
#  8. Arguments (positional or keyword) can be of type:
#     simple - e.g., float, int, string, boolean
#     multivalued - e.g., list, tuple, object
#     a function - technically called a 'callback function'
#  9. Special notation for arguments are *args and **kwargs where an
#     un-specified number of arguments or keyword arguments can be passed.
#     In either case, the arguments and keyword arguments are accessed as a tuple.
# 10. It is good practice to name your functions sensibly so that the name reflects
#     what the function does.
# 11. Variables defined in a function or as an argument have a scope that is
#     local to the function.  If you create or modify a variable in a called
#     function, that variable or value is invisible to the calling function.  If
#     you need to get a value from a function, you should use the return to do this.
# 12. It is good practice to use a docstring for every function so that the user gets
#     a clear picture of what the function does and what the arguments mean.
# 13. It is good practice to make the functions as simple as possible and usually a
#     function should just perform one task.
def trapezoidal(fcn, a, b, args=None, nPoints=100):
    """
    This function calculates the area under a function between limits of a and b using the trapezoidal method.
    :param fcn: A callback for the function to be integrated
    :param a: The lower limit of the integration
    :param b: The upper limit of the integration
    :param args: optional arguments as a tuple
    :param nPoints: number of points for the integration
    :return: area under fcn between a and b
    """
    # Step 1: compute the step size along the x axis
    # Step 2: evaluate the function at the ends of the range ( a & b )
    # Step 3: loop through the interior points and sum the areas of the trapezoidal panels
    # Step 4: return the area beneath the function


    # Step 1:  compute the step size along the x axis
    stepsize = (b-a)/(nPoints - 1)

    # Step 2: evaluate the function at the ends of the range ( a & b )
    if args is None:  fa = fcn(a)
    else: fa = fcn(a,args)
    sum = fa

    if args is None: fb = fcn(b)
    else:fb = fcn(b, args)
    sum += fb

    # Step 3: loop through the interior points and sum the areas of the trapezoidal panels
    for i in range(1, nPoints - 1):
       xi = a + i * stepsize

       if args is None: fxi = fcn(xi)
       else: fxi = fcn(xi, args)

       sum += 2*fxi  # Note the += operator (know as the increment operator)

    # Step 4: return the area beneath the function as a floating point number
    return sum*stepsize/2

def f1(x,args):
    """
    This function takes a tuple of arguments called args, unpacks into a, b, c and calculates f(x)
    :param x: x value for evaluating f(x)
    :param args: a tuple containing scalars a, b, c
    :return: value of f(x)
    """
    # Step 1:  unpack the arguments contained in the tuple args
    a,b,c = args
    # Step 2:  compute and return the function value
    return a*x**2 + b*x + c

def f3(x):
    """
    A less versitle function with 'hard coded' coefficients for a, b, c
    :param x: x value for evaluating f(x)
    :return: value of f(x)
    """
    # Step 1:  compute and return the function value
    return 5*x**2 + 2*x + 4

def test_trapezoidal():
    """
    Actually executes the trapezoidal integration method for a function.
    Recall, the trapezoidal method divides the x range into uniform steps of width h, calculates the summed area of
    a series of the trapezoids between a left and right limit.
    :return: the area under the curve as the summed areas of the trapezoids.
    """
    def f2(x):
        """
        This is a locally defined function to be passed as a callback function to the trapezoidal function.
        :param x:
        :return: f(x):  that is the y value of the function at x
        """
        return a*x**2 + b*x + c

    # Step 1: define some constants (a lesson in scope)
    a = 1
    b = 2
    c = 3
    # Step 2: use the internally defined f2 as the callback for the trapezoidal function.
    valf2_a = trapezoidal(f2, 0, 4, nPoints=20)
    print(f"f2a = {valf2_a:0.3f}")

    # Step 3: use trapezoidal function to compute area beneath f2 with better estimate.
    valf2_b = trapezoidal(f2, 0, 4, nPoints=200)

    # Step 4: print the result to the cli
    print(f"f2b = {valf2_b:0.3f}")

    # Step 5: use an externally defined function as the callback for the trapezoidal function.
    valf3_a = trapezoidal(f3, 0, 4, nPoints=20)
    print(f"f3 = {valf3_a:0.3f}")

    # Step 6:  now integrate f1.  a, b, c are in different scope than f1, so pass as args
    valf1_a = trapezoidal(f1, 0, 4, args = (a,b,c), nPoints=20)
    print(f"f1 = {valf1_a:0.3f}")

    # Step 7:  This defines a lambda function for the callback function of trapezoidal.  Use debugger to follow flow.
    vallambda = trapezoidal(lambda x: a*x**2 + b*x + c, 0, 4)
    print(f"vallambda = {vallambda:0.3f}")
    # Step 8:  return the value of vallambda
    return vallambda

def main():
    """
    This function tests the trapezoidal method for integrating a function.  See numerical methods tutorial for details.
    :return:
    """
    myval = test_trapezoidal()
    print(myval)
# endregion

main()

