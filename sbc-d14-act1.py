name = "IUYOTWHGJAK"
user = input("Enter keyword: ").upper()

index = name.index(user)

if user in name:
    print(f"The starting index is {index} and it ends at index {name.index(user[-1])}")
else:
    print("Not found")