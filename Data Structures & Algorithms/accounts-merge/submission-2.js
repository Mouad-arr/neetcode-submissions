class Solution {
    accountsMerge(accounts) {
        const graph = new Map();

        for (let account of accounts) {

            for (let i = 1; i < account.length; i++) {
                if (!graph.has(account[i])) {
                    graph.set(account[i], []);
                }

                
                if (i > 1) {
                    graph.get(account[1]).push(account[i]);
                    graph.get(account[i]).push(account[1]);
                }
            }
        }

        const visited = new Set();
        const result = [];

        
        const dfs = (email, collected) => {
            visited.add(email);
            collected.push(email);

            for (let nei of graph.get(email) || []) {
                if (!visited.has(nei)) {
                    dfs(nei, collected);
                }
            }
        };

        
        for (let account of accounts) {
            const name = account[0];

            for (let i = 1; i < account.length; i++) {
                const email = account[i];

                if (!visited.has(email)) {
                    const collected = [];
                    dfs(email, collected);

                    collected.sort();
                    result.push([name, ...collected]);
                }
            }
        }

        return result;
    }
}