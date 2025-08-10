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
    
    def node_sum(self, node):
        if not node:
            return 0
        return self.node_sum(node.left) + self.node_sum(node.right) + node.value
    
    def tree_height(self, node):
        if not node:
            return 0
        return max(self.tree_height(node.left), self.tree_height(node.right)) + 1
    
    def is_present(self, node, checkVal):
        if not node:
            return False
        if node.value == checkVal:
            return True
        return self.is_present(node.left, checkVal) or self.is_present(node.right, checkVal)
    
    def max_node(self, node):
        if not node:
            return float('-inf')
        highest = node.value
        left = self.max_node(node.left)
        right = self.max_node(node.right)
        return max(left, right, highest)

    def min_node(self, node):
        if not node:
            return float('inf')
        least = node.value
        left = self.min_node(node.left)
        right = self.min_node(node.right)
        return min(left, right, least)
    
    def leaf_node_count(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return self.leaf_node_count(node.left) + self.leaf_node_count(node.right)
    
    @staticmethod
    def equal(tree_1_node, tree_2_node):
        if tree_1_node == None and tree_2_node == None:
            return True
        if tree_1_node == None or tree_2_node == None:
            return False

        return Tree.equal(tree_1_node.left, tree_2_node.left) and Tree.equal(tree_1_node.right, tree_2_node.right) and tree_1_node.value == tree_2_node.value



if __name__ == "__main__":
    t = Tree()
    t.build_tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    t.show_tree("post_order")
    t.show_tree("level_order")
    print("Nodes:", t.leaf_node_count(t.root))
