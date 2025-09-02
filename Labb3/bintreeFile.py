

class Node:
    """
    Nod
    """
    def __init__(self, value: str):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return self.value

    def __eq__(self, other) -> bool:
        """
        kollar likhet
        :return: bool
        """
        if isinstance(other, str):
            # Jämför likhet mellan sträng och nod
            return self.value == other
        else:
            # Jämför likhet mellan nod och nod
            return self.value == other.value

    def __lt__(self, other) -> bool:
        """
        koollar olikhet
        :param other:
        :return:
        """
        if isinstance(other, str):
            return self.value < other
        else:
            return self.value < other.value

class Bintree:

    def __init__(self):
        self.root = None

    def __contains__(self, item) -> bool:
        if self.root:
            return self.check(self.root, str(item))
        else:
            return False

    def __iter__(self):
        return self._transform_to_list()

    def insert(self, node, new_node):

        if node != new_node:
            if new_node < node:
                if node.left:
                    self.insert(node.left, new_node)
                else:
                    node.left = new_node
            else:
                if node.right:
                    self.insert(node.right, new_node)
                else:
                    node.right = new_node

    def put(self, value):

        new_node = Node(str(value))

        if self.root:
            self.insert(self.root, new_node)
        else:
            self.root = new_node

    def check(self, node, item_str) -> bool:
        if node != item_str:
            if node < item_str:
                if node.right:
                    return self.check(node.right, item_str)
                else:
                    return False
            else:
                if node.left:
                    return self.check(node.left, item_str)
                else:
                    return False
        else:
            return True

    def search_and_write(self, node: Node):

        if node.left:
            self.search_and_write(node.left)

        print(f"{node} ", end="")

        if node.right:
            self.search_and_write(node.right)

    def write(self):
        self.search_and_write(self.root)
        print("\n")

    def _search_and_transform(self, node: Node, result_list):
        if node.left:
            self._search_and_transform(node.left, result_list)

        result_list.append(node)

        if node.right:
            self._search_and_transform(node.right, result_list)

    def _transform_to_list(self):
        result_list = []
        self._search_and_transform(self.root, result_list)
        return iter(result_list)