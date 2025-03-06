class ListNode:
    def __init__(self,key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.check = {}

    def get(self, key: int) -> int:
        if key not in self.check:
            return -1
        node = self.check.get(key)
        self.deleteNode(node)
        self.addToHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.check:
            node = self.check[key]
            node.val = value
            self.deleteNode(node)
            self.addToHead(node)
        else:
            if len(self.check) == self.capacity:
                node = self.tail.prev
                self.check.pop(node.key)
                self.deleteNode(node)
            newNode = ListNode(key,value)
            self.check[key] = newNode
            self.addToHead(newNode)
        

    def addToHead(self, node):
        after = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = after
        after.prev = node

    def deleteNode(self,node):
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before
        node.prev = None
        node.next = None
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)