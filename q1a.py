#def q0(a):
def cadeia_vazia(a):
    if a  == " " or a == "":
        return True
    
#def q1(a):
def transicao_a(a):
    if a == "a" :
        return True
    else:
        return False
    
#def q2(a):
def transicao_b(a):
    if a == "b" or a == "":
        return True
#def q3(a):
def transicao_c(a):
    if a == "c" or a == "":
        return True
    
def check(qq):
    newqq = qq
    states = 0    
    terminal = True

    if(cadeia_vazia(newqq) == True) :
        print("q0")
        return terminal
    
    if transicao_a(newqq[states]) == True :
        print("q0 --> q1")
        if states == len(newqq)-1:
            return terminal
        states += 1
        if newqq[states] == "a":
            terminal = False
            return terminal
    else:
        terminal = False
        return terminal
    
    if transicao_b(newqq[states]) == True:
        print("q1 --> q2")
        while newqq[states] == "b":
            print("q2")
            states += 1
            if states == len(newqq):
                return terminal
    else:
        pass
    if transicao_c(newqq[states]) == True:
        if newqq[states-1] == "a":
            print("q1 --> q3")
        else:
            print("q2 --> q3")
        while(newqq[states] == "c"):
            states += 1
            print("q3")
            if states == len(newqq):
                return terminal
    else:
        pass
    
    return terminal

#teste1
print(check(""))
#teste2
print(check("a"))
#teste3
print(check("acccc"))
#teste4
print(check("abbcccc"))
#teste5
print(check("abbbb"))
#teste6
print(check("bbbbb"))
#teste7
print(check("cccccc"))

