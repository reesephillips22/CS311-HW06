"""
Homework 6: The Prerequisite Planner -- starter.

Complete has_cycle and topological_sort below. See
Homework 6 The Prerequisite Planner.md, Part B, for the full requirements.
"""

from typing import Dict, List, Optional


def has_cycle(graph: Dict[str, List[str]]) -> bool:
    """
    Recursive DFS. Track both a permanent "visited" set and a
    temporary "on the current recursion path" set to detect back
    edges (Part A, Question 4). Must work across disconnected
    components.
    """
    # TODO
    visited = set()
    on_path = set()

    def dfs(course: str) -> bool:
        # Mark this course as visited and add it to the current path
        visited.add(course)
        on_path.add(course)

        # Check every course that depends on this prerequisite
        for neighbor in graph.get(course, []):
            # A neighbor on the current path means there is a cycle
            if neighbor in on_path:
                return True

            # Visit neighbors that have not been visited yet
            if neighbor not in visited:
                if dfs(neighbor):
                    return True

        # Remove the course when its recursive call finishes
        on_path.remove(course)
        return False

    # Start DFS from every unvisited course (including disconnected ones)
    for course in graph:
        if course not in visited:
            if dfs(course):
                return True

    return False


def topological_sort(graph: Dict[str, List[str]]) -> Optional[List[str]]:
    """
    Return a valid topological order via DFS finish-time ordering
    (Part A, Questions 2-3), or None if the graph contains a cycle.
    """
    # TODO
    if has_cycle(graph):
        return None

    visited = set()
    finish_order = []

    def dfs(course: str) -> None:
        
        visited.add(course)

      
        for neighbor in graph.get(course, []):
            if neighbor not in visited:
                dfs(neighbor)

        finish_order.append(course)

    for course in graph:
        if course not in visited:
            dfs(course)

    finish_order.reverse()
    return finish_order
