# 3D Surface Area https://www.hackerrank.com/challenges/3d-surface-area/problem

def surfaceArea(A):
    area = 2 * H * W

    #check the limit
    def check(i, j):
        return A[x+i][y+j] if 0 <= x + i < H and 0 <= y + j < W else 0

    xi = [0, 0, 1, -1]
    yi = [1, -1, 0, 0]

    for x in range(H):
        for y in range(W):
            for i, j in zip(xi, yi):
                area += max(0, A[x][y] - check(i, j)) 


    return area               