'''
author:xiesunsun
date:5-14:9-45
descrption:中缀表达式转为逆波兰式 并计算相应的表达式的值 注意这里的后缀表达式不需要相应的 括号来表示优先级
constraint:op 符号有限制的 无法穷举所有的运算符号情况（+-*/）
'''
def changeCalcuType(data):
    '''中缀转相应的后缀'''
    # data=input('输入相应的中缀表达式')
    opstack=['#']
    resstack=[]
    for i in data:
        if i not in op:
            resstack.append(i)
            
        else:
            if i=='(':
                opstack.append(i)
            elif i==')':
                for i in range(opstack[::-1].index('(')+1):
                    resstack.append(opstack.pop())
                resstack.pop()#舍弃掉相应的括号操作
            else:
                if opstack[-1]=='(':
                    opstack.append(i)
                else:
                    if prioty[i]>prioty[opstack[-1]]:
                        opstack.append(i)
                    else:
                        while prioty[opstack[-1]]>=prioty[i] and opstack[-1]!='(':
                            resstack.append(opstack.pop())
                        opstack.append(i)
    while opstack[-1]!='#':
        resstack.append(opstack.pop())
    print(resstack)
    return resstack
def cacuRepolishValue(data):
    '''计算相应逆波兰式的值'''
    resstack=[]
    for i in data:
        if i not in op:
            resstack.append(i)
        else:
            op1=resstack.pop() 
            op2=resstack.pop()
            data=int(eval(str(op1)+i+str(op2)))
            resstack.append(data)
    print(resstack[-1])
    return resstack[-1]

    
                            
                            

                    
                    
if __name__=='__main__':
    op=['+','-','*','/','(',')']
    prioty={'+':0,'-':0,'*':1,'/':1,'(':30,')':30,'#':-1000}
    cacuRepolishValue(changeCalcuType(str('(1+2)*3')))
    
