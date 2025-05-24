import numpy as np
import string
import random

# 상태 정의
states = ['k', 'n', 'e', 'x', 'E']
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
digit = list(string.digits)
special = list(string.punctuation)

# 상위 상태 전이 확률 행렬 (5x5)
state_transition = np.array([
    [0.1, 0.4, 0.2, 0.1, 0.2],
    [0.3, 0.3, 0.2, 0.1, 0.1],
    [0.3, 0.2, 0.3, 0.1, 0.1],
    [0.25, 0.20, 0.25, 0.20, 0.1],
    [0.5, 0.1, 0.2, 0.1, 0.1]
])

# 마르코프 전이 행렬 생성기 (동일 확률로 다음 글자 선택)
def create_markov_matrix(size):
    mat = np.array([np.random.dirichlet(np.ones(size)) for _ in range(size)])
    return mat

# 하위 전이 행렬
lower_transition = create_markov_matrix(len(lower))
upper_transition = create_markov_matrix(len(upper))
digit_transition = create_markov_matrix(len(digit))
special_transition = create_markov_matrix(len(special))

# 하위 문자 마르코프 함수
def next_char(current_char, char_list, transition_matrix):
    idx = char_list.index(current_char)
    next_idx = np.random.choice(range(len(char_list)), p=transition_matrix[idx])
    return char_list[next_idx]

# 상위 상태에 따른 문자군 선택 및 하위 전이 적용
def generate_password_with_subchains(start_state_idx, steps):
    current_state = start_state_idx
    password = ""
    state_trace = []
    
    # 초기 문자 랜덤 선택
    current_chars = {
        'k': random.choice(lower),
        'e': random.choice(lower),
        'n': random.choice(digit),
        'x': random.choice(special),
        'E': random.choice(upper)
    }

    for _ in range(steps):
        state = states[current_state]
        char = current_chars[state]
        password += char
        state_trace.append(f"{state}({char})")

        # 다음 문자 결정 (하위 마르코프)
        if state == 'k' or state == 'e':
            current_chars[state] = next_char(char, lower, lower_transition)
        elif state == 'E':
            current_chars[state] = next_char(char, upper, upper_transition)
        elif state == 'n':
            current_chars[state] = next_char(char, digit, digit_transition)
        elif state == 'x':
            current_chars[state] = next_char(char, special, special_transition)

        # 다음 상위 상태 결정
        current_state = np.random.choice(range(5), p=state_transition[current_state])

    return password, state_trace

# 실행
start_state = 2  # 'e'
password, trace = generate_password_with_subchains(start_state, 12)

print("마르코프 체인 경로:", ' -> '.join(trace))
print("생성된 비밀번호:", password)
