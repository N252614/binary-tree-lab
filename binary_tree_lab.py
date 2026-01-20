from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

# TODO: Implement the max_depth function
def max_depth(root: Optional[TreeNode]) -> int:
  
    # Base case: empty tree has depth 0
    if root is None:
        return 0

    # Recursively compute left and right subtree depths
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # Current node depth is max of children + 1
    return max(left_depth, right_depth) + 1


# TODO: Implement the lowest_common_ancestor function
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
 
    # Ensure we can compare in a consistent order
    p_val = p.val
    q_val = q.val

    # Traverse the BST using its ordering property
    current = root
    while current is not None:
        if p_val < current.val and q_val < current.val:
            # Both nodes are in the left subtree
            current = current.left
        elif p_val > current.val and q_val > current.val:
            # Both nodes are in the right subtree
            current = current.right
        else:
            # Split happens here (or one node equals current)
            return current

    # This should not happen if p and q exist in the BST 
    return root
