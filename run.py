from rich import print
from rich.padding import Padding
from rich.console import Console
from rich.table import Table
from rich import box
import time
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPE = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json", scopes=SCOPE)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
DOCUMENT_ID = "1ev4aBGg3904TWkGkpIIZq0NqTvKKHihuFNdtoBOZ9Rk"
DOCS_SERVICE = build("docs", "v1", credentials=SCOPED_CREDS)


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
):
    """
    This function gets input from the user and
    throws an error if the input is not valid
    """
    while True:
        console.print(f"[color(166)]{question}[/color(166)]")
        user_input = console.input("> ").strip()

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
            error_console.print(f"\nInvalid input - {error}")


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


def display_initial():
    """
    This function displays the initial travel details
    and asks the user to confirm them.
    a Rich display status bar is used to identify
    when a process is running to display a custom
    statement
    """
    while True:
        budget, duration, spending_money = initial_questions()
        console.print("")
        with console.status(
            "\n[bold green]Calculating...",
            spinner="aesthetic",
            speed=1.0,
        ):
            time.sleep(2)
        console.print(
            f"\nYour travel budget is £{budget:,.2f}, you plan to travel for "
            f"{duration} days and ideally you would like to have £"
            f"{spending_money:,.2f} to spend per day.",
            style="color(226) bold",
        )

        if confirm_initial():
            return budget, duration, spending_money


def confirm_initial():
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
            "\nInvalid input. Please enter 'Y' for Yes or 'N' for No.",
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
            "e.g boat trip, booking.com, etc: "
        ),
        value_type=str,
        error="Please enter a valid type of expense",
    )
    cost = get_input(
            question="\nEnter the amount of the expense e.g 100.00: £",
            value_type=float,
            error="\nPlease enter a valid amount\n",
            min_value=0,
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
    return description, cost, category[selected_index]


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
        description, cost, category = subsequent_questions()

        expense_totals[category] += cost
        total_expenses += cost

        display_added_expense(description, cost, category, expense_totals)
        if not add_more_expenses():
            break
    final_summary(budget, duration, total_expenses)


def display_added_expense(description, cost, category, expense_totals):
    """
    This function displays a summary of the expense added
    and also updates the running total per
    category
    """
    expense_summary = (
        f"\nYou have added an expense of £{cost:,.2f} for {description} "
        f"under the category {category}."
    )
    console.rule("")
    console.print("")
    with console.status(
        "\n[bold green]Calculating...",
        spinner="aesthetic",
        speed=1.0,
    ):
        time.sleep(2)
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
    google_doc_table(expense_totals)


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
    with console.status(
        "\n[bold green]Calculating...",
        spinner="aesthetic",
        speed=1.0,
    ):
        time.sleep(2)
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
    console.print(
        "\nA summary of your results has been added to Google Doc "
        "successfully - You can view it here: "
        "[link=https://docs.google.com/document/d/"
        f"{DOCUMENT_ID}/edit]Google Doc[/link]",
        style="color(51)",)
    console.print("")
    google_doc(summary_text)
    exit_message(remaining_budget, duration)


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
    console.print("")
    console.print(
        "\nThank you for using the Travel Budget Planner!"
        "\nWe hope to see you again soon!\n",
        style="bold color(69)",
        justify="center",
    )


def google_doc(text):
    """
    This function prints the summary to the google doc
    """
    document = DOCS_SERVICE.documents().get(documentId=DOCUMENT_ID).execute()
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


def google_doc_table(expense_totals):
    """
    This function prints the table summary to the google doc
    """
    table_text = '\nExpense Summary\n'
    for category, total in expense_totals.items():
        table_text += f"{category}: £{total:,.2f}\n"
    google_doc(table_text)


def main():
    """
    Main function to run the programme
    """
    console.print(welcome, style="bold #15E6E4", justify="center")
    begin = get_content("intro.txt")
    console.print(begin, style="color(10)")
    console.rule("")
    budget, duration, spending_money = display_initial()
    console.rule("")
    console.print(
        "\nThe next set of questions will be about your expenses.",
        style="color(10)",
        )
    console.print(
        "You can enter multiple expenses if you wish.\n",
        style="color(10)",
        )
    track_expenses(budget, duration)


main()
