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
