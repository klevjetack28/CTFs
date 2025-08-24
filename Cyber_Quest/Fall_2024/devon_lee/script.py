import csv
import base64

my_set = set()
customer_set = set()
my_dict = {
        "VISA": 0,
        "American Express": 0,
        "Discover": 0,
        "Mastercard": 0,
        }

with open('customerPII.csv', 'r') as file:
    next(file)
    csv_reader = csv.reader(file)
    for row in csv_reader:
        customer_set.add(row[1])
        my_set.add(row[0])
        issuer = row[0]
        my_dict[issuer] += 1

print(f"Customers effected: {len(customer_set)}")
print(f"Issuers effected: {len(my_set)}")
print(f"Most effected issuer: {my_dict}")
