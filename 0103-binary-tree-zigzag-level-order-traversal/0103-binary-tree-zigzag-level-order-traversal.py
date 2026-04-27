class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr=[]
        def dfs(node,level):
            if not node:
                return
            if len(arr)==level:
                arr.append([])
            if level%2==0:
                arr[level].append(node.val)
            else:
                arr[level].insert(0,node.val)
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0)
        return arr
        