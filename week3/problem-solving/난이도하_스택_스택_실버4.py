# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

from collections import deque

import sys
input = sys.stdin.readline

def main():
    n = int(input())
    stack = deque()
    for _ in range(n):
        line = input().split()
        com = line[0]

        if com == "push":
            i = int(line[1])
            stack.append(i)

        elif com == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)

        elif com == "size":
            print(len(stack))

        elif com == "empty":
            if stack:
                print(0)
            else:
                print(1)

        elif com == "top":
            if stack:
                print(stack[-1]) # stack 리스트 마지막 요소 출력
            else:
                print(-1)

if __name__ == "__main__":
    main()