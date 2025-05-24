from ArrayStack import ArrayStack
def isValidPos(x,y):
    if 0<=x < MAZE_SIZE and 0<= y <MAZE_SIZE:
        if map[y][x] == '0' or map[y][x]=='x':
            return True
    return False

def DFS():
    print('DFS: ')
    stack = ArrayStack(100)
    stack.push((0,1))#스택 시작위치

    while not stack.isEmpty():
        here = stack.pop()
        print(here,end='->')
        (x,y) = here# 좌표 추출

        if(map[y][x] == 'x'):#출구위치면 탈출 성공
            return True
        else :
            map[y][x]='.'##상하좌우 순으로 검사
            if isValidPos(x,y-1): stack.push((x,y-1))
            if isValidPos(x,y+1): stack.push((x,y+1))
            if isValidPos(x-1,y): stack.push((x-1,y))
            if isValidPos(x+1,y): stack.push((x+1,y))
        print('현재스택',stack)
    return False

result=DFS()
if result : print('--> 성공')
else: print('실패')

        


