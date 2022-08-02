# Functions go here..

# Checks that user has correctly entered yes or no into the question...
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
            dollar_type = yes_no("Do you mean ${:.2f} | ie {:2.f} dollars | y / n".format(amount, amount))

            # Set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no("Do you mean {}%? y / n".format(amount))

            if percent_type == "$":
                profit_type = "%"  
            else:
                profit_type = "$"

            # Return profit goal to main routine
            if profit_type == "$":
                return amount
            else:
                goal = (amount / 100) * total_costs
                return goal

                

          