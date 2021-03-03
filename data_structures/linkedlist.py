class node:
    def __init__(self, data):
        self.item = data
        self.next = None

class linked_list:

    def __init__(self):
        self.head = None
        self.count = 0;

    def add(self, element):
        if(self.head is None):
            self.head = node(element)
        else:
            temp =  node(element)
            temp.next = self.head
            self.head = temp
        self.count += 1
    
    def print_list (self):
        temp = self.head
        while temp is not None:
            print(temp.item)
            temp = temp.next


myll = linked_list()

myll.add(2)
myll.add(4)
myll.add(0)
myll.add(10)

print(type(myll))
myll.print_list();

# https://realpython.com/linked-lists-python/


