class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        runner = self.head
        if self.head == None:
            return -1
        if index == 0:
            return self.head.val
        for i in range(index):
            if (i == index - 1):
                if runner.next is not None:
                    return runner.next.val
                else:
                    return -1
            else:
                if runner.next == None:
                    return -1
                runner = runner.next

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def insertTail(self, val: int) -> None:
        if self.head == None:
            newHead = Node(val)
            newHead.next = None
            self.head = newHead
            return
        runner = self.head
        while runner and runner.next is not None:
            runner = runner.next
        runner.next = Node(val)

    def remove(self, index: int) -> bool:
        runner = Node(None)
        runner.next = self.head
        i = -1
        while runner.next is not None:
            if i != index - 1:
                runner = runner.next
                i += 1
            else:
                if index == 0:
                    self.head = self.head.next
                runner.next = runner.next.next
                return True
        return False

    def getValues(self) -> List[int]:
        values = []
        runner = self.head
        while runner is not None:
            values.append(runner.val)
            runner = runner.next
        return values
        
        
