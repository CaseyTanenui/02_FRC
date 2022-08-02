# Importing Statements..
import pandas

# Frames and content for export..

variable_dict = {
    "Item": ["Mugs", "Printing", "Packaging"],
    "Quantity": [300, 300, 50],
    "Price": [1, .5, 75]
}

fixed_dict = {
    "Item": ["Rent", "Artwork", "Advertising"],
    "Price": [25, 35, 10]
}

variable_frame = pandas.DataFrame(variable_dict)
fixed_frame = pandas.DataFrame(fixed_dict)

# Change dataframe to string (so it can be written to a .txt file)
variable_frame = pandas.DataFrame.to_string(variable_frame)
fixed_frame = pandas.DataFrame.to_string(fixed_frame)

product_name = "Custom Mugs"
profit_target = "$100.00"
required_sales = "$200.00"
recommended_price = "$5.00"

print(variable_frame)

to_write = [product_name, variable_frame, fixed_frame, 
profit_target, required_sales, recommended_price
]

# Write to file..
# Create file to hold data (add .txt extension)
file_name = "{}.txt".format(product_name)
text_file = open(file_name, "w+")

# Heading..
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")

# Close File
text_file.close()

# Print statements...
for item in to_write:
    print(item)
    print()