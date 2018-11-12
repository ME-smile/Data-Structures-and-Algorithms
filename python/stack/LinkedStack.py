'''
    Through previous studies,we have implemented SeqStack in python.But it exists a flaw that the memory
is preassigned.We never exactly know how much memroy is appropriate.less is not convient for maintain,lager
then waste memory.ha???then what can we do to handle it.So,we can imagine using linked list structure to solve 
the problem.
    Then anther question is coming,if we use single linkedlist,which end we chose to be the top of the stack?
let us analyse the time complexity of the both.if we chose the end of the tail node,it takes O(1),to insert an 
element,and it takes O(n) to remove an element.How about the other case?it takes  O(1) time to insert or remove
an element.it is no hard to tell out which is better.

'''
class Node:
    def __init__(self,item):
        self.element = item
        self.next = None

class LinkedStack:
    def __init__(self):
        self.head = Node('head')
        self.top = -1

    def is_empty(self):
        return self.head.next is None

    def push(self,item):
        currentNode = self.head
        newNode =  Node(item)
        newNode.next = currentNode.next
        currentNode.next =newNode
        self.top += 1

    def pop(self):
        currentNode =self.head
        if currentNode.next:
            nextNode = currentNode.next
            currentNode.next = nextNode.next
            self.top -= 1
            return nextNode
        else:
            return 'Stack is empty'

    def len(self):
        return self.top + 1




