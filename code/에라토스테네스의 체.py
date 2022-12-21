# 1 ~ num 까지 소수 여부 판별

num = 100
prime = [True for _ in range(num+1)]  # index number == 자연수
prime[0] = False  # 0과 1은 소수가 아니기 때문에 False
prime[1] = False

for i in range(2, int(num**0.5)+1): # 중복 방지하기 위해 √num까지 반복
    for j in range(i*i, num+1, i):  # i의 배수로 반복 (자기 자신은 제외하기 위해 i*i부터 시작)
        if prime[j]:
            prime[j] = False
