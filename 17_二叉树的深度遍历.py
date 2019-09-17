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

    # def pre_travel(self):
    def pre_travel(self, node):    # 【注意】二叉树的深度遍历，要求传入根节点
        """二叉树的先序遍历：根 左 右；采用了递归的方式"""
        if node is None:
            return
        # 【注意】二叉树的先序遍历
        print(node.elem, end=" ")
        self.pre_travel(node.lchild)
        self.pre_travel(node.rchild)

    def mid_travel(self, node):
        """二叉树的中序遍历，顺序为：左 根 右"""
        if node is None:
            return
        self.mid_travel(node.lchild)
        print(node.elem, end=" ")
        self.mid_travel(node.rchild)

    def last_travel(self, node):
        """二叉树的后序遍历，顺序为：左 右 根"""
        if node is None:
            return
        self.last_travel(node.lchild)
        self.last_travel(node.rchild)
        print(node.elem, end=" ")

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
    # tree_1.pre_travel(0)    # 【注意】传入 0 系统并不能识别，所以得传入该对象的属性，在类方法中才能被识别
    tree_1.pre_travel(tree_1.root)
    print("")
    tree_1.mid_travel(tree_1.root)
    print("")
    tree_1.last_travel(tree_1.root)
    print("")
