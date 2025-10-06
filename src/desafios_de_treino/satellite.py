def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")
    if len(preorder) != len(set(preorder)):
        raise ValueError("traversals must contain unique items")

    if not preorder:
        return {}

    root_value = preorder[0]

    root_index_inorder = inorder.index(root_value)

    left_inorder = inorder[:root_index_inorder]
    right_inorder = inorder[root_index_inorder + 1 :]

    left_subtree_size = len(left_inorder)

    left_preorder = preorder[1 : 1 + left_subtree_size]
    right_preorder = preorder[1 + left_subtree_size :]

    return {
        "v": root_value,
        "l": tree_from_traversals(left_preorder, left_inorder),
        "r": tree_from_traversals(right_preorder, right_inorder),
    }
