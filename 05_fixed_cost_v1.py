# Import Statements...
import pandas

# Checks that input is either a float or 
# an interger that is more than zero, Takes in custom error message
# Number checking function...
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))
            
            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Checks the function to see if it isn't blank...
def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)
    
        if response == "":
            print("{}. \nPlease try again.\n".format(error))
            continue

    return response

# Currency formatting function..
def currency(x):
    return "${:.2f}".format(x)

# Gets expensis, returns list which has
# The data frame and sub_total
def get_expenses(var_fixed):
    # Setup dictionaries

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # Loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()

        # Get name, quantity and item
        item_name = not_blank("Item name: ", "The component name can't be blank.")
        if item_name.lower() == "xxx":
            break
    
        if var_fixed == "variable":
            quantity = num_check("Quantity: ", "The amount must be a whole number", int)
        else:
            quantity = 1

        price = num_check("How much? $", "The price must be a number more than zero", float)

        # Add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = fixed_frame.set_index('Item')

    # Calculate the cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # Find sub total..
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]
    
# Main routine starts here

# Get product name 
# Product_name = not_blank("Product Name: ", "The product name cannot be blank)

fixed_expenses = get_expenses("fixed")
fixed_frame = fixed_expenses[0]
fixed_sub = fixed_expenses[1]

# Printing area..

print()
print(fixed_frame[['Cost']])
print()

print("Fixed Costs: ${:.2f}".format(fixed_sub))