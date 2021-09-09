






# <문제> 시각


# 1. 문제 설명
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성해라
# 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각이 됨
#    00시 00분 03초
#    00시 13분 30초
# 반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 시각임
#    00시 02분 55초
#    01시 27분 45초  




# 2. 문제 조건
# 난이도 1, 풀이시간 15분, 시간제한 2초, 메모리 제한 128MB
# 입력 조건: 첫째 줄에 정수 N이 입력 (0<=N<=23)
# 출력 조건: 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는
#           모든 경우의 수를 출력




# 내가 짜본 코드  

n = int(input())
eh, em, es = n, 59, 59
count = 0

for h in range(eh+1):
     for m in range(em+1):
         for s in range(es+1):
             if '3' in str(s) or '3' in str(m) or '3' in str(h): 
                 count += 1

print(count)                 




# 3. 문제 해결 아이디어
# 이 문제는 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제
# 하루는 86400초 이므로, 00시 00분 00초부터 23시 59분 59초까지의 모든 경우는 86400가지임
#   24 x 60 x 60 = 86400
# 따라서 단순히 시각을 1씩 증가시키면서 3이 하나라도 포함되어 있는지를 확인하면 됨
# 이러한 유형은 완전 탐색 문제 유형이라고 불림
#   완전 탐색 -> 가능한 경우의 수를 모두 검사해보는 탐색 방법을 의미  





# 4. 답안 예시  

# H 입력 받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
print(count)                







