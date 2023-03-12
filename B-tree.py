import random
import math

class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insertNode(self, key):
        print("Inserimento")
        if self.key is None:
            self.key = Node(key)
        else:
            if key>self.key:
                if self.right is None:
                    self.right = Node(key)
                else:
                    self.right.insertNode(key)
                print("destra")
            elif key<self.key:
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insertNode(key)
                print("sinistra")

    def printTree(self, level=0):
        if self.left is not None:
            self.left.printTree(level+1)
        print(f"livello: ", level, " valore: ",self.key)
        if self.right is not None:
            self.right.printTree(level+1)

    def findKey(self, key):#non funzionante
        if key == self.key:
            return True
        elif self.right != None and key > self.key:
            self.right.findKey(key)
        elif self.left != None and key < self.key:
            self.left.findKey(key) 
        else:
            return False
    
    def findNode(self, key):#funzionante
        if key > self.key:
            if self.right == None:
                return f"nodo {key} non trovato"
            return self.right.findNode(key)
        elif key < self.key:
            if self.left == None:
                return f"nodo {key} non trovato"
            return self.left.findNode(key)
        else:
            return f"nodo {key} trovato"

    def heightTree(self, level=0):
        if self.left is not None:
            return self.left.heightTree(level+1)
        
        if self.right is not None:
            return self.right.heightTree(level+1)

        if self.right is not None and self.left is not None:
            return (f"livello: ", level)
        
    def height(self):
        if self.left is None:
            heightL = 0
        else:
            heightL = self.left.height()
        if self.right is None:
            heightR = 0
        else:
            heightR = self.right.height()
        if heightL > heightR:
            return heightL+1
        else:
            return heightR +1


def buildBTree(nodes):#funzione per creare l'albero bilanciato
    l = len(nodes)
    
    if l == 0:
        return None
    
    #nodes.sort()->deve essere già ordinata dal main
    m = l // 2
    root = Node(nodes[m])
    root.left = buildBTree(nodes[0:m])
    root.right = buildBTree(nodes[m+1:])
    return root

def main():
    lista_key = list(range(0, 40, 5))
    random.shuffle(lista_key)
    print(lista_key)
    root = Node(45)
    root.insertNode(50)
    root.insertNode(40)
    root.insertNode(30)

    root.printTree()

    if root.findKey(40):
        print("chiave trovata")
    else:
        print("chiave non trovata") 

    albero = Node(lista_key[0])
    for key in lista_key[1:]:
        albero.insertNode(key)

    albero.printTree()

    if albero.findKey(20):
        print("chiave trovata")
    else:
        print("chiave non trovata")    
    
    print(albero.findNode(20))

    albero.heightTree()
    lista_btree = list(range(0, 40, 5))
    random.shuffle(lista_btree)
    print(lista_btree)
    lista_btree.sort()
    bTree = buildBTree(lista_btree)
    bTree.printTree()

if __name__ == "__main__":
    main()