#region imports
from copy import deepcopy
import math
#endregion

#region function definitions
def printlist(mylist):
    """
    Print the elements of mylist with each on a new line.
    :param mylist:
    :return: none
    """
    #print(mylist)
    for val in mylist:
        print(val)
    return

def pl2(alist):
    """
    Prints a blank line and then length of alist.
    Then, prints the elements of alist each on a new line.
    :param alist:
    :return: none
    """
    print("\n",len(alist)," length of alist \n")
    printlist(alist)

def printmat(mymat):
    """
    This function prints out the rows of a matrix where each element of each row is printed on a new line.
    :param mymat:
    :return: none
    """
    print("\n\nprinting mymat")
    for row in range(len(mymat)):
        print("row ", row)
        printlist(mymat[row])
        # for col in range(len(mymat[row])):
        #     print(mymat[row][col])

def arraysum(thelist):
    """
    This function sums the elements of a list.
    :param thelist:
    :return: the sum of the elements in thelist
    """
    sum=0
    for num in thelist:
        #sum=sum+num
        sum += num
    return sum

def matrixsum(thematrix):
    """
    This function sums all the values in a matrix.
    :param thematrix:
    :return: the sum of thematrix
    """
    sum=0
    for rowval in thematrix:
        sum += arraysum(rowval)
        # for colval in rowval:
        #     sum += colval
        #next colval
    #next rowvals
    return sum

def superbowl():
    """
    This was my prediction for the NFC and AFC championship games of 2021
    :return: none
    """
    NFC={'Packers':26, 'Bucs':31, 'Brady':'GOAT'}
    AFC={'Bills':24, 'Chiefs':38, 'Mahomes':'young enough to be Bradys son'}
    print('NFC Championship: Bucs {} to Packers {}. Brady is {}'.format(NFC['Bucs'],NFC['Packers'], NFC['Brady']))
    print('AFC Championship: Chiefs {} to Bills {}. Mahomes is {}'.format(AFC['Chiefs'], AFC['Bills'], AFC['Mahomes']))

def getLoopy():
    '''
    This is a function I'm using to teach the differnce between for and while loops.
    Generally, a for loop executes for a specified number of iterations whereas a while loop executes until a particular
    condition is met.
    :return:
    '''
    upperLim = 13
    # Example 1:  make a list of x values from 0 to 13 in increments of pi/17.  I'll first do this with a for loop.
    # Step 1: how many intervals?
    N = int(upperLim/(math.pi/17))  #  this will always round down to a whole number (called floor division)
    # Step 2: compute interval size
    h = math.pi/17
    # Step 2:  make a list of appropriate size
    list0 = [0]*(N+1)
    for i in range(N+1):
        list0[i] = i*h

    # Example 2:  repeat Example 1 with a while loop.
    # Step 1: initialize a list that is empty
    list1 = []
    # Step 2: create 'watch' variable to be incremented each time through the loop
    xVal = 0.0
    # Step 3: write the while loop
    while xVal < upperLim:
        list1.append(xVal)
        xVal += h  # incrementally increase xVal using increment operator

    # Example 3:  use a while loop to check the exit condition internally
    list2 = []
    xVal = 0.0
    while True:
        if xVal < upperLim:
            list2.append(xVal)
        else:
            break
        xVal += h

    # Example 4:  make a list like example 1, but in reverse order
    list3 = deepcopy(list0)
    list3.reverse()
    list4=[0]*(N+1)
    for i in range(len(list4)):
        list4[i]=(N-i)*h

    list5=[]
    xVal = N*h
    while xVal>=0:
        list5.append(xVal)
        xVal -= h

    # Example 5:  use a list comprehension
    list6 = [i*h for i in range(N+1)]
    list7 = deepcopy(list6)
    list7.reverse()
    list8=list6[::-1]  # slicing [start index: stop index: step]  If no start index then 0.  If no stop index then length of list-1. If no step, then 1.
    list9=list6[::]  # effectively creates a deep copy of list6 by copying value of elements.
    list9.reverse()
    pass

def exploreCopying():
    """
    This function explores shallow vs. deep copying of a list.
    :return: none
    """
    list1 = [1, 2, 3, 4, 5, 6, 7]  # make a simple list
    print(list1)

    list2 = list1  # this creates a 'shallow' copy of list1.
    list1[3] = 17
    print("list2 changes after change in list 1", list2)

    list2[2] = 28
    print("list1 changes after a change in list 2", list1)

    list3 = deepcopy(list1)  # this creats a 'deep' copy of list1
    list1[4] = 25
    print("list1 ", list1)
    print("list 3 deepcopy no change after change in list 1", list3)

    # creating new lists
    new1 = [0] * 5  # strange notation, but creates a list of 5 elements long with 0 in each element.
    print("\na new list of zeros", new1)
    new1[2] = 7
    print("change only 1 term ", new1)

    # creating new matrix ????
    nrows, ncols = 6, 4
    matrix1 = [[0] * ncols] * nrows
    matrix1[2][2] = 494  # node that each row is a shallow copy of the first row
    print("\n", matrix1)  # this doesn't work!!!

    # list comprehension (list math) for creating new lists
    nrows, ncols = 4, 7
    matrix2 = [[0] * ncols for i in range(nrows)]
    matrix2[2][2] = 73
    print(matrix2)

def main():
    """
    This program is for teaching lists in python.
    Notes:
    1.  A list in Python is like a vector on paper.  That is, it has elements that are referenced by an index value.  On paper
        we talk about row or column vectors, but in Python a list is just a 1-dimensional list and row or column is irrelevant.
    2.  The indicies of a list start at 0.  So if a list has 10 elements, the indicies are from 0 to 9.
    3.  We access the values stored in the list by index:  theList[3] refers to the fourth element in a list called theList
    4.  We can retrieve sub lists by slicing.  For example subList = theList[2:5] creates a list called subList that contains
        elements from theList starting at index 2 and ending at index 4.  subList will contain 3 elements.
    5.  We can also use negative indexing to retrieve an element from a list. For example if theList contains 10 elements,
        I can access the tenth element by theList[9] OR theList[-1].  I can access the 7th element by theList[6] OR theList[-4]
    6.  You can pass a list as an argument to a function and/or return a list from a function.
    7.  The type of information store in the elements of a list can be real or complex numbers, floating point or integer numbers,
        strings, booleans (true or false), other lists, objects.  Very few restrictions about what can be in an element of
        a list.  Most of the time, we store numbers in a list.
    8.  The number of elements in a list is found by:  len(theList).
    9.  We can iterate through the elements of a list in two common ways:
        a. for E in theList:  This extracts the elements in theList starting at index 0 and assigns the value to E.
        b. for i in range(len(theList)):  This uses a counting variable i that assumes the value from 0 to len(theList) - 1.

    Dictionary:
    1.  In python, a dictionary is a special kind of list where the elements are made of key:value pairs.
    2.  The elements of a dictionary can be accessed by index OR key.
    3.  See the function superbowl for an example.

    Tuple:
    1.  In python, a tuple behaves the same as a list except that once it is defined, neither the length of the tuple nor any
        of the elements may be changed.  That is, it is immutable.
    2.  A tuple assigned to a variable like tp1=(2,5,9) can be redefined by tp1=(3, 6, 9, 12), but I can't say tp1[1]=7.

    :return:
    """
    ralph=[1,3,5,2,4,9,3,5,-2,11.7]  # the list name ralph (scope: local to main)
    ralph_sub = ralph[3:5]  # this is known as list slicing.  It counts from index 3 to 4 (note: last index is 5-1)
    ralph_sub_1 = ralph[3:9:2]  # this slices from index 3 to 8, but with a step size of 2.
    gerald=[[1,2,3,4],[5,6,7],[5,6,7,8],[5,6,7,8],[4,3,2,1]]  # a matrix (list of lists) called gerald (scope:  local to main)
    #note row 1 only has 3 terms
    printlist(ralph)  # see function printlist
    pl2(ralph)
    print("\n",ralph)
    printmat(gerald)
    #a=arraysum(ralph)
    cc=matrixsum(gerald)

    print("matrixsum(gerald)={}".format(cc))

    superbowl()
    exploreCopying()
    getLoopy()

#endregion

# Note:  the starting point when I run or debug the program.
main()





