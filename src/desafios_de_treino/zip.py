class Zipper:
    def __init__(self, value, left, right, parent=None, is_left_child=False):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.is_left_child = is_left_child
    
    @staticmethod
    def from_tree(tree):
        if tree is None:
            return None
        return Zipper._build_zipper(tree, None, False)
    
    @staticmethod
    def _build_zipper(tree, parent, is_left_child):
        if tree is None:
            return None
        
        zipper = Zipper(
            tree["value"],
            None,
            None,
            parent,
            is_left_child
        )
        
        zipper.left = Zipper._build_zipper(tree.get("left"), zipper, True)
        zipper.right = Zipper._build_zipper(tree.get("right"), zipper, False)
        
        return zipper
    
    def to_tree(self):
        if self.parent is not None:
            return self.parent.to_tree()
        
        return self._to_dict()
    
    def _to_dict(self):
        return {
            "value": self.value,
            "left": self.left._to_dict() if self.left else None,
            "right": self.right._to_dict() if self.right else None
        }
    
    def value(self):
        return self.value
    
    def left(self):
        return self.left
    
    def right(self):
        return self.right
    
    def up(self):
        return self.parent
    
    def set_value(self, value):
        return Zipper(value, self.left, self.right, self.parent, self.is_left_child)
    
    def set_left(self, left):
        if left is None:
            left_zipper = None
        else:
            left_zipper = Zipper.from_tree(left)
            if left_zipper:
                left_zipper.parent = self
                left_zipper.is_left_child = True
        
        return Zipper(self.value, left_zipper, self.right, self.parent, self.is_left_child)
    
    def set_right(self, right):
        if right is None:
            right_zipper = None
        else:
            right_zipper = Zipper.from_tree(right)
            if right_zipper:
                right_zipper.parent = self
                right_zipper.is_left_child = False
        
        return Zipper(self.value, self.left, right_zipper, self.parent, self.is_left_child)