//BINARY TREE PATHS

class Solution12 {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> paths = new ArrayList<>();
        if (root != null) {
            constructPaths(root, "", paths);
        }
        return paths;
    }
    private void constructPaths(TreeNode node, String path, List<String> paths) {
        if (node != null) {
            path += Integer.toString(node.val);
            if (node.left == null && node.right == null) { 
                paths.add(path); 
            } else {
                path += "->"; 
                constructPaths(node.left, path, paths);
                constructPaths(node.right, path, paths);
            }
        }
    }
}