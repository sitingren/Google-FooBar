from math import factorial
def combinations(n, r):
    # n! / r! / (n-r)!
    return factorial(n) / factorial(r) / factorial(n-r)
    
def answerHelper(seq):   
    # Base Case: the root is an empty tree
    if len(seq) == 0:
        return 1
    
    # Get left subtree and right subtree
    root = seq[0]
    left_tree = list()
    right_tree = list()
    for i in seq[1:]:
        if i > root:
            left_tree.append(i)
        else:
            right_tree.append(i)

    l_len = len(left_tree)
    r_len = len(right_tree)
    
    # Recursively count the result for each subtree
    left_result = answerHelper(left_tree)
    right_result = answerHelper(right_tree)
    
    # Number of ways to interleave two subtrees
    # Choose l_len positions among (l_len + r_len) positions
    interleave = combinations(l_len + r_len, l_len)
    return interleave * left_result * right_result 
        

def answer(seq):
    if seq is None or len(seq) == 0:
        return 1
    return "%d" % answerHelper(seq)    