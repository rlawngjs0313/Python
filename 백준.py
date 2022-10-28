import sys
import numpy as np


T = int(sys.stdin.readline())

for i in range(T):
    U_D = [["w", "w", "w"] for _ in range(3)]
    D_U = [["y", "y", "y"] for _ in range(3)]
    F_B = [["r", "r", "r"] for _ in range(3)]
    B_F = [["o", "o", "o"] for _ in range(3)]
    L_R = [["g", "g", "g"] for _ in range(3)]
    R_L = [["b", "b", "b"] for _ in range(3)]

    n = int(sys.stdin.readline())
    execution = list(map(str, sys.stdin.readline().split()))
    for j in execution:
        if j == "U-":
            F_B[0][:], R_L[0][:], B_F[0][:], L_R[0][:], U_D[:][:
                                                               ] = L_R[0][:], F_B[0][:], R_L[0][:], B_F[0][:]
        elif j == "U+":
            F_B[0][:], L_R[0][:], B_F[0][:], R_L[0][:] = R_L[0][:], B_F[0][:], L_R[0][:], F_B[0][:]
        elif j == "D-":
            F_B[2][:], R_L[2][:], B_F[2][:], L_R[2][:] = L_R[2][:], F_B[2][:], R_L[2][:], B_F[2][:]
        elif j == "D+":
            F_B[2][:], L_R[2][:], B_F[2][:], R_L[2][:] = R_L[2][:], B_F[2][:], L_R[2][:], F_B[2][:]
