#!/usr/bin/env python
# Data Structures
# Created on: June 2, 2025
# Created by: Rick Henderson

# Implement a simple Stack data structure using Python.

DEBUG = False

class RDHStack:
    def __init__(self):
        self.items = [1,3,56,7]
        
        if DEBUG:
            print("[DEBUG] Stack instantiated.")

    def push(self,new_value):
        self.items.append(new_value)
        return 1

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0
    
    def __str__(self):
        result = str(self.items)
        return result

    def elemental_print(self):
        full_stack = "["
        stack_length = len(self.stack_store)
        count = stack_length

        if count > 0:
            for element in self.stack_store:
                print(element)
                if count < stack_length:
                    full_stack += f"{str(element)},"
                else:
                    full_stack += str(element)
                count+=1

        full_stack += "]"
        return full_stack