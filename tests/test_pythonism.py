from pythonismm.pythonisim_linked_list import LinkedList,Node

def test_str():
    num = LinkedList()
    num.insert(4)
    num.insert(5)
    num.insert(6)
    actual = str(num)  
    assert actual == 'The LinkedList Representation is : {6} -> {5} -> {4} ->  + NULL'



def test_get_item():
    num = LinkedList()
    num.insert(2)
    num.insert(1)
    actual = num[1]
    assert actual == 'The index of item wanted is : 2'


def test_decorator_null():
    num = LinkedList()
    num.insert(2)
    num.insert(1)
    num.insert(8)
    actual = str(num)  
    assert actual == 'The LinkedList Representation is : {8} -> {1} -> {2} ->  + NULL'


def test_decorator_index():
    num = LinkedList()
    num.insert(2)
    num.insert(1)
    actual = num[0]
    assert actual == 'The index of item wanted is : 1'