# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    coins = [0] * n
    cnt = 0
    for i in range(n):
        coins[i] = int(input())
    for coin in coins[::-1]:
        cnt += k // coin
        k %= coin
    print(cnt)

if __name__ == "__main__":
    main()