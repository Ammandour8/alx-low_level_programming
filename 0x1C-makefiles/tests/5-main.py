#!/usr/bin/python3
"""
5-main
"""
island_perimeter = __import__('5-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
<<<<<<< HEAD
     ]
print(island_perimeter(grid))
=======
    ]
    print(len(grid))
    print(island_perimeter(grid))
>>>>>>> 50dbb2b1d625d6106cf023b66f4fa876fadf6b6d
