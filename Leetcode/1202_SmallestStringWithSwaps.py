# 1202. Smallest String With Swaps
""" The code below presents a clean Python DFS solution for this problem. The algorithm works as follows:
The initial idea is that each pair of swappable letters in "pairs" can be treated as an edge in a (undirected) graph. 

This works because, in the limit case, we could do bubble sort across connected letters.
We then go one step further and treat each index s[i] as a node, and convert the array "pairs" into a dictionary "d" of connected nodes.

While our dictionary "d" has entries, we choose one element in "d" and visit all connected nodes, returning a list of detected points. We sort this list, and place the results back in our final string/array. Since each node can only be visited once, this process has a linear time complexity of O(E), where E is the number of edges in our graph ( E = len(pairs) ).
Once all nodes have been visited, we exit our function and return the final string, with all its connected sections sorted .

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"

"""




class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        d = defaultdict(list)
        for a,b in pairs:
            d[a].append(b)
            d[b].append(a)
        

        def dfs(x,a):
            if x in d:
                a.append(x)
                for y in d.pop(x):
                    dfs(y,a)
        s = list(s)
        print(d)
        while d:
            
            x = next(iter(d))
            print(x)
            a = []
            dfs(x,a)
            a = sorted(a)
            b = sorted([s[i] for i in a])
            for i in range(len(b)):
                s[a[i]] = b[i]
            print(s)
        return ''.join(s)

        
