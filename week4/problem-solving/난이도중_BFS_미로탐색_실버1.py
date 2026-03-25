# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178

from collections import deque

import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    visited = [[False] * M for _ in range(N)] # 방문배열은 False로 기본값 설정해둬야함
    grid = [list(map(int, input().strip())) for _ in range(N)]

    def bfs():
        # BFS: 큐에 시작점 넣고 시작
        queue = deque([(0, 0)])
        visited[0][0] = True
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue: # 아직 탐색 안한 좌표가 있다면
            row, col = queue.popleft() # 가장 가까운 칸부터 = 너비우선
            for dr, dc in dir:
                nr, nc = row + dr, col + dc

                if nr < 0 or nr >= N or nc < 0 or nc >= M: continue # 그리드 범위 벗어났을 경우
                if grid[nr][nc] == 1 and not visited[nr][nc]: 
                    visited[nr][nc] = True
                    grid[nr][nc] = grid[row][col] + 1 # 현재 거리 = 이전 칸 거리 + 1로 덮어쓰기
                    queue.append((nr, nc)) # 다음 탐색 칸 큐에 넣기

    bfs()
    print(grid[N - 1][M - 1]) # 그리드에 거리를 덮어쓰기해서 도착점 값이 곧 최단 칸 수
    # bfs는 도착점에 처음 도착했을 때가 무조건 최단거리

if __name__ == "__main__":
    main()