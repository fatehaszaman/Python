# Time: O(n)
# Space: O(n)

""" The project "greet"
Context
This environment is a simple python project, containing a function greet. This function outputs "HELLO", followed by the name given in parameters.
To manually test it, open a terminal and run the command python src/main.py. The terminal will ask you to type a name, then will write the function result.
Goal
Modify the function greet, so that it returns the upcased name.
Test
Open a terminal and execute pytest to launch the tests. Initially, one test passes and one fails.
All the tests will succeed when the function greet is fixed. """

"""instructions 
The project "greet"

Context

This environment is a simple python project, containing a function greet. This function outputs "HELLO", followed by the name given in parameters.

To manually test it, open a terminal and run the command python src/main.py. The terminal will ask you to type a name, then will write the function result.

Goal

Modify the function greet, so that it returns the upcased name.

Test

Open a terminal and execute pytest to launch the tests. Initially, one test passes and one fails.

All the tests will succeed when the function greet is fixed."""

#Project 25 min 150 pts

def greet(name: str) -> str:
    return "HELLO " + name


if __name__ == "__main__":
    name = input("Enter a string: ")
    print(greet(name))


#ANSWER but you have to delete and save the tab
def greet(name: str) -> str:
    return "HELLO " + name.upper()


if __name__ == "__main__":
    name = input("Enter a string: ")
    print(greet(name))
