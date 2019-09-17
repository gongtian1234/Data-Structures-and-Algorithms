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
        self.root = None    # 用于存放根节点，一开始根节点默认为空

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]   # 用来存放节点，且在下面是一端取，一端添加
        while queue:    # 用于驱动整个程序往复循环，只要queue不为空则一直找空
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
