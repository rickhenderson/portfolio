#!/usr/bin/env python
# Data Structures
# Created on: June 2, 2025
# Created by: Rick Henderson

# Implement a simple Stack data structure using Python.

DEBUG = True

class RDHStack:
    def __init__(self):
        self.stack_store = [1,3,56,7]
        print(self.stack_store)
        
        if DEBUG:
            print("[DEBUG] Stack instantiated.")

    def push(self,new_value):
        pass

    def pop(self,value):
        pass

    def __str__(self):
        return print(self.stack_store.items)

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

s1 = RDHStack()
print(s1)