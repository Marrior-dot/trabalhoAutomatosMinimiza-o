def q0(a):
    if a  == " " or a == "":
        return True
    
def q1(a):
    if a == "a":
        return True
    else:
        return False
    
def q2(a):
    if a == "b" or a == "":
        return True
def q3(a):
    if a == "c" or a == "":
        return True
    
def check(qq):
    newqq = qq
    while type(newqq) != str:
        newqq = str(input("Escolha uma string"))
    
    states = 0    
    terminal = True

    if(q0(newqq) == True) :
        return terminal
    
    if q1(newqq[states]) == True:
        print(terminal)
        states += 1
        if states == len(newqq):
            return terminal
        
    else:
        terminal = False
        print(terminal)
        return terminal
    
    if q2(newqq[states]) == True:
        while newqq[states] == "b":
            states += 1
            if states == len(newqq):
                return terminal
        
    else:
        pass
    if q3(newqq[states]) == True:
        while(newqq[states] == "c"):
            states += 1
            if states == len(newqq):
                return terminal
        
    else:
        pass
    
    return terminal

print(check("abbbbccc"))

    
'''
    for states in range(0,len(qq)):
        if(q0(qq[states]) == True):
            return terminal
        else:
            states += 1
            if(q1(qq[states]) == False):
                terminal = False
                return terminal
            else:
'''
                
                    
                
    
    

