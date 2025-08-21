/**
 * // Definition for a _Node.
 * function _Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {_Node} node
 * @return {_Node}
 */
var cloneGraph = function(node) {
    if (!node) return null;
    const cloneMap = new Map();
    function dfs(originalNode) {
        if (cloneMap.has(originalNode)) {
            return cloneMap.get(originalNode);
        }
        const clone = new _Node(originalNode.val);
        cloneMap.set(originalNode, clone);
        for (let neighbor of originalNode.neighbors) {
            clone.neighbors.push(dfs(neighbor));
        }
        return clone;
    }
    return dfs(node)
};