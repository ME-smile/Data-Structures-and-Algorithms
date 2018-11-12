class Node:
    def __init__(self,element):
        self.element = element
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=new Node('head')

    def find(self,item):
        currentNode = self.head
        while self.element != item and currentNode:
            ''' there are two situations of getting out of loop：
            ①currentNode is the last Node ,it means that after traversing the whole list and still not find the item 
            ②find the item in the list .
            '''
            currentNode = currentNode.next
        return currentNode

    def retrieve(self,pos):
        currentNode = self.head
        i = 0
        while i < pos and currentNode:
            currentNode=currentNode.next
            i += 1
        if i == pos and currentNode:
            return currentNode

    def insert(self,pos,item):
        previousNode = self.find(pos-1)
        newNode = Node(item)
        newNode.next = previousNode.next
        previousNode.next = newNode

    def remove(self,pos):
        previousNode = self.find(pos-1)
        currentNode = self.find(pos)
        previousNode.next = currentNode.next 
        currentNode = null

    




