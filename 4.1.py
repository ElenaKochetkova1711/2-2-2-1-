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

def find_single_child_nodes(root, result):
    if root is None:
        return
    
    children_count = 0
    if root.left is not None:
        children_count += 1
    if root.right is not None:
        children_count += 1
    
    if children_count == 1:
        result.append(root.value)
    
    find_single_child_nodes(root.left, result)
    find_single_child_nodes(root.right, result)

def main():
    numbers = list(map(int, input().split()))
    
    numbers = [x for x in numbers if x != 0]
    
    root = None
    for num in numbers:
        root = insert_node(root, num)
    
    result = []
    find_single_child_nodes(root, result)
    
    result.sort()
    
    for num in result:
        print(num, end=' ')
    print()

if __name__ == "__main__":
    main()