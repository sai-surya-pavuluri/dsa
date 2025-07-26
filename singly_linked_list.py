class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def add_first(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
    
    def add_last(self, value):
        node = Node(value)
        curr = self.head
        if curr != None: 
            while curr.next is not None:
                curr = curr.next
            curr.next = node
        else:
            self.head = node

    def is_empty(self):
        return self.head == None
    
    def find_index(self, value):
        curr = self.head
        index = 0
        while curr is not None:
            if curr.value == value:
                return index
            curr = curr.next
            index += 1
        return -1
    
    def insert_at(self, index, value):
        newNode= Node(value)
        curr = self.head
        prev = self.head
        idx = 0
        
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return True
        
        while curr is not None:
            if idx == index:
                newNode.next = curr
                prev.next = newNode
                return True
            prev = curr
            curr = curr.next
            idx += 1
        return False
    
    def length(self):
        length = 0
        curr = self.head
        while curr is not None:
            length += 1
            curr = curr.next
        return length
    
    def print_linked_list(self):
        curr = self.head
        if curr is None:
            return
        while curr.next is not None:
            print(str(curr.value), end='->')
            curr = curr.next
        print(str(curr.value), end='')

    def delete_at(self, index):
        curr = self.head
        prev = None
        idx = 0
        
        if index >= self.length():
            return False
        
        if curr is None:
            return False
        
        if index == 0:
            nextNode = self.head.next
            self.head = nextNode
            return True

        while curr is not None:
            if index == idx:
                prev.next = curr.next
                return True
            prev =  curr
            curr = curr.next
            idx += 1
        return False

    def delete_node(self, value):
        curr = self.head
        prev = self.head
        while curr is not None:
            if curr.value == value:
                if curr == self.head:
                    self.head = curr.next
                    return True
                else:
                    prev.next = curr.next
                    return True
            prev = curr
            curr = curr.next
        return False

    def get_sum(self):
        curr = self.head
        sum = 0
        while curr is not None:
            sum += curr.value
            curr = curr.next
        return sum

    def reverse(self):
        curr = self.head
        prev = None
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev