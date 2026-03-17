# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    words = [input().strip() for _ in range(N)]

    for word in words:
        re_word = word[::-1]
        if re_word in words:
            length = len(word)
            mid = length // 2
            print(f"{length} {word[mid]}")
            return

if __name__ == "__main__":
    main()