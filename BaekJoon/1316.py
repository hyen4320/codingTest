N=int(input())
count=N
for i in range(N):
    sentence=list(input())
    for j in range(len(sentence)-1):
        if sentence[j]==sentence[j+1]:#일치하면 아직까지는 그룹단어임
            pass
        elif sentence[j] in sentence[j+1:]:# 일치하지 않는데 문장에 있으면 그룹단어 아님
            count-=1
            break
print(count)
        
        