description - https://py.checkio.org/en/mission/inside-block/


from typing import Tuple
import numpy as np

def solve (i1, j1, k1, i2, j2, k2):            # to solve linear equation using matrix
    matrix_a = [[i1, j1], [i2, j2]]
    matrix_b = [k1, k2]
    return np.linalg.solve(matrix_a, matrix_b)    

def is_inside(polygon: Tuple[Tuple[int, int], ...], point: Tuple[int, int]) -> bool:
    a_int = 5
    b_int = point[1] - a_int * point[0]                                                       # lets say that a=2 for intersection line always 
    cuts = 0
    for [x1, y1], [x2, y2] in [[polygon[0-i], polygon[-1-i]] for i in range(len(polygon))]:     #list compr generate pairs of points of sides     
        try:
            a,b = solve(x1, 1, y1, x2, 1, y2)               # what is a and b for "side" line
            x, y = solve(a_int, -1, -b_int, a, -1, -b)      # intersection point of side and line crossing point
        except Exception as e:
            x, y= x1, a_int * x1 + b_int
            if (y1 <= y <= y2) and y >= point[1]:
                cuts += 1
            continue             
        con1 = ((y1 <= int(y) <= y2) or (y1 >= int(y) >= y2)) and ((x1 <= x <= x2) or (x1 >= x >= x2))
        if con1 and point[1]==a*point[0] + b:
            return True
        if con1 and y >= point[1]:                                    # does point is in side length            
            cuts += 1
    return False if cuts%2 == 0  else True