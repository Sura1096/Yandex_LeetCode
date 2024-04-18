from typing import Optional


'''
449. Serialize and Deserialize BST

Serialization is converting a data structure or object into a sequence of bits so 
that it can be stored in a file or memory buffer, 
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You need to ensure that a binary search tree can be serialized to a string, 
and this string can be deserialized to the original tree structure.
The encoded string should be as compact as possible.

Example 1:
Input: root = [2,1,3]
Output: [2,1,3]

Example 2:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 10^4].
0 <= Node.val <= 10^4
The input tree is guaranteed to be a binary search tree.
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        result = []

        def preorder(root):
            if not root:
                result.append('null')
                return
            result.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ','.join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        vals = data.split(',')
        self.i = 0

        def preorder():
            if vals[self.i] == 'null':
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = preorder()
            node.right = preorder()
            return node
        return preorder()


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# des = Codec()
# tree = ser.serialize(root)
# ans = des.deserialize(tree)
# return ans
