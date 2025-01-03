user = input("Greeting: ").lower().strip()
print(user)
if (user.startswith("hello ") or user.startswith("hello")):
    print("$0")
elif user.startswith("h"):
    print("$20")
else:
    print("$100")

