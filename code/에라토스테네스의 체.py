# 1 ~ n 까지 소수 구하기

n = 100
check = [False, False] + [True for _ in range(n-1)]  # index number == 자연수
prime = []  # 소수

for i in range(2, n+1):
    if check[i]:
        prime.append(i)
        for j in range(i*2, n+1, i):  # i의 배수로 반복 (자기 자신은 제외하기 위해 i*i부터 시작)
            check[j] = False
