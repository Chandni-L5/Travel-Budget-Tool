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
    1,
)


def get_content(file):
    """
    Reads the content of a file and returns it as a string
    """
    with open(file, "r") as f:
        return f.read()


def get_input(
    question,
    value_type,
    min_value=None,
    error="Please enter a valid number greater than 0",
):
    """
    This function gets input from the user and
    throws an error if the input is not valid
    """
    while True:
        print()
        user_input = input(question).strip()

        try:
            value = value_type(user_input)

            if (
                (value_type == str and user_input.isdigit())
                or (
                    isinstance(value, (int, float))
                    and not user_input.replace('.', '', 1).isdigit()
                )
                or (isinstance(value, (int, float)) and value <= min_value)
            ):
                print(f"\n{error}\n")
                continue
            return value

        except ValueError:
            print(f"\nInvalid input - {error}\n")


def get_budget():
    """
    This function gets the travel budget from the user
    and returns it as a float
    """
    return get_input(
        question="What is your travel budget? £",
        value_type=float,
        error="Please enter a number greater than 0",
        min_value=0,
    )


def length_of_travel():
    """
    This function gets the length of travel from the user
    and returns it as an integer
    """
    return get_input(
        question="What is the length of your travel in days? ",
        value_type=int,
        error="Please enter a number greater than 0",
        min_value=0,
    )


def spending_money():
    """
    This function gets the spending money from the user
    and returns it as a float
    """
    return get_input(
        question="How much spending money do you require per day? £",
        value_type=float,
        error="Please enter a number greater than 0",
        min_value=0,
    )


def confirm_details():
    """
    This function asks the user to confirm if their travel details are correct.
    Returns True if they confirm (Y), False if they want to restart (N).
    """
    while True:
        confirmation = input(
            "\nAre these details correct? (Y/N): "
        ).strip().lower()

        if confirmation in ["y", "n"]:
            return confirmation == "y"  # True for "Y", False for "N"

        print("\nInvalid input. Please enter 'Y' for Yes or 'N' for No.")


def expense_type():
    """
    This function gets the type of expense from the user
    and returns it as a string, the expense amount as a float and
    the category of the expense
    """
    console.print("The next set of questions will be about your expenses.")
    console.print("You can enter multiple expenses if you wish.")
    return get_input(
        question=(
            "Enter a description of the expense "
            "e.g boat trip, booking.com, etc:"
        ),
        value_type=str,
        error="Please enter a valid type of expense",
    )


def amount():
    """
    This function gets the amount of the expense from the user and returns
    as a float
    """
    return get_input(
            question="\nEnter the amount of the expense e.g 100.00: £",
            value_type=float,
            error="Please enter a valid amount",
            min_value=0,
        )


def expense_category():
    category = [
        "✈️ Flights/Transport",
        "🏨 Accommodation",
        "🚤 Excursions",
        "✨ Miscellaneous",
    ]
    while True:
        print("Please select a category: ")
        for i, category_option in enumerate(category):
            print(f"  {i + 1}. {category_option}")

        value_range = f"[1 - {len(category)}]"
        try:
            selected_index = int(input(f"Enter a category number {value_range}: ")) - 1
            if selected_index not in range(len(category)):
                raise ValueError  # Handle out-of-range numbers
            break  # Exit the loop if the selection is valid
        except ValueError:
            print(f"Invalid input. Please enter a number between 1 and {len(category)}.")

    return category[selected_index]  # Return the selected category


def main():
    """
    Main function to run the programme
    """
    console.print(welcome, style="bold #15E6E4", justify="center")
    begin = get_content("intro.txt")
    console.print(begin, style="#9DE635", justify="center")

    while True:
        budget = get_budget()
        duration = length_of_travel()
        initial_spending = spending_money()

        console.print(
            f"Your travel budget is £{budget:,.2f}, you plan to travel for "
            f"{duration} days and ideally you would like to have £"
            f"{initial_spending:,.2f} to spend per day.",
            style="#9DE635",
            justify="center",
        )

        if confirm_details():
            break

    expense_type()
    amount()
    expense_category()
    # type of expense?
    # expense amount?
    # select a category
    # do you want to add more expenses?
    # restart


main()
