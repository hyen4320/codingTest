def recursive_function(i):
    if i==100:
        return 
    print(i,'재귀함수 호출')
    recursive_function(i+1)
recursive_function(1)
