# product_name = "bananas"
# price = 1.23
# product_id = 123456
# format_string = "The price of these %s id: %d are %.2f " % (product_name, product_id, price)
# print(format_string)

my_string = "Hello, World"

# print string length
print(len(my_string))  # 12 print string length

# print index (desired at rld in this case)
print(my_string.index("rld"))  # 9 print index starting at r of rld

# count occurrences
print(my_string.count('l'))  # 3 how often l appreas in the string
print(my_string.count('He'))  # 1 how often He appreas in the string

#  slice strings
print(my_string[1:4])  # ell is the slice starting at 1 and ending at 3 or before 4
