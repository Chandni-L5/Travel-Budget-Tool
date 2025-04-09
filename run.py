from rich import print
from rich.padding import Padding
from rich.console import Console
from rich.table import Table
from rich import box
import time
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json
import os
from google.oauth2 import service_account


class Expense:
    def __init__(self, description, cost, category):
        """
        Creates an expense object as a class
        """
        self.description = description
        self.cost = cost
        self.category = category

    def __str__(self):
        """ Returns a string representation of the expense object"""
        return f"{self.description}: £{self.cost:,.2f} ({self.category})"

    def update_cost(self, new_cost):
        """ Updates the cost of the expense. """
        if new_cost > 0:
            self.cost = new_cost
        else:
            print("Invalid input. Please enter a valid number greater than 0.")

    def get_category(self):
        """Returns the category of the expense."""
        return self.category


SCOPE = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS_DICT = json.loads(os.environ['GOOGLE_CREDS'])
CREDS = service_account.Credentials.from_service_account_info(
    CREDS_DICT,
    scopes=SCOPE,
)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
DOCUMENT_ID = "1ev4aBGg3904TWkGkpIIZq0NqTvKKHihuFNdtoBOZ9Rk"
DOCS_SERVICE = build("docs", "v1", credentials=SCOPED_CREDS)
creds = service_account.Credentials.from_service_account_info(
    CREDS_DICT, scopes=SCOPE
)


console = Console()
"""
Enable use of rich library for console output
"""
error_console = Console(stderr=True, style="bold red")


welcome = Padding(
    (
        "[u]:airplane_departure: Welcome to your Travel Budget Planner "
        ":money_with_wings:[/u]"
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
    show_symbol=False
):
    """
    This function gets input from the user and
    throws an error if the input is not valid
    """
    while True:
        console.print(f"[color(166)]{question}[/color(166)]")
        currency = "£ " if show_symbol else ""
        user_input = console.input(f"> {currency} ").strip()
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
                error_console.print(f"\n{error}\n")
                continue
            return value
        except ValueError:
            error_console.print(f"\n Invalid input - {error}")


def initial_questions():
    """
    This function asks the user for their travel budget, duration,
    and spending money whilst using the get_input function.
    """
    budget = get_input(
        question="What is your travel budget?",
        value_type=float,
        error="Please enter a [underline]number[/underline] greater than 0",
        min_value=0,
        show_symbol=True,
    )
    duration = get_input(
        question="What is the length of your travel in days? ",
        value_type=int,
        error="Please enter a [underline]number[/underline] greater than 0",
        min_value=0,
        show_symbol=False,
    )
    spending_money = get_input(
        question="How much spending money do you require per day?",
        value_type=float,
        error="Please enter a [underline]number[/underline] greater than 0",
        min_value=0,
        show_symbol=True,
    )
    return budget, duration, spending_money


def display_initial():
    """
    This function displays the initial travel details
    and asks the user to confirm them.
    a Rich display status bar is used to identify
    when a process is running to display a custom
    statement
    """
    console.print(
        "\nThe first set of questions will assist the app in understanding "
        "your criteria and requirements for this trip.\n"
        "\nLet's begin!\n",
        style="color(10)"
    )
    while True:
        budget, duration, spending_money = initial_questions()
        console.print("")
        loading_widget()
        display_initial_text = (
            f"\nYour travel budget is £{budget:,.2f}, you plan to travel for "
            f"{duration} days and ideally you would like to have £"
            f"{spending_money:,.2f} to spend per day."
        )
        console.print(display_initial_text, style="color(226) bold")

        if confirm():
            google_doc(display_initial_text)
            return budget, duration, spending_money
        else:
            console.print("\nLet's try again.")


def confirm():
    """
    This function asks the user to confirm if their travel details are correct.
    Returns True if they confirm (Y), False if they want to restart (N).
    """
    while True:
        confirmation = console.input(
            "\n\n[color(166)]Are these details correct?[/color(166)] "
            "[bold color(50)](Y/N):[/bold color(50)] "
        ).strip().lower()

        if confirmation in ["y", "n"]:
            return confirmation == "y"  # True for "Y", False for "N"

        error_console.print(
            "\n Invalid input. Please enter 'Y' for Yes or 'N' for No.",
            style="bold red"
            )


def subsequent_questions():
    """
    This function gets the type of expense from the user, cost
    and category of the expense.
    It also asks for confirmation before proceeding.
    """
    while True:
        description = get_input(
            question=(
                "\nEnter a description of the expense "
                "e.g boat trip, booking.com, etc: "
            ),
            value_type=str,
            error="Invalid input - Please enter a valid type of expense",
            show_symbol=False,
        )
        cost = get_input(
            question="\nEnter the amount of the expense e.g 100.00:",
            value_type=float,
            error="Please enter a valid amount\n",
            min_value=0,
            show_symbol=True,
        )
        category = [
            "Flights/Transport",
            "Accommodation",
            "Excursions",
            "Miscellaneous"
        ]
        styled_category = [
            "[color(57)]✈️ Flights/Transport[/color(57)]",
            "[color(57)]🏨 Accommodation[/color(57)]",
            "[color(57)]🚤 Excursions[/color(57)]",
            "[color(57)]✨ Miscellaneous[/color(57)]",
        ]
        while True:
            console.print(
                "\n[color(50)]Please select a category: [/color(50)]\n"
            )
            for i, category_option in enumerate(styled_category):
                console.print(f"  {i + 1}. {category_option}")
            value_range = f"[1 - {len(category)}]"
            try:
                selected_index = int(console.input(
                    f"\n[color(50)]Enter a category number {value_range}: "
                    f"[/color(50)]"
                )) - 1
                if selected_index not in range(len(category)):
                    raise ValueError
                break
            except ValueError:
                error_console.print(
                    f"\nInvalid input. Please enter a number between "
                    f"1 and {len(category)}.\n",
                    style="bold red"
                )
        expense = Expense(description, cost, category[selected_index])
        if confirm():
            return expense
        else:
            console.print(
                "\nLet's try entering that expense again.", style="color(166)"
            )


def track_expenses(budget, duration):
    """
    This function tracks the expenses
    """
    expense_totals = {
        "Flights/Transport": 0,
        "Accommodation": 0,
        "Excursions": 0,
        "Miscellaneous": 0,
    }
    total_expenses = 0
    while True:
        expense = subsequent_questions()
        expense_totals[expense.get_category()] += expense.cost
        total_expenses += expense.cost

        display_added_expense(expense, expense_totals)
        if not add_more_expenses():
            break
    google_doc_expense_summary(expense_totals)
    final_summary(budget, duration, total_expenses)


def display_added_expense(expense, expense_totals):
    """
    This function displays a summary of the expense added
    and also updates the running total per
    category
    """
    expense_summary = (
        f"\nYou have added an expense of £{expense.cost:,.2f} for "
        f"{expense.description} under the category {expense.category}."
    )
    console.rule("")
    console.print("")
    loading_widget()
    console.print(expense_summary, style="color(226) bold")
    table = Table(
        title="\n[color(51)]Expense Summary[/color(51)]",
        box=box.ASCII_DOUBLE_HEAD
    )
    table.add_column("Category", justify="left")
    table.add_column("Running Total", justify="right")
    for cat, total in expense_totals.items():
        table.add_row(f"{cat}", f"£{total:,.2f}", style="color(226)")
    console.print(table)
    google_doc(expense_summary)


def loading_widget():
    """
    This function displays a loading widget
    """
    with console.status(
        "\n[bold green]Loading...",
        spinner="aesthetic",
        speed=1.0,
    ):
        time.sleep(2)


def add_more_expenses():
    """
    This function asks the user if they want to add more expenses
    """
    while True:
        add_more = console.input(
            "\n[color(166)]Do you want to add another expense?[/color(166)\n]"
            "[bold color(50)] (Y/N):[/bold color(50)] "
        ).strip().lower()
        if add_more == "y":
            return True
        elif add_more == "n":
            return False
        else:
            error_console.print(
                "\nInvalid input. Please enter 'Y'"
                "for Yes or 'N' for No.\n", style="bold red"
            )


def final_summary(budget, duration, total_expenses):
    """
    This function displays the final summary of the expenses and then appends
    the summary to Google Docs.
    """
    console.print("")
    loading_widget()
    remaining_budget = budget - total_expenses
    summary_text = (
        f"\nYour total expenses are £{total_expenses:,.2f}.\n"
        f"\nYou have £{remaining_budget:,.2f} left to "
        f"spend on your trip.\n"
        f"\nYou can spend £{remaining_budget / duration:,.2f}"
        f" per day.\n"
    )
    console.rule("")
    console.print(
        summary_text,
        style="color(226)",
    )
    exit_message(remaining_budget, duration)
    console.print(
        "\nA summary of your results has been added to Google Doc "
        "successfully - Copy and paste this link into your browser to view "
        "your summary - https://tinyurl.com/2e77c76c \n"
        "\nPlease consider copy and pasting the summary into a "
        "separate document for your records.\n",
        style="color(51)",
    )
    console.print("")
    google_doc(summary_text)
    while True:
        exit_choice = console.input(
            "\n[color(166)]Have you finished viewing the Google Doc?"
            "[/color(166)]\n"
            "\n[bold color(50)] (Y/N):[/bold color(50)] "
        ).strip().lower()
        if exit_choice == "y":
            clear_google_doc()
            break
        else:
            error_console.print(
                "\nProgram will not exit until you have finished viewing the "
                "Google Doc.",
                style="bold red"
            )
    console.print("")
    console.print(
        "\nThank you for using the Travel Budget Planner!"
        "\nWe hope to see you again soon!\n",
        style="bold color(69)",
        justify="center",
    )


def exit_message(remaining_budget, duration):
    """
    This function displays the final message and conclusion
    of the programme.
    """
    remaining_budget_per_day = remaining_budget / duration
    if remaining_budget_per_day > 0:
        console.print(
            "\nPack your bags and get ready for your trip! 🧳 ",
            style="bold color(226)",
        )
    else:
        console.print(
            "\nUnfortunately, your expenses "
            "have exceeded your budget. ",
            style="bold red",
        )


def google_doc(text):
    """
    This function prints the summary to the google doc
    """
    document = DOCS_SERVICE.documents().get(
        documentId=DOCUMENT_ID
    ).execute()
    document_length = document.get(
        "body", {}
        ).get("content", [])[-1]["endIndex"]
    try:
        requests = [
            {
                "insertText": {
                    "location": {
                        "index": document_length - 1
                        },
                    "text": text + "\n",
                }
            }
        ]
        DOCS_SERVICE.documents().batchUpdate(
            documentId=DOCUMENT_ID,
            body={"requests": requests}
        ).execute()
    except HttpError as error:
        print(f"An error occurred: {error}")


def google_doc_expense_summary(expense_totals):
    """
    prints readable text table to Google Docs
    """
    header = "Expense Summary\n\n"
    col1 = "Category"
    col2 = "Running Total"
    line_length = 50

    table = f"{col1.ljust(25)} | {col2.rjust(15)}\n"
    table += "-" * line_length + "\n"

    for cat, total in expense_totals.items():
        amount = f"£{total:,.2f}"
        table += f"{cat.ljust(25)} | {amount.rjust(15)}\n"

    table += "-" * line_length + "\n"
    full_text = "\n" + header + table + "\n"
    google_doc(full_text)


def google_doc_final_summary(total_spent, remaining_budget, updated_daily):
    summary = (
        f"\nYour total expenses are £{total_spent:,.2f}.\n\n"
        f"You have £{remaining_budget:,.2f} left to spend on your trip.\n\n"
        f"You can spend £{updated_daily:,.2f} per day.\n"
    )
    google_doc(summary)


def clear_google_doc():
    """
    This function clears the Google Doc
    """
    try:
        document = DOCS_SERVICE.documents().get(
            documentId=DOCUMENT_ID
        ).execute()
        document_length = document.get(
            "body", {}
            ).get("content", [])[-1]["endIndex"]
        requests = [
            {
                "deleteContentRange": {
                    "range": {
                        "startIndex": 1,
                        "endIndex": document_length - 1
                    }
                }
            }
        ]
        DOCS_SERVICE.documents().batchUpdate(
            documentId=DOCUMENT_ID,
            body={"requests": requests}
        ).execute()
    except HttpError as error:
        print(f"An error occurred whilst clearing the document {error}")


def main():
    """
    Main function to run the programme
    """
    console.print(welcome, style="bold #15E6E4", justify="center")
    begin = get_content("intro.txt")
    console.print(begin, style="color(195)")
    console.rule("")
    budget, duration, spending_money = display_initial()
    console.rule("")
    console.print(
        (
            "\nThe next set of questions will be about your expenses such as "
            "hotels, flights or activities such as boat trips or a tour of a "
            "vineyard."
        ),
        style="color(10)",
        )
    console.print(
        "You can enter multiple expenses if you wish.\n",
        style="color(10)",
        )
    track_expenses(budget, duration)


main()
