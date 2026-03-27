# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    def fib(n, memo=None):
        # 처음 호출이냐(None)만 확인하고 싶을 때: memo is None
        # 비어있거나 없을때(None, [], {}, "", 0)를 전부 처리하고 싶을 때: not memo
        if memo is None:
            memo = {}
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            memo[n] = fib(n-1, memo) + fib(n-2, memo)

        return memo[n]
    
    print(fib(n))
    
if __name__ == "__main__":
    main()