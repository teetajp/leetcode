/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        // Left, Root, Right
        vector<int> output;
        stack<TreeNode*> to_visit;
        
        while (root || !to_visit.empty()) {
            // Add current node (parennt of left child) to the stack to revisit later to add to output and traverse right subtree
            while (root) {
                to_visit.push(root);
                root = root -> left;
            }
            root = to_visit.top();
            to_visit.pop();
            output.push_back(root->val);
            root = root->right;
        }
        return output;
    }
};