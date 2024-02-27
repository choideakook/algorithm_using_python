class Node:
    def __init__(self, value=0, l=None, r=None):
        self.value = value
        self.l = l
        self.r = r

class Tree:
    def __init__(self):
        self.root = None

def dfs(now, p, q):
    if now is None:
        return None

    left = dfs(now.left, p, q)
    right = dfs(now.right, p, q)

    if now.value is p or now.value is q:
        return now.value
    elif left and right:
        return now.value
    return left or right

p, q = 5,7

ancestor = {}
print(dfs([3,5,1,6,2,0,8,None,None,7,4], p, q))