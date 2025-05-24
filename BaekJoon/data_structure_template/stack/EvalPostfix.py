from ArrayStack import ArrayStack
def evalPostfix(expr):
    s=ArrayStack[100]

    for token in expr:#expr의 항들이 순서대로 대입됨
        if token in "+-/*":
            val2=s.pop()#순서 맞추기 위해 2부터
            val1=s.pop()
            if token=="+":s.push(val1+val2)
            elif token=="-":s.push(val1-val2)
            elif token=="/":s.push(val1/val2)
            elif token=="*":s.push(val1*val2)
        else:s.push(float(token))#문자열을 실수로 변경
    return s.pop()
##연산자 우선순위 계산 함수
def predence(op):
    if op in ('(',')'):
        return 0
    elif op in ('+','-'):
        return 1
    elif op in ('*','/'):
        return 2
    else: return -1

#중위표기 수식의 후위표기 변환
def Infix2Postfix(expr):
    s=ArrayStack(100)
    output=[]

    for term in expr:
        if term in '(':
            s.push('(')
        elif term in ')':
            while not s.isEmpty():#왼쪽괄호 나올 때 까지 연산자 꺼내서 출력
                op = s.pop()
                if op =='(':
                    break
                else:
                    output.append(op)
        elif term in "+-/*":#연산자면 스택에서 같거나 높은 연사자를 모두 꺼내 출력
            while not s.isEmpty():
                op = s.peek()
                if(predence(term)<=predence(op)):#우선순위 비교
                    output.append(op)
                    s.pop()
                else:break
            s.push(term)#스택에 삽입
        else:
            output.append(term)#피연산자면 바로 출력
    while not s.isEmpty():#처리 끝 남은거 출력
        output.append(s.pop())
    return output#최종 후위표기식을 반환