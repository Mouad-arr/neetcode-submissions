/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    map<Node*,Node*> dict ;
    Node* dfs(Node* node){
        if(dict.find(node) != dict.end()) return dict[node];
        Node* newNode = new Node(node->val);
        dict[node]=newNode;
        for(Node* n : node->neighbors){
            newNode->neighbors.push_back(dfs(n));
        }
        return newNode;
    }
    Node* cloneGraph(Node* node) {
        if(!node) return nullptr ;
        return dfs(node);
    }
};
