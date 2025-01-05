amount_due = 50
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert coin: "))
    # coins: 5, 10, 25 cents
    if coin in [5, 10, 25]:
        amount_due = amount_due - int(coin)

if amount_due < 0:
    change = -amount_due
else:
    change = amount_due

print(f"Change Owed: {change}")
