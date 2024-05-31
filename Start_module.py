# This instruction shows that we are trying to import 'take_input()' function present in 'Input_module'.
from Input_module import take_input
# This instruction shows that we are trying to import 'process()' function present in 'Process_module'.
from Process_module import process
# This instruction shows that we are trying to import 'output()' function present in 'Output_module'.
from Output_module import output
# This instruction shows that we are trying to import 'greet()' function present in 'Welcome_module'.
from Welcome_module import greet
# This built in module has a function with which we can clear the terminal every time when it runs.
import os

os.system("cls")

# Welcome message:
greet()
# This loop remains always 'True' for asking question.
while True:
    # Creating a variable 'i' that stores input of 'take_input()' function.
    i = take_input()
    # Here we are passing user input to the process module's function;'process()' as an argument.
    o = process(i)
    output(o)
