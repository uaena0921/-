# 코드 11.16: Floyd 알고리즘
INF = 9999
def printA(A):
    vsize = len(A)
    print("====================================")
    for i in range(vsize) :
        for j in range(vsize) :
            if (A[i][j] == INF) :
                print(" INF ", end='')
            else :
                print("%4d "%A[i][j], end='')
        print("");






def shortest_path_floyd(vertex, adj):
    vsize = len(vertex)
    A = list(adj)
    path = [[None for _ in range(vsize)] for _ in range(vsize)]

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    path[i][j] = k  # 경로 저장

    def print_path(start, end):
        if path[start][end] is None:
            print(f"{vertex[start]} -> {vertex[end]}")
        else:
            print_path(start, path[start][end])
            print(f"{vertex[path[start][end]]} -> {vertex[end]}")

    s_vtx = input("Start Vertex: ")
    e_vtx = input("End Vertex: ")

    start = vertex.index(s_vtx)
    end = vertex.index(e_vtx)

    print(f"Shortest Path")
    print_path(start, end)
    print(f"Distance of the Shortest Path: {A[start][end]}")

        
if __name__ == "__main__":
    
    vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
    weight = [
               [0,	    7,		INF,	INF,	3,      10,		INF],
               [7,		0,	    4,		10,	    2,	    6,	    INF],
               [INF,	4,		0,	    2,		INF,	INF,	INF],
               [INF,	10,     2,		0,      11,		9,	    4   ],
               [3,	    2,	    INF,   11,		0,      13,		5   ],
               [10,		6,	    INF,	9,      13,		0,	    INF],
               [INF,    INF,	INF,   4,		5,		INF,	0   ]]
    
    while(1):
        command = input("시작- s, 종료-q : ")
        if command == 's':
            shortest_path_floyd(vertex, weight)
        elif command == 'q'  : quit()















