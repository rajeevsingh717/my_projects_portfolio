"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap={i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        

        visitset=set() ## all courses along the curr DFS path
        def dfs(crs):
            if crs in visitset: ## if the course is already visisted then return False
                return False
            if premap[crs]==[]: ## if the course does not have any prereqisite then return True
                return True

            visitset.add(crs)
            for pre in premap[crs]: ## run the loop through the prerequisite
                if not dfs(pre): return False ## if any of the function call return False then return False, No need to look further

            visitset.remove(crs) ## if above does not return False then all prerequisite courses can be taken, then remove the current course from visitset
            premap[crs]=[] ## set the prerequisite of this course in the map to blank list [] so that it will return true if the course appears again next time
            return True

        for crs in range(numCourses): ## need to call the dfs function for all the course
            if not dfs(crs):return False ## if any call return False then return overall False
        
        return True
