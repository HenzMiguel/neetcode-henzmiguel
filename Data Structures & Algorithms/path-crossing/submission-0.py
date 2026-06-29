class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coords = [0,0]

        locations = {tuple(coords)}
        for char in path:
            match char:
                case 'N':
                    coords[0]+=1
                case 'S':
                    coords[0] -=1
                case 'E':
                    coords[1]+=1
                case 'W':
                    coords[1]-=1
            
            if tuple(coords) in locations:
                return True
            else:
                locations.add(tuple(coords))
        return False