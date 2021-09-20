from functools import wraps
from time import sleep

def decorate_null(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        return_val = func(*args, **kwargs)

        decorator = f'The LinkedList Representation is : {return_val} + NULL'

        return decorator

    return wrapper
def decorate_index(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        return_val = func(*args, **kwargs)

        decorator = f'The index of item wanted is : {return_val}'

        return decorator

    return wrapper

class Node: # its has two thing associated with it the the data(values) and the pointer for the next value
    def __init__(self,value = '' ):
        self.value = value
        self.next= None # in ordder to be able to create node without data 
    
    def __str__(self):
        return str(self.value)




class LinkedList():
    
    def __init__(self):
        self.head = None

    all_values = 0
   
    def insert(self,value):

        node = Node(value)
        
        
        if self.head:
            node.next = self.head
        
        
        self.head = node

        

    def __iter__(self):

        current = self.head

        while current : 
           yield current.value 
           current = current.next
    

    @decorate_null   
    def __str__(self):
       
        string = ""
        for value in self:
            string = string + f"{ {value} } -> "
        
        return string
        
    @decorate_index
    def __getitem__(self, index):
   
        if index < 0:
           raise IndexError

        for i, elemant in enumerate(self):
            if i == index:
               return elemant
        
        raise IndexError





if __name__ == '__main__' :
   num = LinkedList()
   num_2 = LinkedList()
   num_4 = LinkedList()
   num.insert(2)
   num.insert(1)
   num.insert(8)
   print(num)
   print(num[1])