/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func helper(root *TreeNode, res *[]int) {
    if root == nil {
        return
    }
    helper(root.Left, res)
    *res = append(*res, root.Val)
    helper(root.Right, res)
}

func inorderTraversal(root *TreeNode) []int {
    res := []int{}
    helper(root, &res)
    return res
}