
print("** Lists are an ordered collection with duplicate members allowed. Changeable. **")
myList = [1, 2, 5, 99, "car"]

print(f"Starting list: {myList}")

value = myList.pop()

print(f"Popped: {value}")
print(myList)

print(f"Length: {len(myList)}")

newValue = 77
myList.append(newValue)
print(f"New values can be appended to the end of the list: {myList}")


