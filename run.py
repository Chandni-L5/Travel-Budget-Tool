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
    with open(file, "r", encoding="utf-8") as f:
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
                console.print(f"\n{error}\n")
                continue
            return value

        except ValueError:
            console.print(f"\nInvalid input - {error}\n")


def initial_questions():
    """
    This function asks the user for their travel budget, duration,
    and spending money whilst using the get_input function.
    """
    budget = get_input(
        question="What is your travel budget? £",
        value_type=float,
        error="Please enter a number greater than 0",
        min_value=0,
    )
    duration = get_input(
        question="What is the length of your travel in days? ",
        value_type=int,
        error="Please enter a number greater than 0",
        min_value=0,
    )
    spending_money = get_input(
        question="How much spending money do you require per day? £",
        value_type=float,
        error="Please enter a number greater than 0",
        min_value=0,
    )
    return budget, duration, spending_money
    """
    Return all three values for global use
    """


def confirm_initial():
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

        console.print(
            "\nInvalid input. Please enter 'Y' for Yes or 'N' for No.\n",
            style="bold red"
            )


def subsequent_questions():
    """
    This function gets the type of expense from the user, cost
    and category of the expense
    """
    description = get_input(
        question=(
            "Enter a description of the expense "
            "e.g boat trip, booking.com, etc:"
        ),
        value_type=str,
        error="Please enter a valid type of expense",
    )
    cost = get_input(
            question="\nEnter the amount of the expense e.g 100.00: £\n",
            value_type=float,
            error="\nPlease enter a valid amount\n",
            min_value=0,
        )
    category = [
        "✈️ Flights/Transport",
        "🏨 Accommodation",
        "🚤 Excursions",
        "✨ Miscellaneous",
    ]
    while True:
        console.print("\nPlease select a category: \n")
        for i, category_option in enumerate(category):
            console.print(f"  {i + 1}. {category_option}")
        value_range = f"[1 - {len(category)}]"
        try:
            selected_index = int(input(
                f"\nEnter a category number {value_range}: \n"
            )) - 1
            if selected_index not in range(len(category)):
                raise ValueError
            break
        except ValueError:
            console.print(
                f"\nInvalid input. Please enter a number between "
                f"1 and {len(category)}.\n",
                style="bold red"
            )
    return description, cost, category[selected_index]


def main():
    """
    Main function to run the programme
    """
    console.print(welcome, style="bold #15E6E4", justify="center")
    begin = get_content("intro.txt")
    console.print(begin, style="#9DE635", justify="center")

    while True:
        budget, duration, initial_spending = initial_questions()
        console.print(
            f"\nYour travel budget is £{budget:,.2f}, you plan to travel for "
            f"{duration} days and ideally you would like to have £"
            f"{initial_spending:,.2f} to spend per day.",
            style="#9DE635",
            justify="center",
        )
        if confirm_initial():
            break

    console.print(
        "\nThe next set of questions will be about your expenses.",
        style="#9DE635",
        justify="center"
        )
    console.print(
        "You can enter multiple expenses if you wish.\n",
        style="#9DE635",
        justify="center"
        )

    expense_totals = {
        "✈️ Flights/Transport": 0,
        "🏨 Accommodation": 0,
        "🚤 Excursions": 0,
        "✨ Miscellaneous": 0,
    }
    total_expenses = 0

    while True:
        description, cost, category = subsequent_questions()

        expense_totals[category] += cost
        total_expenses += cost

        console.print(
            f"\nYou have added an expense of £{cost:,.2f} for {description} "
            f"under the category {category}.",
            style="bold #9DE635",
        )
        console.print("\nCurrent expense totals by category:")
        for cat, total in expense_totals.items():
            console.print(f"{cat}: £{total:,.2f}", style="bold green")

        while True:
            add_more = input(
                "\nDo you want to add another expense? (Y/N): "
                ).strip().lower()
            if add_more == "y":
                break
            elif add_more == "n":
                remaining_budget = budget - total_expenses
                console.print(
                        f"\nYour total expenses are £{total_expenses:,.2f}."
                        f"\nYou have £{remaining_budget:,.2f} left"
                        "to spend on your trip."
                        f"\nYou can spend £{
                            remaining_budget / duration:,.2f
                            } per day.",
                        style="bold #9DE635",
                        justify="center",
                )
                remaining_budget_per_day = remaining_budget / duration
                if remaining_budget_per_day > 0:
                    console.print(
                        "\nPack your bags and get ready for your trip! 🧳 ",
                        style="bold",
                    )
                else:
                    console.print(
                        "\nUnfortunately, your expenses "
                        "have exceeded your budget. ",
                        style="bold red",
                    )
                console.print(
                    "\nThank you for using the Travel Budget Planner!"
                    "\nWe hope to see you again soon!",
                    style="bold #9DE635", justify="center"
                )
                break
            else:
                console.print(
                    "\nInvalid input. Please enter 'Y'"
                    "for Yes or 'N' for No.\n", style="bold red"
                )
                

main()
