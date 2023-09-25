#Доработать бинарное дерево с семинара, добавить подсчет количества элементов, вывод всего дерева на экран, удаление элемента.

class Node:
    """узел содержит всебе значение левого потоска и праввого потомка"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        """вывод узла"""
        if self.value == None: res = "n"
        else:
            res = f'{self.value}'
        # if self.left:
        #     res =  res + " " + f'\n{self.left.value}'
        # if self.right:
        #     res += f'  {self.right.value}'
        return res


class BinaryTree:
    """класс дерева содеожет в себе корень дерева"""
    def __init__(self, root_value):
        self.root = Node(root_value)

    def add(self, value):
        """добавить узел"""
        res = self.search(self.root, value)
        
        if res[0] is None:
            new_node = Node(value)
            if value > res[1].value:
                res[1].right = new_node
            else:
                res[1].left = new_node
        else:
            print("Хорош")

    def search(self, node, value, parent=None):
        """поиск узла по значению возвращает предка и сам узел в виде списка"""
        if node == None or value == node.value:
            return node, parent
        if value > node.value:
            return self.search(node.right, value, node)
        if value < node.value:
            return self.search(node.left, value, node)



    def size(self, node):
        """подсчет количиства узлов"""
        if node == None: return 0
        return (self.size(node.left)+1+self.size(node.right))
        

    def height(self, node):
        """водсчет высоты дерва(нужен для обхода в ширину)"""
        if not node:
            return 0
        l_height = self.height(node.left) 
        r_height = self.height(node.right) 
        return max(l_height, r_height) + 1


            
    def print_tree(self, node):
        """вывод дерева в консоль(в зависимости от урвня по несложной формуле добавляю пробеллы)"""
        h = self.height(node)
        for i in range(h):
            if i == 0:
                print((((h-i)*2)-1)*" ", end = "")
            else:
                print((h-i)*2*" ", end = "")
            self.print_level(node, i)
            print('\n')
        


    def print_level(self, node, level ):
        """обход в ширину и вывод по уровнего если значение нет выдает n(None) важный момент, если глубина одной из веток сильно ,больше остальных пустые места он также заполняет буквой n(None)"""
        if not node:
            return print("n", end =" ")
        if level == 0:
            print (node, end =" ")
        elif level > 0:
            self.print_level(node.left, level - 1)
            self.print_level(node.right, level - 1)


    def del_node(self, value):
        """удаления узла(важно, данным методом корень удалить нельзя)"""
        res = self.search(self.root, value)
        if res[0] != None:
            if (res[0].left == None)&(res[0].right == None):
                if (res[1].left == res[0]):
                    res[1].left = None
                else:
                    res[1].right = None
            elif (res[0].left != None)&(res[0].right == None):
                if (res[1].left == res[0]):
                    res[1].left, res[0].left = res[0].left , None
                else:
                    res[1].right, res[0].left = res[0].left , None
            elif (res[0].left == None)&(res[0].right != None):
                if (res[1].left == res[0]):
                    res[1].left, res[0].right = res[0].right , None
                else:
                    res[1].right, res[0].right = res[0].right , None

bt = BinaryTree(5)
bt.add(9)
bt.add(8)
bt.add(3)
bt.add(2)
bt.add(1)
bt.add(4)
bt.add(6)
bt.add(7)





print(bt.size(bt.root))
bt.print_tree(bt.root)
bt.del_node(9)
bt.print_tree(bt.root)
bt.del_node(8)
bt.print_tree(bt.root)
bt.del_node(4)
bt.print_tree(bt.root)
bt.del_node(7)
bt.print_tree(bt.root)
bt.del_node(3)
bt.print_tree(bt.root)