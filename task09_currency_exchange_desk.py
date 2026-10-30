exchange_rate = 150

usd_amount = float(input("Enter amount in USD: "))

etb_amount = usd_amount * exchange_rate

print("\n==============================")
print("       CURRENCY EXCHANGE")
print("============================")

print(f"USD Amount: {usd_amount:,}")
print(f"\nExchange Rate: 1 USD = {exchange_rate} ETB")
print(f"\nETB Amount: {etb_amount:,.2f} ETB")

print("=================...")