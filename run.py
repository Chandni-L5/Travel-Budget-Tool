from rich import print
from rich.padding import Padding
from rich.console import Console
from rich.table import Table
from rich import box
import time
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from expenses import Expense
import uuid


SCOPE = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = service_account.Credentials.from_service_account_file(
    "creds.json",
    scopes=SCOPE,
)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
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


def display_initial(document_id, user_uuid):
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
            google_doc(display_initial_text, document_id, user_uuid)
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
        expense_summary = (
            f"\nYou have added an expense of £{expense.cost:,.2f} for "
            f"{expense.description} under the category {expense.category}."
        )
        console.print(expense_summary, style="color(226) bold")
        if confirm():
            return expense
        else:
            console.print(
                "\nLet's try entering that expense again.", style="color(166)"
            )


def track_expenses(budget, duration, spending_money, document_id, user_uuid):
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

        expense_summary = (
            f"\nYou have added an expense of £{expense.cost:,.2f} for "
            f"{expense.description} under the category {expense.category}."
        )
        display_added_expense(
            expense_summary, expense, expense_totals, document_id, user_uuid
        )
        if not add_more_expenses():
            break
    google_doc_expense_summary(expense_totals, document_id, user_uuid)
    final_summary(
        budget, duration, spending_money,
        total_expenses, document_id, user_uuid
    )


def display_added_expense(
            expense_summary, expense, expense_totals, document_id, user_uuid
):
    """
    This function displays a summary of the expense added
    and also updates the running total per
    category
    """
    console.rule("")
    console.print("")
    loading_widget()
    table = Table(
        title="\n[color(51)]Expense Summary[/color(51)]",
        box=box.ASCII_DOUBLE_HEAD
    )
    table.add_column("Category", justify="left")
    table.add_column("Running Total", justify="right")
    for cat, total in expense_totals.items():
        table.add_row(f"{cat}", f"£{total:,.2f}", style="color(226)")
    console.print(table)
    google_doc(
        expense_summary,
        document_id,
        user_uuid
    )


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


def final_summary(
    budget, duration, spending_money, total_expenses, document_id, user_uuid
):
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
    exit_message(remaining_budget, duration, spending_money)
    console.print(
        f"\nYour unique summary has been saved here: "
        f"https://docs.google.com/document/d/{document_id}",
        style="bold color(51)",
    )
    console.print("")
    google_doc(summary_text, document_id, user_uuid)
    console.print("")
    console.print(
        "\nThank you for using the Travel Budget Planner!"
        "\nWe hope to see you again soon!\n",
        style="bold color(69)",
        justify="center",
    )


def exit_message(remaining_budget, duration, spending_money):
    """
    This function displays the final message and conclusion
    of the programme.
    """
    remaining_budget_per_day = remaining_budget / duration
    if remaining_budget_per_day > spending_money:
        console.print(
            "\nPack your bags and get ready for your trip! 🧳 ",
            style="bold color(10)",
        )
    else:
        console.print(
            "\nUnfortunately, your expenses "
            "have exceeded your budget. ",
            style="bold color(196)",
        )


# Google Doc Functions

def google_doc(text, document_id, user_uuid):
    """
    This function prints the summary to a google doc
    using the provided document ID
    """
    document = DOCS_SERVICE.documents().get(
        documentId=document_id
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
                    "text": f"{text}\n",
                }
            }
        ]
        DOCS_SERVICE.documents().batchUpdate(
            documentId=document_id,
            body={"requests": requests}
        ).execute()
    except HttpError as error:
        print(f"An error occurred: {error}")


def google_doc_expense_summary(expense_totals, document_id, user_uuid):
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
    full_text = "\n" + header + table
    google_doc(full_text, document_id, user_uuid)


def google_doc_final_summary(total_spent, remaining_budget, updated_daily):
    summary = (
        f"\nYour total expenses are £{total_spent:,.2f}.\n\n"
        f"You have £{remaining_budget:,.2f} left to spend on your trip.\n\n"
        f"You can spend £{updated_daily:,.2f} per day.\n"
    )
    google_doc(summary)


def create_new_google_doc():
    """
    This function creates a new Google Doc whilst returning its
    document ID and UUID. The document is also made public
    so that anyone can access it.
    """
    user_uuid = str(uuid.uuid4())
    doc_title = f"Travel Budget Planner - {user_uuid}"
    doc = DOCS_SERVICE.documents().create(
        body={"title": doc_title}
    ).execute()
    document_id = doc.get("documentId")
    public_document(document_id)
    return user_uuid, document_id


def public_document(document_id):
    """
    This function makes the Google Doc public
    so that anyone can access it.
    """
    try:
        drive_service = build("drive", "v3", credentials=SCOPED_CREDS)
        permission = {
            "type": "anyone",
            "role": "reader",
        }
        drive_service.permissions().create(
            fileId=document_id,
            body=permission,
            fields="id"
        ).execute()
    except HttpError as error:
        error_console.print(
            f"\nAn error occurred: {error}",
            style="bold red"
        )
    return


# Run programme

def main():
    """
    Main function to run the programme
    """
    user_uuid, document_id = create_new_google_doc()
    console.print(welcome, style="bold #15E6E4", justify="center")
    begin = get_content("intro.txt")
    console.print(begin, style="color(195)")
    console.rule("")
    budget, duration, spending_money = display_initial(document_id, user_uuid)
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
    track_expenses(budget, duration, spending_money, document_id, user_uuid)


main()
