# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157
# 한마디: Counter 클래스같은게 존재하다니

import sys
input = sys.stdin.readline

word = input().upper.strip()
cnt_dic = {}

for w in word: # w: 알파벳 자체를 받아옴
    if w not in cnt_dic:
        cnt_dic[w] = 0
    if w in cnt_dic:
        cnt_dic[w] += 1
# Counter 클래스를 사용하면 빈도수를 그냥 딕셔너리로 반환 (위 반복문 한 줄 축약)
# word_cnt = Counter(word)

max_value = max(cnt_dic.values())
max = [k for k, v in cnt_dic.items() if max_value == v]

if len(max) == 1:
    print(max[0])
else:
    print("?")


