class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self, value):
        newNode = StackNode(value)
        if self.head:
            newNode.next = self.head
        self.head = newNode
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            return
        temp = self.head.value
        self.head = self.head.next
        self.size -= 1
        return temp

class Solution:
    def isValid(self, s: str) -> bool:

        matchingDict = {')': '(', ']': '[', '}': '{'}

        charStack = Stack()
        for char in s:
            if char in '({[':
                charStack.push(char)
            else:
                if matchingDict[char] != charStack.pop():
                    return False
        return charStack.size == 0
        