#!/usr/bin/python3

"""
Write a function that divides element by element 2 lists.

Prototype: def list_division(my_list_1, my_list_2, list_length):
my_list_1 and my_list_2 can contain any type (integer, string, etc.)
list_length can be bigger than the length of both lists
Returns a new list (length = list_length) with all divisions
If 2 elements can’t be divided, the division result should be equal to 0
If an element is not an integer or float:
print: wrong type
If the division can’t be done (/0):
print: division by 0
If my_list_1 or my_list_2 is too short
print: out of range
You have to use try: / except: / finally:
You are not allowed to import any module
"""

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            try:
                new_list.append(my_list_1[i] / my_list_2[i])
            except ValueError:
                new_list.append(0)
                print("wrong type")
            except TypeError:
                new_list.append(0)
                print("wrong type")
            except ZeroDivisionError:
                new_list.append(0)
                print("division by 0")
            except IndexError:
                new_list.append(0)
                print("out of range")
    except ValueError:
        print("wrong type")
    except TypeError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("out of range")
    finally:
        return new_list
