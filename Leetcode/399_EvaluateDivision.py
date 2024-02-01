"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.
You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.
Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.
Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        paird = {}
        allvar = set()
        
        for i in range(len(equations)):
            paird[(equations[i][0], equations[i][1])] = values[i]
            paird[(equations[i][1], equations[i][0])] = 1 / values[i]
            allvar.add(equations[i][0])
            allvar.add(equations[i][1])
        
        def dfs(start, end, visited):
            if (start, end) in paird:
                return paird[(start, end)]
            
            for var in allvar: ## following loop is checking for all var which can fall in indirect relationship between start and end value of given queries. It adds the "var" in the visited list so that search does not fall into infinite loop. Later it removes the "var" from visited to try for other queries
                if (start, var) in paird and var not in visited:
                    visited.add(var)
                    tmp = dfs(var, end, visited)
                    if tmp != -1:
                        return paird[(start, var)] * tmp
                    visited.remove(var)
            return -1
        
        ans_list = []
        for query in queries:
            if query[0] not in allvar or query[1] not in allvar:
                ans_list.append(-1.0)
            elif query[0] == query[1]:
                ans_list.append(1.0)
            else:
                result = dfs(query[0], query[1], set())
                ans_list.append(result)
        
        return ans_list
