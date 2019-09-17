# 二叉树
class Node(object):
    """二叉树的单个节点"""

    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    """二叉树"""

    def __init__(self):
        self.root = None  # 用于存放根节点，一开始根节点默认为空

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]  # 用来存放节点，且在下面是一端取，一端添加
        while queue:  # 用于驱动整个程序往复循环，只要queue不为空则一直找空
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """二叉树的广度遍历"""
        # 【二叉树的广度遍历】
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
        print("")

if __name__ == "__main__":
    tree_1 = Tree()
    tree_1.add(0)
    tree_1.add(1)
    tree_1.add(2)
    tree_1.add(3)
    tree_1.add(4)
    tree_1.add(5)
    tree_1.add(6)
    tree_1.add(7)
    tree_1.add(8)
    tree_1.add(9)
    tree_1.breadth_travel()    # 0 1 2 3 4 5 6 7 8 9
    tree_2 = Tree()
    tree_2.breadth_travel()
