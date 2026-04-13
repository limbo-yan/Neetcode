class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]
    
    def findNode(self, key):
        node = self.map[key % 1000]
        while node.next != None:
            if node.next.key == key:
                return node
            node = node.next
        return node

    def put(self, key: int, value: int) -> None:
        node = self.findNode(key)
        if node.next:
            node.next.val = value
        else:
            node.next = ListNode(key, value)

    def get(self, key: int) -> int:
        node = self.findNode(key)
        if node.next:
            return node.next.val
        return -1

    def remove(self, key: int) -> None:
        node = self.findNode(key)
        if node:
            node.next = node.next.next
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)