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
                    "following format: 1000.00"
                )
            )
            print()


def length_of_travel():
    """
    This function gets the length of travel from the user
    and returns it as an integer
    """
    while True:
        print()
        length = input("What is the length of your travel in days? ")
        try:
            length = int(length)
            if length <= 0:
                print()
                print("Please enter a number greater than 0")
                print()
                continue
            return length
        except ValueError:
            print()
            print(
                (
                    "Invalid input - Please enter a valid number in the "
                    "following format: 10"
                )
            )
            print()


# def type_of_expense():
#     """
#     This function gets the type of expense from the user
#     and returns it as a string
#     """


# def expense_amount():
#     """
#     This function gets the expense amount from the user
#     and returns it as a float
#     """

# def select_category():
#     """
#     This function gets the category of expense from the user
#     """

# def any_more(): # do you want to add more expenses?
# # result
# # restart


def main():
    """
    Main function to run the programme
    """
    console.print(welcome, style="bold #15E6E4", justify="center")
    begin = get_content('intro.txt')
    console.print(begin, style="#9DE635", justify="center")
    budget = get_budget()
    duration = length_of_travel()
    console.print(
        f"Your travel budget is £{budget:,.2f}, you plan to travel for "
        f"{duration} days.",
        style="#9DE635",
        justify="center"
    )

    # type of expense?
    # expense amount?
    # select a category
    # do you want to add more expenses?
    # restart


main()
