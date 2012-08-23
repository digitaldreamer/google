#!/usr/bin/env python
class BinaryTree(object):
    """
    basic implamentation of a Binary Search Tree

    each node has maximum of 2 children
    for this implamentation each node is unique (doesn't always have to be that way)
    use recursion

    depends entirely on insert order to be balenced
    """
    root = None

    def add(self, data):
        """
        small wrapper to abstract the tree/node structure
        """
        if not self.root:
            self.root = Node(data)
            return self.root
        else:
            return self._add(self.root, data)

    def _add(self, root, data):
        # check root
        if not root:
            return None

        # find insertion point
        if self.root.data == data:
            return None
        if root.data < data:
            if not root.right:
                root.right = Node(data)
                return root.right
            else:
                return self._add(root.right, data)
        elif root.data > data:
            if not root.left:
                root.left = Node(data)
                return root.left
            else:
                return self._add(root.left, data)

    def delete(self, data):
        # find element: hold on to the parent node
        if not self.root:
            return False
        elif self.root.data == data:
            parent = None
            node = self.root
        else:
            parent, node = self._find_parent_node(self.root, data)

        if node:
            number_of_children = node.number_of_children

            # if node has one child then link the node's parent to its child
            if number_of_children == 1:
                if not parent:
                    self.root = node.get_child()
                elif parent.left == node:
                    parent.left = node.get_child()
                elif parent.right == node:
                    parent.right = node.get_child()

                return True

            # if node has two children then link smallest child of right branch to its parent
            elif number_of_children == 2:
                right_root = self._root_smallest_node(node.right)
                right_root.left = node.left

                if not parent:
                    self.root = right_root
                elif parent.left == node:
                    parent.left = right_root
                elif parent.right == node:
                    parent.right = right_root

                return True

            # if node has no children then just delete node
            else:
                if not parent:
                    self.root = node
                if parent.left == node:
                    parent.left = None
                elif parent.right == node:
                    parent.right = None

                return True

        return False

    def _root_smallest_node(self, root):
        """
        rearange the tree to make the smallest node the root
        """
        if not root.left:
            return root

        smallest_node_parent = self._smallest_node_parent(root)

        if smallest_node_parent:
            smallest_node = smallest_node_parent.left
            smallest_node_parent.left = smallest_node.right
        else:
            smallest_node = root

        # rearange smallest_node children
        smallest_node.left = None
        smallest_node.right = root

        return smallest_node

    def _smallest_node_parent(self, root):
        """
        returns the parent of the smallest node of the tree
        """
        if not root.left:
            return None
        elif not root.left.left:
            return root
        else:
            return self._smallest_node_parent(root.left)
        
    def _find_parent_node(self, root, data):
        """
        finds the parent node of the data element
        """
        if root.left and root.left.data == data:
            return root, root.left
        elif root.right and root.right.data == data:
            return root, root.right

        if root.data > data and root.left:
            return self._find_parent_node(root.left, data)
        elif root.data < data and root.right:
            return self._find_parent_node(root.right, data)

        # we didn't find a match
        return None, None

    def max(self):
        """
        return the maximum node
        """
        if not self.root:
            return None

        return self._max(self.root)

    def _max(self, root):
        if root.right:
            return self._max(root.right)
        else:
            return root

    def min(self):
        """
        return the minimum node
        """
        if not self.root:
            return None

        return self._min(self.root)

    def _min(self, root):
        if root.left:
            return self._min(root.left)
        else:
            return root

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, root, data):
        if not root:
            return None
        elif root.data == data:
            return root
        elif root.data > data:
            return self._search(root.left, data)
        else:
            return self._search(root.right, data)

    def traverse(self, method='inorder'):
        if method == 'inorder':
            self.traverse_inorder(self.root)
        elif method == 'postorder':
            self.traverse_postorder(self.root)
        elif method == 'preorder':
            self.traverse_preorder(self.root)

    def traverse_inorder(self, root):
        if not root:
            return

        self.traverse_inorder(root.left)
        self._process_node(root)
        self.traverse_inorder(root.right)

    def traverse_preorder(self, root):
        if not root:
            return

        self._process_node(root)
        self.traverse_preorder(root.left)
        self.traverse_preorder(root.right)

    def traverse_postorder(self, root):
        if not root:
            return

        self.traverse_postorder(root.left)
        self.traverse_postorder(root.right)
        self._process_node(root)

    def _process_node(self, node):
        print node.data


class Node(object):
    data = None
    left = None
    right = None

    def __init__(self, data):
        self.data = data

    def __unicode__(self):
        return '%s' % self.data

    @property
    def number_of_children(self):
        if self.left and self.right:
            return 2
        elif self.left and not self.right:
            return 1
        elif not self.left and self.right:
            return 1
        else:
            return 0

    def get_child(self):
        if self.left and not self.right:
            return self.left
        elif not self.left and self.right:
            return self.right
        else:
            return None


if __name__ == '__main__':
    tree = BinaryTree()
    tree.add(20)
    tree.add(10)
    tree.add(70)
    tree.add(40)
    tree.add(80)
    tree.add(30)
    tree.add(35)
    tree.add(60)
    tree.add(50)
    tree.add(55)

    print 'Search 10: %s' % tree.search(10).data
    print 'Search 20: %s' % tree.search(20).data
    print 'Search 50: %s' % tree.search(50).data
    print 'Search 550: %s' % tree.search(550)
    print 'Min: %s' % tree.min().data
    print 'Max: %s' % tree.max().data

    tree.delete(40)

    print 'postorder'
    tree.traverse('inorder')

    print 'preorder'
    tree.traverse('preorder')

    print 'postorder'
    tree.traverse('postorder')
