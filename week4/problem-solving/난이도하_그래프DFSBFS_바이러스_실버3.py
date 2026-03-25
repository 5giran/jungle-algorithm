# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

def main():
    n = int(input())
    e = int(input())

    network = [[] for _ in range(n+1)]
    for _ in range(e):
        u, v = map(int, input().split())
        network[u].append(v)
        network[v].append(u)

    visited = [False] * (n+1)
    visited[1] = True # 최초 노드는 명시적으로 방문처리하고 시작
    def dfs(node):
        for next_node in network[node]:
            if not visited[next_node]:
                visited[next_node] = True
                dfs(next_node)

    dfs(1) # 1번 컴퓨터가 웜 바이러스에 걸렸을때
    result = visited.count(True) - 1 # 시작 노드는 제외해야 하기 때문
    print(result)

if __name__ == "__main__":
    main()