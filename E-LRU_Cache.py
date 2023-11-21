'''
146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache.
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
'''


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, key, value):
        node = Node(key, value)

        tail_prev = self.tail.prev
        tail_prev.next = node
        self.tail.prev = node
        node.prev = tail_prev
        node.next = self.tail

        self.size += 1
        return node

    def pop(self):
        return self.remove(self.head.next)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.list = DoublyLinkedList()
        self.hash = {}

    def get(self, key: int) -> int:
        if key in self.hash:
            node = self.hash[key]
            self.list.remove(node)
            self.hash[key] = self.list.append(key, node.value)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.list.remove(self.hash[key])
        node = self.list.append(key, value)
        self.hash[key] = node

        if self.list.size > self.capacity:
            delete = self.list.pop()
            del self.hash[delete.key]


# capacity = 2
# key = 1
# value = 1
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
