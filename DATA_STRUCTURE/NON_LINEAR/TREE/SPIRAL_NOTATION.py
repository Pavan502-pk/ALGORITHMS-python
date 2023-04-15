class Node:
    def __init__(self, data, left=None, right=None):
        self.key = data
        self.left = left
        self.right = right

def clockwise(root, level):
 
    if root is None:
        return False
 
    if level == 1:
        print(root.key, end=' ')
        return True

    left = clockwise(root.left, level - 1)
    right = clockwise(root.right, level - 1)
 
    return left or right
 
def anti_clockwise(root, level):
 
    if root is None:
        return False
 
    if level == 1:
        print(root.key, end=' ')
        return True
 

    right = anti_clockwise(root.right, level - 1)
    left = anti_clockwise(root.left, level - 1)
 
    return right or left
 
def show_clockwise(root):
 
    if root is None:
        return
 
    level = 1
    process = True
 
    while process:
        process = clockwise(root, level)
        level = level + 1
        if process:
            process = anti_clockwise(root, level)
            level = level + 1 
        
def show_ant_clockwise(root):
 
    if root is None:
        return
 
    level = 1
    process = True
 
    while process:
        process = anti_clockwise(root, level)
        level = level + 1
        if process:
            process = clockwise(root, level)
            level = level + 1 
 
if __name__ == '__main__':
 
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(60)
    root.right.left = Node(70)
    root.right.right = Node(80)
    
    print("\n")
    print("CLOCKWISE_SPIRAL -> ",end="")
    show_clockwise(root)
    print("\n")
    print("ANTI_CLOCKWISE_SPIRAL -> ",end="")
    show_ant_clockwise(root)
    print("\n")
