def q0q1q2q3(a,i):
    if a[i]  == "a":
        i += 1
        if a[i]  == "a":
            i += 1
            if a[i]  == "a":
                return True
    else:
        return False
'''    
def q1(a):
    if a == "a":
        return True
    else:
        return False
    
def q2(a):
    if a == "a": 
        return True
    else:
        return False
def q3(a):
    if a == "c" or a == "b":
        return True
'''    
def check(qq):
    newqq = qq
    while type(newqq) != str:
        newqq = str(input("Escolha uma string"))
    
    states = 0    
    terminal = True

    if q0q1q2q3(newqq[states]) == True:
        print(terminal)
        states += 1
    else:
        terminal = False
        print(terminal)
        return terminal
'''    
    if q2(newqq[states]) == True:
            states += 1
    else:
        terminal = False
        return terminal
    
    if q3(newqq[states]) == True:
        while(newqq[states] == "c"):
            states += 1
            if states == len(newqq):
                return terminal
        
    else:
        pass
    
    return terminal
'''
print(check("aaa"))