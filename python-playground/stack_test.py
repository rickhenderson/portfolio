""" 
    Test Stack module/program thingy
    For reference to remember what an ADT was https://www.geeksforgeeks.org/abstract-data-types/
"""

import RDHStack

def print_stack(any_stack):
    """Print the stack and return 1 on success."""
    print(any_stack)
    return 1

def main():
    """Testing the stack class."""
    print("[+] Test stack Class\n")

    pile = RDHStack.RDHStack()
    print(pile)

    # Push an element on top of the stack
    print("[+] Push 77 onto the stack.")
    pile.push(77)

    # Display the stack again
    print_stack(pile)

    # Push a string onto the stack
    print("[+] Push 'add ebx, [result]' onto the stack")
    pile.push("add ebx, [result]")

    # Display the stack again
    print_stack(pile)

    # Remove an item
    print(f"[+] Popped: {pile.pop()}")
    print_stack(pile)

    print(f"[+] Popped: {pile.pop()}")
    print(f"[+] Popped: {pile.pop()}")
    print(f"[+] Popped: {pile.pop()}")
    print_stack(pile)

    print(f"[+] Popped: {pile.pop()}")
    print(f"[+] Popped: {pile.pop()}")
    print_stack(pile)

    print(f"[+] Popped: {pile.pop()}")
    print_stack(pile)

if __name__ == "__main__":
    main()
