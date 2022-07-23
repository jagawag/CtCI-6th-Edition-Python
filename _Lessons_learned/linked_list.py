# https://realpython.com/linked-lists-python/
'''
Variable names
data
next
current
target
prev

Remember

class Node
__iter__(self,data=None,next=None)

class LinkedList
__init__(data_list=None)
__repr__()
"".join([])
__iter__()
yield


'''

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self,data_list=None):
        self.head = None
        node = None
        if data_list:
            self.head = Node(data_list.pop())
            node = self.head
            node.next = None
        while data_list:
            node.next = Node(data_list.pop())
            node = node.next
            node.next = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node
        node.next = None

    # Alternative
    # For loop uses __iter__() to yield last node via multiple passes
    def add_end(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    # stop at pos before provided index
    def insert_at(self,node,index):
        pos = 0
        current = self.head
        while current.next and (pos < index - 1): # stop node before replacement site
            current = current.next
            pos += 1
        if pos == index - 1:
            node.next = current.next
            current.next = node
        else:
            raise Exception("Index does not exist. Last index is: "+ str(pos+1))

    def add_after(self,node,target):
        if self.head is None:
            raise Exception("List is empty")
        for current in self:
            if current.data == target:
                node.next = current.next
                current.next = node
                return
        raise Exception(f"Node with data ({target}) not in list")

    '''Must keep track of node before target (i.e. prev)'''
    def add_before(self,node,target):
        prev = self.head
        current = self.head
        if self.head is None:
            raise Exception("List is empty")
        if self.head.data == target:
            return self.add_first(node)
        while current.data != target and (current.next):
            prev = current
            current = current.next
        if current.data == target:
            node.next = current
            prev.next = node
            return
        raise Exception(f"Node with data ({target}) not in list")

if __name__ == "__main__":
    l = LinkedList(["a","b","c"])
    print(l)
    for node in l:
        print(node)
    l.add_first(Node("j"))
    print(l)
    l.add_last(Node("z"))
    print(l)
    l.add_end(Node("e"))
    print(l)
    l.insert_at(Node("m"),6)
    print(l)
    l.add_after(Node("p"), "b")
    print(l)
    l.add_before(Node("v"), "j")
    print(l)


