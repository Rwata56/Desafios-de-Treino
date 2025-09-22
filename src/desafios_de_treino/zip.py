class Zipper:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        
        # Configura o parent dos filhos
        if self.left is not None:
            self.left.parent = self
        if self.right is not None:
            self.right.parent = self

    @staticmethod
    def from_tree(tree):
        if tree is None:
            return None
        
        left = Zipper.from_tree(tree.get("left"))
        right = Zipper.from_tree(tree.get("right"))
        
        return Zipper(tree["value"], left, right)

    def to_tree(self):
        # Encontra a raiz
        current = self
        while current.parent is not None:
            current = current.parent
        
        return current._to_dict()

    def _to_dict(self):
        return {
            "value": self.value,
            "left": self.left._to_dict() if self.left else None,
            "right": self.right._to_dict() if self.right else None
        }

    @property
    def up(self):
        return self.parent

    def set_value(self, value):
        """Cria um novo zipper com o valor modificado"""
        new_zipper = Zipper(value, self.left, self.right, self.parent)
        return self._update_parent(new_zipper)

    def set_left(self, left):
        """Cria um novo zipper com a subárvore esquerda modificada"""
        left_zipper = Zipper.from_tree(left) if left is not None else None
        new_zipper = Zipper(self.value, left_zipper, self.right, self.parent)
        return self._update_parent(new_zipper)

    def set_right(self, right):
        """Cria um novo zipper com a subárvore direita modificada"""
        right_zipper = Zipper.from_tree(right) if right is not None else None
        new_zipper = Zipper(self.value, self.left, right_zipper, self.parent)
        return self._update_parent(new_zipper)

    def _update_parent(self, new_child):
        """Atualiza o pai com o novo filho - CORREÇÃO AQUI"""
        if self.parent is None:
            return new_child  # CORREÇÃO: era 'new_zipper', deve ser 'new_child'
        
        if self.parent.left is self:
            return self.parent.set_left(new_child._to_dict())
        else:
            return self.parent.set_right(new_child._to_dict())