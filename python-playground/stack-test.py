# Test Stack class
# For reference to remember what an ADT was https://www.geeksforgeeks.org/abstract-data-types/

import RDHStack

def printStack(anyStack):
    print(anyStack)
    return 1

def main():
    print("[+] Test stack Class\n")

    pile = RDHStack.RDHStack()
    print(pile)

    # Push an element on top of the stack
    print("[+] Push 77 onto the stack.")
    pile.push(77)

    # Display the stack again
    printStack(pile)

    # Push a string onto the stack
    print("[+] Push 'add ebx, [result]' onto the stack")
    pile.push("add ebx, [result]")

    # Display the stack again
    printStack(pile)

    # Remove an item
    print(f"[+] Popped: {pile.pop()}")
    printStack(pile)

    print(f"[+] Popped: {pile.pop()}")
    print(f"[+] Popped: {pile.pop()}")
    print(f"[+] Popped: {pile.pop()}")
    printStack(pile)    
    print(f"[+] Popped: {pile.pop()}")
    print(f"[+] Popped: {pile.pop()}")
    printStack(pile)    
    print(f"[+] Popped: {pile.pop()}")
    printStack(pile) 

if __name__ == "__main__":
    main()
