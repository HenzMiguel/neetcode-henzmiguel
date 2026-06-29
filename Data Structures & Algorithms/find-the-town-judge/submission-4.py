class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        h = {}
        j = {}

        ever = {n for n in range(1, n + 1)}
        
        for conn in trust:
            h[conn[1]] = h.get(conn[1], [])
            h[conn[1]].append(conn[0])
        
        for conn in trust:
            j[conn[0]] = j.get(conn[0], [])
            j[conn[0]].append(conn[1])

        # Every one likes him
        for key, value in h.items():
            if len(ever - set(value)) == 1 and key not in j:
                return key

        return -1   
        