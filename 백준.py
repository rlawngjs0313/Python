import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    execute = list(map(str, sys.stdin.readline().split()))
    cube = [[["g", "g", "g"] for _ in range(3)], 
            [["r", 'r', 'r'] for _ in range(3)], 
            [['b', 'b', 'b'] for _ in range(3)], 
            [['o', 'o', 'o'] for _ in range(3)], 
            [['w', 'w', 'w'] for _ in range(3)], 
            [['y', 'y', 'y'] for _ in range(3)]]
    for i in execute:
        if i == "U-":
            cube[0][0][:], cube[1][0][:], cube[2][0][:], cube[3][0][:] = cube[3][0][:], cube[0][0][:], cube[1][0][:], cube[2][0][:]
            cube[4][0][0], cube[4][0][1], cube[4][0][2], cube[4][1][0], cube[4][1][2], cube[4][2][0], cube[4][2][1], cube[4][2][2] = cube[4][0][2], cube[4][1][2], cube[4][2][2], cube[4][0][1], cube[4][2][1], cube[4][0][0], cube[4][1][0], cube[4][2][0]
        elif i == "U+":
            cube[0][0][:], cube[1][0][:], cube[2][0][:], cube[3][0][:] = cube[1][0][:], cube[2][0][:], cube[3][0][:], cube[0][0][:]
            cube[4][0][0], cube[4][0][1], cube[4][0][2], cube[4][1][0], cube[4][1][2], cube[4][2][0], cube[4][2][1], cube[4][2][2] = cube[4][2][0], cube[4][1][0], cube[4][0][0], cube[4][2][1], cube[4][0][1], cube[4][2][2], cube[4][1][2], cube[4][0][2]
        elif i == "D-":
            cube[0][2][:], cube[1][2][:], cube[2][2][:], cube[3][2][:] = cube[1][2][:], cube[2][2][:], cube[3][2][:], cube[0][2][:]
            cube[5][0][0], cube[5][0][1], cube[5][0][2], cube[5][1][0], cube[5][1][2], cube[5][2][0], cube[5][2][1], cube[5][2][2] = cube[5][0][2], cube[5][1][2], cube[5][2][2], cube[5][0][1], cube[5][2][1], cube[5][0][0], cube[5][1][0], cube[5][2][0]
        elif i == "D+":
            cube[0][2][:], cube[1][2][:], cube[2][2][:], cube[3][2][:] = cube[3][2][:], cube[0][2][:], cube[1][2][:], cube[2][2][:]
            cube[5][0][0], cube[5][0][1], cube[5][0][2], cube[5][1][0], cube[5][1][2], cube[5][2][0], cube[5][2][1], cube[5][2][2] = cube[5][2][0], cube[5][1][0], cube[5][0][0], cube[5][2][1], cube[5][0][1], cube[5][2][2], cube[5][1][2], cube[5][0][2]
        elif i == "F-":
            cube[0][0][2], cube[0][1][2], cube[0][2][2], cube[5][0][0], cube[5][0][1], cube[5][0][2], cube[2][0][0], cube[2][1][0], cube[2][2][0], cube[4][2][0], cube[4][2][1], cube[4][2][2] = cube[4][2][2], cube[4][2][1], cube[4][2][0], cube[0][0][2], cube[0][1][2], cube[0][2][2], cube[5][0][2], cube[5][0][1], cube[5][0][0], cube[2][0][0], cube[2][1][0], cube[2][2][0]
            cube[1][0][0], cube[1][0][1], cube[1][0][2], cube[1][1][0], cube[1][1][2], cube[1][2][0], cube[1][2][1], cube[1][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2], cube[1][0][1], cube[1][2][1], cube[1][0][0], cube[1][1][0], cube[1][2][0]
        elif i == "F+":
            cube[0][0][2], cube[0][1][2], cube[0][2][2], cube[4][2][0], cube[4][2][1], cube[4][2][2],  cube[2][0][0], cube[2][1][0], cube[2][2][0], cube[5][0][0], cube[5][0][1], cube[5][0][2] = cube[5][0][0], cube[5][0][1], cube[5][0][2], cube[0][2][2], cube[0][1][2], cube[0][0][2], cube[4][2][0], cube[4][2][1], cube[4][2][2], cube[2][2][0], cube[2][1][0], cube[2][0][0]
            cube[1][0][0], cube[1][0][1], cube[1][0][2], cube[1][1][0], cube[1][1][2], cube[1][2][0], cube[1][2][1], cube[1][2][2] = cube[1][2][0], cube[1][1][0], cube[1][0][0], cube[1][2][1], cube[1][0][1], cube[1][2][2], cube[1][1][2], cube[1][0][2]
        elif i == "B-":
            cube[0][0][0], cube[0][1][0], cube[0][2][0], cube[4][0][0], cube[4][0][1], cube[4][0][2], cube[2][0][2], cube[2][1][2], cube[2][2][2], cube[5][2][0], cube[5][2][1], cube[5][2][2] = cube[5][2][0], cube[5][2][1], cube[5][2][2], cube[0][2][0], cube[0][1][0], cube[0][0][0], cube[4][0][0], cube[4][0][1], cube[4][0][2], cube[2][2][2], cube[2][1][2], cube[2][0][2]
            cube[3][0][0], cube[3][0][1], cube[3][0][2], cube[3][1][0], cube[3][1][2], cube[3][2][0], cube[3][2][1], cube[3][2][2] = cube[3][0][2], cube[3][1][2], cube[3][2][2], cube[3][0][1], cube[3][2][1], cube[3][0][0], cube[3][1][0], cube[3][2][0]
        elif i == "B+":
            cube[0][0][0], cube[0][1][0], cube[0][2][0], cube[5][2][0], cube[5][2][1], cube[5][2][2], cube[2][0][2], cube[2][1][2], cube[2][2][2], cube[4][0][0], cube[4][0][1], cube[4][0][2] = cube[4][0][2], cube[4][0][1], cube[4][0][0], cube[0][0][0], cube[0][1][0], cube[0][2][0], cube[5][2][2], cube[5][2][1], cube[5][2][0], cube[2][0][2], cube[2][1][2], cube[2][2][2]
            cube[3][0][0], cube[3][0][1], cube[3][0][2], cube[3][1][0], cube[3][1][2], cube[3][2][0], cube[3][2][1], cube[3][2][2] = cube[3][2][0], cube[3][1][0], cube[3][0][0], cube[3][2][1], cube[3][0][1], cube[3][2][2], cube[3][1][2], cube[3][0][2]
        elif i == "L-":
            cube[1][0][0], cube[1][1][0], cube[1][2][0], cube[3][0][2], cube[3][1][2], cube[3][2][2], cube[4][0][0], cube[4][1][0], cube[4][2][0], cube[5][0][0], cube[5][1][0], cube[5][2][0] = cube[5][0][0], cube[5][1][0], cube[5][2][0], cube[4][2][0], cube[4][1][0], cube[4][0][0], cube[1][0][0], cube[1][1][0], cube[1][2][0], cube[3][2][2], cube[3][1][2], cube[3][0][2]
            cube[0][0][0], cube[0][0][1], cube[0][0][2], cube[0][1][0], cube[0][1][2], cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[0][0][2], cube[0][1][2], cube[0][2][2], cube[0][0][1], cube[0][2][1], cube[0][0][0], cube[0][1][0], cube[0][2][0]
        elif i == "L+":
            cube[1][0][0], cube[1][1][0], cube[1][2][0], cube[4][0][0], cube[4][1][0], cube[4][2][0], cube[5][0][0], cube[5][1][0], cube[5][2][0], cube[3][0][2], cube[3][1][2], cube[3][2][2] = cube[4][0][0], cube[4][1][0], cube[4][2][0], cube[3][2][2], cube[3][1][2], cube[3][0][2], cube[1][0][0], cube[1][1][0], cube[1][2][0], cube[5][2][0], cube[5][1][0], cube[5][0][0]
            cube[0][0][0], cube[0][0][1], cube[0][0][2], cube[0][1][0], cube[0][1][2], cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[0][2][0], cube[0][1][0], cube[0][0][0], cube[0][2][1], cube[0][0][1], cube[0][2][2], cube[0][1][2], cube[0][0][2]
        elif i == "R-": 
            cube[1][0][2], cube[1][1][2], cube[1][2][2], cube[3][0][0], cube[3][1][0], cube[3][2][0], cube[4][0][2], cube[4][1][2], cube[4][2][2], cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[4][0][2], cube[4][1][2], cube[4][2][2], cube[5][2][2], cube[5][1][2], cube[5][0][2], cube[3][2][0], cube[3][1][0], cube[3][0][0], cube[1][0][2], cube[1][1][2], cube[1][2][2]
            cube[2][0][0], cube[2][0][1], cube[2][0][2], cube[2][1][0], cube[2][1][2], cube[2][2][0], cube[2][2][1], cube[2][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2], cube[2][0][1], cube[2][2][1], cube[2][0][0], cube[2][1][0], cube[2][2][0]
        elif i == "R+":
            cube[1][0][2], cube[1][1][2], cube[1][2][2], cube[3][0][0], cube[3][1][0], cube[3][2][0], cube[4][0][2], cube[4][1][2], cube[4][2][2], cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[5][0][2], cube[5][1][2], cube[5][2][2], cube[4][2][2], cube[4][1][2], cube[4][0][2], cube[1][0][2], cube[1][1][2], cube[1][2][2], cube[3][2][0], cube[3][1][0], cube[3][0][0]
            cube[2][0][0], cube[2][0][1], cube[2][0][2], cube[2][1][0], cube[2][1][2], cube[2][2][0], cube[2][2][1], cube[2][2][2] = cube[2][2][0], cube[2][1][0], cube[2][0][0], cube[2][2][1], cube[2][0][1], cube[2][2][2], cube[2][1][2], cube[2][0][2]
    print(str(cube[4]).replace("[", "").replace("'", "").replace("], ", "\n").replace("]", "").replace(", ", ""))