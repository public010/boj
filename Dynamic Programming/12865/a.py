# 12865 평범한 배낭

"""
입력
첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다.
두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
입력으로 주어지는 모든 수는 정수이다.

출력
한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

예제입력 1
4 7
6 13
4 8
3 6
5 12

예제 출력 1 
14
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stuffs = []
prev_knapsack = [0] * (K + 1)

for _ in range(N):
    stuffs.append(tuple(map(int, input().split())))

stuffsCount = len(stuffs)

for row in range(1, N + 1):
    cur_knapsack = [0] * (K + 1)
    for column in range(1, K + 1):
        if stuffs[row - 1][0] <= column:
            cur_knapsack[column] = max(prev_knapsack[column],\
                                            prev_knapsack[column - stuffs[row - 1][0]] +\
                                                stuffs[row - 1][1])
        else:
            cur_knapsack[column] = prev_knapsack[column]
    prev_knapsack = cur_knapsack
            
print(prev_knapsack[K])