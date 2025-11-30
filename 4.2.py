class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, value):
    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert_node(root.left, value)
    elif value > root.value:
        root.right = insert_node(root.right, value)
    
    return root

def get_height(node):
    if node is None:
        return 0
    
    left_height = get_height(node.left)
    right_height = get_height(node.right)
    
    return max(left_height, right_height) + 1

def is_balanced(node):
    if node is None:
        return True
    
    left_height = get_height(node.left)
    right_height = get_height(node.right)
    
    if abs(left_height - right_height) > 1:
        return False
    
    return is_balanced(node.left) and is_balanced(node.right)

def main():
    data = input().split()
    numbers = []
    
    for num_str in data:
        num = int(num_str)
        if num == 0:
            break
        numbers.append(num)
    
    root = None
    for num in numbers:
        root = insert_node(root, num)
    
    if is_balanced(root):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()