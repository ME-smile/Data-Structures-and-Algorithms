'''
    now we are going to talk about the deformations of liner list.first we are going to introduce stack.
stack is a kind of specific linear list,the diffrence is that the operaions on stack is restricted.if we 
want to insert elements into stack,it must be added to the top of stack.Also,if we want to remove the elements in the stack,
we can only remove it form the top of the stack.It means its insertion and remove only happened at the top of stack.Just because of this,stack has the characteristic of 'FIFO'(first in first out).
    we make this as a rule: the varible top is used for stage the position of the of top the stack element. 
    when top equal with -1,it means the stack is empty.
'''
class SeqStack:
    def __init__(self,length):
        self.length=length
        self.top=-1
        self.data=list(None for i in range(length))

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.length == length

    def len(self):
        return self.top + 1

    def push(self,item):
        if  self.top != self.length -1:
            self.data.append(item)
            self.top += 1
        else:
            return 'Stack is full'

    def pop(self):
        if self.top != -1:
            self.top -= 1
            return self.data.pop()
        else:
            return 'Stack is empty'

            



