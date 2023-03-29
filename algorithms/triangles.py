# description  https://py.checkio.org/en/mission/similar-triangles/



from typing import List, Tuple
import math
Coordss = List[Tuple[int, int]]
def sides_prop(coords : Coordss):
    a = math.sqrt(math.pow(coords[1][0]-coords[0][0], 2) + math.pow(coords[1][1]-coords[0][1], 2))
    b = math.sqrt(math.pow(coords[2][0]-coords[1][0], 2) + math.pow(coords[2][1]-coords[1][1], 2))
    c = math.sqrt(math.pow(coords[0][0]-coords[2][0], 2) + math.pow(coords[0][1]-coords[2][1], 2))
    ab, ba = a/b, b/a
    bc, cb = b/c, c/b
    ca, ac = c/a, a/c
    
    return [ab, bc, ca, ba, cb, ac]
    
def similar_triangles(coords_1: Coordss, coords_2: Coordss) -> bool:
    return sum(1 if prop in  sides_prop(coords_2) else 0 for prop in sides_prop(coords_1)) >=3