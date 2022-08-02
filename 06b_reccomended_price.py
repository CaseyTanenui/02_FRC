import math

# Checks to see if the user
# has entered an Integer that is more than zero.. 
# takes in custom error message..
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

# Rounding function...
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to

# Main Routine starts here..

how_many = num_check("How many items are you selling?: ", "Can't be 0", int)
print()
total = num_check("What is the total cost for this project?: ", "Has to be more than 0", float)
print()
profit_goal = num_check("What is your profit Goal?: ", "Has to be more than zero", float)
print()
round_to = num_check("Round to the nearest?... ", "Cannot be zero", int)

sales_needed = total + profit_goal

print("Total: ${:.2f}".format(total))
print()
print("Profit Goal: {:.2f}".format(profit_goal))

selling_price = sales_needed / how_many
print("Selling Price (unrounded): ${:.2f}".format(selling_price))

recommended_price = round_up(selling_price, round_to)
print("Recommended Price: ${:.2f}".format(recommended_price))

