# Define a dictionary
customers = {'06753':'Mehzabin Afroze','02457':'Md. Ali',
'02834':'Mosarof Ahmed','05623':'Mila Hasan', '07895':'Yaqub Ali'}

# Append a new data
customers['05634'] = 'Mehboba Ferdous'

print("testing the whole thing")
print(customers)

print("testing printing an item")
print(customers['05634'])

print("The customer names are:")
# Print the values of the dictionary
for customer in customers:
    print(customers[customer])

# Take customer ID as input to search
idish = input("Enter customer ID:")

# Search the ID in the dictionary
for customer in customers:
    if customer == idish:
        print(customers[customer])
        break


customers.items()
customers.keys()
customers.values()
print(dict.fromkeys([54,123,5,3,4],[4,3,2,1,5]))