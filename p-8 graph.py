def DFS(vtx, adj, s, visited) :
    print(vtx[s], end=' ')          # 현재 정점 s를 출력함
    visited[s] = True               # 현재 정점 s를 visited에 추가함
    for v in range(len(vtx)) :      # 인접행렬
        if adj[s][v] != 0 :         # 모든 간선 (s,v)에 대해
            if visited[v]==False:   # v를 아직 방문하지 않았으면 
                DFS(vtx, adj, v, visited)
from queue import Queue                 # queue 모듈의 Queue 사용


def BFS_AL(vtx, adj, s):
    n = len(vtx)                                # 그래프의 정점 수
    visited = [False]*n                     # 방문 확인을 위한 리스트
    Q = Queue()                         # 공백상태의 큐 생성
    Q.put(s)                            # 맨 처음에는 시작 정점만 있음
    visited[s] = True                   # s는 "방문"했다고 표시
    while not Q.empty() :
        s = Q.get()                     # 큐에서 정점을 꺼냄
        print(vtx[s], end=' ')          # 정점을 출력(처리)함
        for v in range(len(vtx)):
            if adj[s][v] != 0 and not visited[v]:
                Q.put(v)
                visited[v] = True



        
def create_graph(vertices, edges):
    
    graph = {}
    for vertex in vertices:
        graph[vertex] = []
        
    for edge in edges:
        u, v = edge.split('-')
        graph[u].append(v)
        graph[v].append(u)  

    return graph





def create_matrix(vertices, edges):
  num_vertices = len(vertices)
  adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
  # 정점 이름과 인덱스를 매핑하는 딕셔너리 생성
  vertex_index = {vertex: index for index, vertex in enumerate(vertices)}
  # 간선 정보를 이용하여 인접 행렬에 1 설정
  for edge in edges:
    u, v = edge.split('-')
    row = vertex_index[u]
    col = vertex_index[v]
    adjacency_matrix[row][col] = 1
    adjacency_matrix[col][row] = 1  # 무방향 그래프인 경우 양방향으로 설정
  return adjacency_matrix




def find_connected_component(vtx, adj) :
    n = len(vtx)
    visited = [False]*n
    groups = []		# 부분 그래프별 정점 리스트

    for v in range(n) :
        if visited[v] == False :
            color = bfs_cc(vtx, adj, v, visited)
            groups.append( color )

    return groups

# 코드 10.8: 너비우선탐색을 이용한 연결성분 검사
from queue import Queue
def bfs_cc(vtx, adj, s, visited):
    group = [s]    # 새로운 연결된 그룹 생성
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty() :
        s = Q.get()
        for v in range(len(vtx)) :
            if visited[v]==False and adj[s][v] != 0 :
                Q.put(v)
                visited[v] = True
                group.append(v)
    return group


def dfs_spanning_tree(graph, start, visited, parent, spanning_tree):
    visited[start] = True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            spanning_tree.append((start, neighbor))
            dfs_spanning_tree(graph, neighbor, visited, start, spanning_tree)

def find_spanning_tree(graph, start):
    start = vertex_index[start_vertex]
    visited = [False] * len(graph)
    parent = [-1] * len(graph)
    spanning_tree = []
    dfs_spanning_tree(graph, start, visited, -1, spanning_tree)
    return spanning_tree



# 코드 10.10: 깊이우선탐색을 이용한 신장트리
def ST_DFS(vtx, adj, s, visited) :
    visited[s] = True               # 현재 정점 s를 visited에 추가함
    for v in range(len(vtx)) :      # 인접행렬
        if adj[s][v] != 0 :         # 모든 간선 (s,v)에 대해
            if visited[v]==False:   # v를 아직 방문하지 않았으면 
                print("(", vtx[s], vtx[v], ")", end=' ')  # 간선 출력
                ST_DFS(vtx, adj, v, visited)


start_cnt = 0

while True :
    command = input("[메뉴선택] i-입력, m-매크로, l-리스트 출력, d- DFS, b-BFS,c-연결성분, s-신장트리,  q-종료=> ")

    if command == 'i' :
        vertices = input("vertex : ").split(', ')
        edges = input("edge : ").split(', ')

    elif command == 'q' : exit()
        
    elif command == 'm':
        vertices = "A, B, C, D, E, F, G, H".split(', ')
        edges = "A-B, A-C, B-D, C-D, C-E, D-F, E-H, E-G, G-H".split(', ')

    elif command == 'l':
        vertex_index = {}
        index = 0
        for vertex in vertices:
            vertex_index[vertex] = index
            index += 1  

        visited = [False] * len(vertices)

        graph = create_graph(vertices, edges)
        print("adjacent vertex 리스트")
        for vertex, neighbors in graph.items():
            print(f"{vertex}: {neighbors}")

        start_cnt = 1

    elif command == 'd':
        if start_cnt == 1:
            print("DFS : ", end='')
            DFS(vertices,create_matrix(vertices, edges), vertex_index[vertices[0]], visited)
            print(end='\n')

        else:
            print("I를 먼저 입력하세요")


    elif command == 'b':
        if start_cnt == 1:
            print("BFS : ", end='')
            BFS_AL(vertices, create_matrix(vertices, edges), 0)
            print(end='\n')
        else:
            print("I를 먼저 입력하세요")

    elif command == 'c':
        if start_cnt == 1:
            colorGroup = find_connected_component(vertices, create_matrix(vertices, edges))
            print("연결성분 개수 = %d " % len(colorGroup))
            print(colorGroup)
        else:
            print("I를 먼저 입력하세요")

            
    elif command == 's':
        if start_cnt == 1:
            print('신장트리(DFS): ', end="")
            ST_DFS(vertices, create_matrix(vertices, edges), 0, [False]*len(vertices))
            print()
        else:
            print("I를 먼저 입력하세요")

    else :
        print("없는 커맨드입니다")
    print("==========================================")
              







               
