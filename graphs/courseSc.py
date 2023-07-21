class Solution(object):
    def canFinish(self, numCourses, prerequisites):
            graph = defaultdict(list)

            for pair in prerequisites:
                course, pre = pair
                graph[course].append(pre)

            visit = [0]*numCourses

            def hasCycle(course):
                if visit[course] == 1: return True
                if visit[course] == 2: return False

                visit[course] = 1
                for pre in graph[course]:
                    if hasCycle(pre):
                        return True 

                visit[course] = 2
                return False 



            for course in range(numCourses):
                if hasCycle(course):
                    return False
            return True