from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        queue = deque([root])
        results = []
        while queue:
            node = queue.popleft()
            if node is None:
                results.append("NONE")
                continue
            results.append(str(node.val))

            queue.append(node.left)
            queue.append(node.right)  

        # temporary
        last = len(results)
        for i in range(len(results) - 1, -1, -1):
            if results[i] != "NONE":
                break
            last -= 1            
        encoded = "-".join(results[:last])
        print(encoded)
        return encoded

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        nodes = data.split("-")
        root = TreeNode(int(nodes[0]))
        queue = deque([[0, root]])
        current = 0
        while queue:
            index, node = queue.popleft()

            leftchild = current + 1
            rightchild = current + 2
            current += 2
            if leftchild < len(nodes) and nodes[leftchild] != "NONE":
                node.left = TreeNode(int(nodes[leftchild]))
                queue.append([leftchild, node.left])
            if rightchild < len(nodes) and nodes[rightchild] != "NONE":
                node.right = TreeNode(int(nodes[rightchild]))
                queue.append([rightchild, node.right])

        return root
