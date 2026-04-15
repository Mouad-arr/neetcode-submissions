/**
 * // Definition for a Node.
 * class Node {
 *     constructor(val = 0, neighbors = []) {
 *       this.val = val;
 *       this.neighbors = neighbors;
 *     }
 * }
 */

class Solution {
    map=new Map()
    dfs(node){
        if(node==null) return null;
        if( this.map.has(node)  ) return this.map.get(node);
        let newNode=new Node(node.val);
        this.map.set(node,newNode);
        for(let n of node.neighbors){
            newNode.neighbors.push(this.dfs(n));
        }
        return newNode;
    }
    /**
     * @param {Node} node
     * @return {Node}
     */

    cloneGraph(node) {
        return this.dfs(node);
    }
}