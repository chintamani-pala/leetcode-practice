class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        frequency = {}
        for move in moves:
            frequency[move] = frequency.get(move, 0)+1
        return abs(frequency.get("R", 0) - frequency.get("L", 0))+frequency.get("_", 0)