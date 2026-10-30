customer = input("Enter customer name: ")
product = input("Enter product name: ")
price = float(input("Enter product price (ETB): "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("\n========================================")
print("                 RECEIPT")
print("========================================")

print(f"Customer: {customer}")

print(f"\n{'Product':<15} {'Price':<10} {'Quantity':<5}")
print("----------------------------------------")

print(f"{product:<15} {price:<10} {quantity:<5}")

print("----------------------------------------")
print(f"Total: {total:} ETB")

print("\nThank you for shopping!")
print("========================================")