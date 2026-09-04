#This is a multi-line string (also called a docstring when used as documentation).
#It doesn't affect the program execution.
"""
Bank Account System using Python OOP Concepts
Demonstrates: Classes, Objects, Inheritance, Encapsulation, and Polymorphism
"""
#This imports the datetime class from Python's built-in datetime module.
from datetime import datetime


#List from the typing module is used for type hints—it tells readers, IDEs,
# and type-checking tools what kind of data a variable, parameter, or return value should contain.
#This means:transactions should be a list containing strings.
from typing import List

# Parent Class (Base Class)
class BankAccount:
    '''Base class for all bank accounts'''

    # Class variable (shared across all instances)
    #A class variable belongs to the class itself, not individual objects.
    total_accounts = 0




