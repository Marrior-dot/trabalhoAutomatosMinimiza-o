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
        print("q0 --> q1, a")
        states += 1
        if len(newqq) == 1:
            return True
        elif transicao_a(newqq,states) == True:
            print("q1 --> q2, a")
            states += 1
            while newqq[states] == "a" and states < len(newqq)-1:
                print("q2, a")
                states += 1
            if transicao_b(newqq,states) == True:
                print("q2 --> q3, b")
                return True
            else:
                return False
        elif transicao_b(newqq,states) == True:
            print("q1 --> q4, b")
            states += 1
            while states < len(newqq):               
                if newqq[states] != "b":
                    return False
                states += 1
                print("q4, b")
            return True
        else:
            return False    
                
    elif transicao_b(newqq,states) == True and len(newqq) == 1:
        print("q0 --> q3, b")
        return True
    else:
        return False    

print("teste 1 - a")
print(check("a"))
print("\n")

print("teste 2 - b")
print(check("b"))
print("\n")

print("teste 3 - aaaaaaaaaaaaab") 
print(check("aaaaaaaaaaaaab"))
print("\n")

print("teste 4 - abbbbbbbbbbbbb")
print(check("abbbbbbbbbbbbb"))
print("\n")

print("teste 5 - abc")
print(check("abc"))
print("\n")

print("teste 6 - cccccb") 
print(check("cccccb"))
print("\n")

print("teste 7 - ddddd")
print(check("ddddd"))
