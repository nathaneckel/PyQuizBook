from xml.dom.expatbuilder import parseString
## Think SLICING for many of these.
def create_list_from_tuple(t):
    return list(t)  #    This function takes a tuple of elements and returns a list containing those elements of the tuple.

def drop_last(lst):
    return lst[:-1]  #   This function takes a list and returns a list with the last item removed.

def drop_first_two(lst):
    return lst[2:]  # This function takes a list and returns a list with the first two items removed.

def drop_mangle(lst):
    return lst[2:-1]    #    This function takes a list and returns a list with the first two items AND last item removed.

def add_item_front(lst, a):
    return [a] + lst    #    This function takes a list and an item, returning the list with the item prepended to the list

def add_item_end(lst, a):
    return lst + [a]    #    This function takes a list and an item, returning the list with the item appended to the list

def add_list_to_list(lsta, lstb):
    return lsta + lstb    #  This function takes two lists and appends one to the other, returning a list

def list_and_list_to_tuple(lsta, lstb):
    return (lsta, lstb)   #This function takes two lists and returns a tuple containing the two lists

def list_and_list_to_list(lsta, lstb):
    return [lsta, lstb]      #  This function takes two lists and returns a list containing the two lists

def list_from_range(n):
    return list(range(n+1))  #  This function returns list with 0..n as integers in a list
#FAILED 4 OF 4



def list_from_range2(n, m):   # This function returns list with n..m (without m) as integers in a list
   return list(range(n, m))

def list_from_range3(n, m):
    return list(range(n, m+1))    #   This function returns list with n..m (including m(!)) as integers in a list

def list_from_range4(n, m):
    return list(range(n+1, m+1))    #  This function returns list with n..m (WITHOUT n and including m) as integers in a list

def list_from_range_by(n, step):
    return list(range(0, n+1, step))    #    This function returns list with 0..n as integers by step in a list
#FAIL 3 PASS 1



def rev_list(lst):  # This function returns list which is a reverse of the argument list
    return lst[::-1]

def concat_list_indexwise(lst1, lst2):
    return [a + b for a, b in zip(lst1, lst2)]

# Write a program to add two lists index-wise.
# Create a new list that contains the 0th index item from both the list, then the 1st index item, etc till last element.
# Any leftover items will get added at the end of the new list.

def square_each_item(lst):
    return [x**2 for x in lst]   # This function returns list which each item in argument list has been squared

def remove_empty_strs(lst):
    return [s for s in lst if s != '']  # Remove empty strings from the list of strings

def remove_item_from(lst, aaa):
    return [x for x in lst if x != aaa]  #  Remove all occurrences of a specific item from a list.

def leave_item_in(lst, aaa):
    return [x for x in lst if x == aaa] #   Leave all occurrences of a specific item in a list.

def length_of(lst):
    return len(lst) #  return the length of the list