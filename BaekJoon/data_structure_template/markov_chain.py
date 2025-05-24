import numpy as np
import string
import random
# 상태(state) 정의
states = ['k', 'n', 'e', 'x','E']
lower=list(string.ascii_lowercase)
upper=list(string.ascii_uppercase)
digit=list(string.digits)
special=list(string.punctuation)
# 상태 전이 확률 행렬 (4x4)
transition_matrix = np.array([
    [0.1, 0.4, 0.2, 0.1,0.2],  # S0 -> [S0, S1, S2, S3]
    [0.3, 0.3, 0.2, 0.1,0.1],  # S1 -> ...
    [0.3, 0.2, 0.3, 0.1,0.1],  
    [0.25, 0.20, 0.25, 0.20, 0.1],
    [0.5, 0.1, 0.2, 0.1,0.1]
])

# 초기 상태
current_state = 2# S2

# 마르코프 체인 시뮬레이션 함수
def markov_chain(transition_matrix, current_state, steps):
    states_visited = [states[current_state]]
    for _ in range(steps):
        current_state = np.random.choice(
            [0, 1, 2, 3,4], 
            p=transition_matrix[current_state]
        )
        states_visited.append(states[current_state])
    return states_visited

# 예: 10단계 시뮬레이션
result = markov_chain(transition_matrix, current_state, 10)
password=""
print(result)
for i in result:
    print(i)
    if i =="e":
        password+=(random.choice(lower))
    if i =="x":
        password+=(random.choice(special))
    if i =="E":
        password+=(random.choice(upper))
    if i =="k":
        password+=(random.choice(lower))
    if i =="n":
        password+=(random.choice(digit))
print("마르코프 체인 경로:", ' -> '.join(password))
