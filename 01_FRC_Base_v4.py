# import libraries...
import re
import pandas

# Functions Go Here..

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

# Checks that user has entered either 'yes' or 'no'...
def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return response

        print("Please enter either yes or no...\n")

# Checks that user has not completed anything with blank errors
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

# Gets expenses, returns a list which has..
# Gets expenses, returns a list which has..
# The data-frame and sub-total...
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
        print("The item you have chosen is: ", item_name)
        print()

        if item_name.lower() == "xxx":
            break
    
        quantity = num_check("Quantity", "The component name cannot be blank", int)
        
        price = num_check("How much? $", "The price must be a number more than zero", float)

        # Add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate the cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # Find sub total..
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]

# Prints expenses frame..
def expense_print(heading, frame, subtotal):
    print()
    print("** {} Costs **".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))
    return ""

# Shows what the profit goal may be..
def profit_goal(total_costs): 

   # Initialise variables and error messages
   error = "Please enter a valid profit goal: \n"

   valid = False
   while not valid:
        # ask for the profit goal..
        response = input("What is your profit goal (for example: $500 to $1000)?: ") 

        # Checks if first character is $...
        if response[0] == "$":
            profit_type = "$"
            # Get amount (everything after the $)
            amount = response[1:]

        # Check if last character is %
        elif response [-1] == "%":
            profit_type = "%"
            # Get amount (everything before the %)
            amount = response[:-1]

        else:
            # set response for amount for now 
            profit_type = "unknown"
            amount = response

        try:
            # Check amount is a number more than zero
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue
        
        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no("Do you mean ${:.2f} | ie {:.2f} dollars | y / n".format(amount, amount))

            # Set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no("Do you mean {}%? y / n:  ".format(amount))

            if percent_type == "$":
                profit_type = "%"  
            else:
                profit_type = "$"
                return amount

            # Return profit goal to main routine
            if profit_type == "$":
                return amount
            else:
                goal = (amount / 100) * total_costs
                return goal

# Main routine starts here..

# Get product name 
product_name = not_blank("Product Name: ", "The product name cannot be blank")

print()
print("Please enter your variable cost below..")

# Get variable costs..
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("Do you have fixed costs y / n? ")

if have_fixed == "yes":
    # Get fixed costs..
    fixed_expenses = get_expenses("fixed")
    fixed_frame = variable_expenses[0]
    fixed_sub = fixed_expenses[1]
else:
    fixed_sub = 0

# work out total costs and profit target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal(all_costs)

# Calculate reccommended price
selling_price = 0

# Printing area..

print()
print("** Fund Raising Program for - {} **".format(product_name))
print()
expense_print("Variable: ", variable_frame, variable_sub)

if have_fixed == "yes":
    expense_print("Fixed", fixed_frame[['Cost']], fixed_sub)

print()
print("** Total Costs for {} | ${:.2f} |".format(product_name, all_costs))
print()

print()
print("** Profit & Sales Targets for {}".format(product_name))
print("Profit Target: | ${:.2f} |".format(profit_target))
print("Total Sales: | ${:.2f} |".format(all_costs, profit_target))

print()
print("** Recommended Selling Price: | {:.2f} |**")
