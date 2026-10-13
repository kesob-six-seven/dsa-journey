"""Day 97 — NeetCode 150: Graphs
Course Schedule (LC 207) — Medium
Course Schedule II (LC 210) — Medium
"""
from collections import defaultdict
from typing import List


class SolutionCourseSchedule:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        DFS with visiting state:
        Track visited nodes along the current DFS recursion path to detect cycles.
        If a course is already completed, clear its prerequisites to optimize re-checks.
        """
        pre_map = defaultdict(list)
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visit = set()

        def dfs(crs: int) -> bool:
            if crs in visit:
                return False
            if pre_map[crs] == []:
                return True

            visit.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            pre_map[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True


class SolutionCourseScheduleII:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        DFS with 3-state Cycle Detection:
        - cycle: currently in DFS stack (back-edge detected -> cycle exists)
        - visit: fully processed and safe
        Append node to output after visiting all prerequisites (post-order DFS).
        """
        pre_map = defaultdict(list)
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        output = []
        visit = set()
        cycle = set()

        def dfs(crs: int) -> bool:
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return output