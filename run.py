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
    Displays the introductory text about the content of this programme
    """
    intro = open(file, 'r')
    content = intro.read()
    intro.close()
    return content


begin = get_content('intro.txt')


def main():
    """
    Main function to run the programme
    """
    console.print(welcome, style="bold #15E6E4", justify="center")
    # displays the welcome message
    console.print(begin, style="#9DE635", justify="center")
    # displays the introductory text


main()
