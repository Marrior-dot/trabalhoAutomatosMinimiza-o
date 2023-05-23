#def q0q1q2q3(a,i):
def transicao_aaa(a,i):
    if a[i]  == "a":
        i += 1
        if a[i]  == "a":
            i += 1
            if a[i]  == "a":
                return True
    else:
        return False
#def q0q1q4(a,i):
def transicao_bc(a,i): 
    if a[i] == "b" or a[i] == "c":
        return True
        
def check(qq):
    newqq = qq
    states = 0    
    terminal = True

    if transicao_aaa(newqq,states) == True:
        states = 3
        print("q0 --> q1\nq1 --> q2\nq2 --> q3")
        if(len(newqq)) == 3:
            return True
        else:
            if transicao_bc(newqq,states) == True:
                print("q3-->q4")
                while states < len(newqq)-1:
                    print("q4")
                    states += 1
                    if transicao_bc(newqq,states) == False:
                        return False
                return True
            else:
                return False           
    else:
        pass
    
    if transicao_bc(newqq,states) == True:
        print("q0 --> q5")
        while (newqq[states] == "b" or newqq[states] == "c") and states < len(newqq)-1:
            print("q5")
            states += 1
        if transicao_aaa(newqq,states) == True and states == len(newqq) - 3:
            print("q5 --> q6\nq6 --> q7\nq7 --> q8")
            return True
        else:
            print(states)
            return False
    else:
        return False
#teste1
print(check("aaabcbcbb"))
#teste2
print(check("bcbcbbaaa"))
#teste3
print(check("bcbcbcbcbcb"))
#teste4
print(check("ddddddd"))