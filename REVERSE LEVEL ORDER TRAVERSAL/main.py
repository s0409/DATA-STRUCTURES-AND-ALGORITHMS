def reverselevelorder(root):
    q=deque()
    q.append(root)
    ans=deque()
    while q:
        node=q.popleft()
        if node is None:
            continue
        ans.appendleft(node.data)
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)
    return ans
