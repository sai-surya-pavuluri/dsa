from collections import deque
from typing import Optional, List, Any


class TreeNode:
    def __init__(self, value: Any):
        self.value: Any = value
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class Tree:
    def __init__(self):
        self.root: Optional[TreeNode] = None

    # ----- Build -----
    def build_tree(self, values: List[Optional[Any]]) -> None:
        if not values:
            self.root = None
            return
        n = len(values)

        def form(i: int) -> Optional[TreeNode]:
            if i >= n or values[i] is None:
                return None
            node = TreeNode(values[i])
            node.left = form(2 * i + 1)
            node.right = form(2 * i + 2)
            return node

        self.root = form(0)

    # ----- Display Tree -----
    def show_tree(self, order: str = "in_order") -> None:
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

    # ----- Traversals -----
    def in_order(self, node: Optional[TreeNode]) -> List[Any]:
        if not node:
            return []
        return self.in_order(node.left) + [node.value] + self.in_order(node.right)

    def pre_order(self, node: Optional[TreeNode]) -> List[Any]:
        if not node:
            return []
        return [node.value] + self.pre_order(node.left) + self.pre_order(node.right)

    def post_order(self, node: Optional[TreeNode]) -> List[Any]:
        if not node:
            return []
        return self.post_order(node.left) + self.post_order(node.right) + [node.value]

    def level_order(self) -> List[Any]:
        if not self.root:
            return []
        q = deque([self.root])
        out: List[Any] = []
        while q:
            node = q.popleft()
            out.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return out

    # ----- Aggregates -----
    def node_count(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + self.node_count(node.left) + self.node_count(node.right)

    def node_sum(self, node: Optional[TreeNode]) -> Any:
        if not node:
            return 0
        return self.node_sum(node.left) + self.node_sum(node.right) + node.value

    def tree_height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(self.tree_height(node.left), self.tree_height(node.right))

    def is_present(self, node: Optional[TreeNode], check_val: Any) -> bool:
        if not node:
            return False
        if node.value == check_val:
            return True
        return self.is_present(node.left, check_val) or self.is_present(node.right, check_val)

    def max_node(self, node: Optional[TreeNode]) -> Any:
        if not node:
            return float("-inf")
        left = self.max_node(node.left)
        right = self.max_node(node.right)
        return max(left, right, node.value)

    def min_node(self, node: Optional[TreeNode]) -> Any:
        if not node:
            return float("inf")
        left = self.min_node(node.left)
        right = self.min_node(node.right)
        return min(left, right, node.value)

    def leaf_node_count(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return self.leaf_node_count(node.left) + self.leaf_node_count(node.right)

    # ----- Equality & Copy -----
    @staticmethod
    def equal(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.value != b.value:
            return False
        return Tree.equal(a.left, b.left) and Tree.equal(a.right, b.right)

    def copy(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if node is None:
            return None
        new_node = TreeNode(node.value)
        new_node.left = self.copy(node.left)
        new_node.right = self.copy(node.right)
        return new_node

    def copy_tree(self) -> "Tree":
        t2 = Tree()
        t2.root = self.copy(self.root)
        return t2


if __name__ == "__main__":
    t = Tree()
    t.build_tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    t.show_tree("post_order")
    t.show_tree("level_order")
    print("Leaf nodes:", t.leaf_node_count(t.root))
    t2 = t.copy_tree()
    print("Equal copies:", Tree.equal(t.root, t2.root))