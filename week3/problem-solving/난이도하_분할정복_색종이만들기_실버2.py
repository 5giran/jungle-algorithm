# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = [0, 0]  # result[0] = white, result[1] = blue

    def check(x, y, size):
        """이 구역을 더 나눌 필요가 없는가? → 문제마다 이 부분만 바꾸면 됨"""
        base = matrix[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if matrix[i][j] != base:
                    return None  # 다르면 → 계속 나눠야 함
        return base  # 같으면 → 멈춰도 됨

    def divide(x, y, size):
        """나누기 뼈대 → 거의 모든 2D 분할정복 문제에서 동일"""
        val = check(x, y, size)
        if val is not None:       # 멈출 조건 충족
            result[val] += 1      # ← 결과 처리도 문제마다 바꾸는 부분
            return # divide 호출 중 이번호출 하나만 종료

        half = size // 2
        divide(x,        y,        half)
        divide(x,        y + half, half)
        divide(x + half, y,        half)
        divide(x + half, y + half, half)

    divide(0, 0, N)
    print(result[0])
    print(result[1])

if __name__ == "__main__":
    main()