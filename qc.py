#def q0q1q2(a,i):
def transicao_a(a,i):
    if a[i]  == "a":
        return True
#def q0q1q2q3(a,i):
def transicao_b(a,i): 
    if a[i] == "b": 
        return True
    
def check(qq):
    newqq = qq
    states = 0
    
    if transicao_a(newqq,states) == True:
        print("q0 --> q1")
        states += 1
        if len(newqq) == 1:
            return True
        elif transicao_a(newqq,states) == True:
            print("q1 --> q2")
            while newqq[states] == "a" and states < len(newqq)-1:
                print("q2")
                states += 1
            if transicao_b(newqq,states) == True:
                print("q1 --> q3")
                return True
            else:
                return False
        elif transicao_b(newqq,states) == True:
            print("q1 --> q4")
            while states < len(newqq):
                print("q4")
                if newqq[states] != "b":
                    return False
                states += 1
            return True
        else:
            return False    
                
    elif transicao_b(newqq,states) == True and len(newqq) == 1:
        print("q0 --> q3")
        return True
    else:
        return False    

#teste1
print(check("a"))
#teste2
print(check("b"))
#teste3
print(check("aaaaaaaaaaaaab"))
#teste4
print(check("abbbbbbbbbbbbb"))
#teste5
print(check("abc"))
#teste6
print(check("cccccb"))
#teste7
print(check("ddddd"))
