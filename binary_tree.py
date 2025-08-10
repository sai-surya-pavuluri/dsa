from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def build_tree(self, values):
        if not values:
            self.root = None
            return
        n = len(values)

        def form(i):
            if i >= n or values[i] is None:
                return None
            node = TreeNode(values[i])
            node.left = form(2 * i + 1)
            node.right = form(2 * i + 2)
            return node

        self.root = form(0)

    def show_tree(self, order="in_order"):
        if order == "in_order":
            print(*self.in_order(self.root), sep=" ")
        elif order == "pre_order":
            print(*self.pre_order(self.root), sep=" ")
        elif order == "post_order":
            print(*self.post_order(self.root), sep=" ")
        elif order == "level_order":
            print(*self.level_order(), sep=" ")
        else:
            raise ValueError("order must be one of: in_order, pre_order, post_order, level_order")

    def in_order(self, node):
        if not node:
            return []
        return self.in_order(node.left) + [node.value] + self.in_order(node.right)

    def pre_order(self, node):
        if not node:
            return []
        return [node.value] + self.pre_order(node.left) + self.pre_order(node.right)

    def post_order(self, node):
        if not node:
            return []
        return self.post_order(node.left) + self.post_order(node.right) + [node.value]
    
    def level_order(self):
        if not self.root:
            return []
        q = deque([self.root])
        out = []
        while q:
            node = q.popleft()
            out.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return out
    
    def node_count(self, node):
        if not node:
            return 0
        return 1 + self.node_count(node.left) + self.node_count(node.right)


if __name__ == "__main__":
    t = Tree()
    t.build_tree([1,2,3,4,5,6,7])
    t.show_tree("post_order")
    t.show_tree("level_order")
    print("Nodes:", t.node_count(t.root))
