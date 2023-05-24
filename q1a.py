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
        print("q0,e")
        return terminal
    
    if transicao_a(newqq[states]) == True :
        print("q0 --> q1, a")
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
        print("q1 --> q2, b")
        states += 1
        while newqq[states] == "b":
            print("q2, b")
            if states == len(newqq)-1:
                return terminal
            states += 1
        if newqq[states] != "c":
            return False
                     
    if transicao_c(newqq[states]) == True:
        if newqq[states-1] == "a":
            print("q1 --> q3, c")
        else:
            print("q2 --> q3, c")
        while newqq[states] == "c":
            print("q3, c")
            states += 1
            if states == len(newqq)-1:
                return terminal
        if newqq[states] != "c":
            return False
            
    else:
      pass
    return terminal

print("teste 1 - ''")
print(check(" "))
print("\n")

print("teste 2 - a")
print(check("a"))
print("\n")

print("teste 3 - acccc")
print(check("acccc"))
print("\n")

print("teste 4 - abbcccc")
print(check("abbcccc"))
print("\n")

print("teste 5 - abbbb")
print(check("abbbb"))
print("\n")

print("teste 6 - bbbbb")
print(check("bbbbb"))
print("\n")

print("teste 7 - cccccc") 
print(check("cccccc"))
print("\n")

print("teste 8 - abababab")
print(check("abababab"))
print("\n")

print("teste 9 - abbbccbcbc")
print(check("abbbccbcbc"))
print("\n")