from rich import print
from rich.padding import Padding
from rich.console import Console


console = Console()
"""
Enable use of rich library for console output
"""


welcome = Padding(
    (
        ":airplane_departure: Welcome to your Travel Budget Planner "
        ":money_with_wings:"
    ),
    1
)


def get_content(file):
    """
    Reads the content of a file and returns it as a string
    """
    intro = open(file, 'r')
    content = intro.read()
    intro.close()
    return content


def get_budget():
    """
    This function gets the travel budget from the user
    and returns it as a float
    """
    while True:
        print()
        budget = input("What is your travel budget? £")
        print()
        try:
            budget = float(budget)
            if budget <= 0:
                print()
                print("Please enter a number greater than 0")
                print()
                continue
            return budget
        except ValueError:
            print()
            print(
                (
                    "Invalid input - Please enter a valid number in the "
                    "following format: 1000.00 /n"
                )
            )
            print()
# length of travel?
# type of expense?
# expense amount?
# select a category
# do you want to add more expenses?
# result
# restart


def main():
    """
    Main function to run the programme
    """
    console.print(welcome, style="bold #15E6E4", justify="center")
    begin = get_content('intro.txt')
    console.print(begin, style="#9DE635", justify="center")
    budget = get_budget()
    console.print(f"Your travel budget is £{budget:,.2f}.")
    # what is your travel budget?
    # length of travel?
    # type of expense?
    # expense amount?
    # select a category
    # do you want to add more expenses?
    # restart


main()
