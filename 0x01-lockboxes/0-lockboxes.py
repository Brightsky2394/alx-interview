#!/usr/bin/python3

from collections import deque


def canUnlockAll(boxes):
    if not boxes:
        return False

    n = len(boxes)
    visited = set()
    queue = deque([0])
    visited.add(0)

    while queue:
        current_box = queue.popleft()

        for key in boxes[current_box]:
            if key not in visited and key < n:
                visited.add(key)
                queue.append(key)

    return len(visited) == n
