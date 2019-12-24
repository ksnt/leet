class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start < destination:
            path1 = distance[start:destination]
        else:
            path1 = distance[destination:start]
        for p in path1:
            distance.remove(p)
        return min(sum(path1),sum(distance))