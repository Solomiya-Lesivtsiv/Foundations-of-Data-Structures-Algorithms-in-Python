class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

def insertAtTop(data):
    global head
    nn = Node(data)
    if (head is None):
        head = nn
    else:
        nn.next = head
        head = nn

def traverse():
    curr = head
    while (curr is not None):
        print(curr.data)
        curr = curr.next

insertAtTop("A")
insertAtTop("B")
insertAtTop("E")
insertAtTop("C")

traverse()
