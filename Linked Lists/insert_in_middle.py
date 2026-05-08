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

def insertAtEnd(data):
    global head
    nn = Node(data)
    if (head is None):
        head = nn
    else:
        curr = head
        while (curr.next is not None):
            curr = curr.next
        curr.next = nn

def insertAt(data, pos):
    global head
    nn = Node(data)
    if (head is None):
        head = nn
    else:
        curr = head
        i = 0
        while (i < pos - 1 and curr is not None and curr.next is not None):
            curr = curr.next
            i += 1
        nn.next = curr.next
        curr.next = nn

def traverse():
    curr = head
    while (curr is not None):
        print(curr.data)
        curr = curr.next

insertAtEnd("A")
insertAtEnd("B")
insertAtEnd("C")
insertAtEnd("D")
insertAt("Z", 2)
insertAt("X", 1)
insertAt("Y", 100)

traverse()
