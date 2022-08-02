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

# Main routine starts here..

# Setup Dictionaries and Lists...
item_list = []
quantity_list = []
price_list = []

variable_dict = {
    "Item": item_list,
    "Quantity": quantity_list,
    "Price": price_list
}

# Get user data..
product_name = not_blank("Product name: ", "The product name cannot be blank, please try again...")

# Loop to get component, quantity and price
item_name = ""
while item_name.lower() != "xxx":

    print()

    # Get name, quantity and item
    item_name = not_blank("Item name: ", "The component name can't be blank.")
    if item_name.lower() == "xxx":
        break
    
    quantity = num_check("Quantity: ", "The amount must be a whole number or more than zero", int)

    price = num_check("How much for a single item? $", "The price must be a number <more than zero>", float)

    # Add quantity, item and price to lists...
    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(price)

variable_frame = pandas.DataFrame(variable_dict)
variable_frame = variable_frame.set_index('Item')

# Calculate cost of each component
variable_frame['Cost'] = variable_frame['Quantity'] * variable_frame['Price']

# Find the sub total.
variable_sub = variable_frame['Cost'].sum()

# Currenct Formatting (uses currency function)
add_dollars = ['Price', 'Cost']
for item in add_dollars:
    variable_frame[item] = variable_frame[item].apply(currency)

# Printing area
print(variable_frame)

print()

print("Variable Costs: ${:.2f}".format(variable_sub))

