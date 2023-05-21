def q0q1q2q3(a,i):
    if a[i]  == "a":
        i += 1
        if a[i]  == "a":
            i += 1
            if a[i]  == "a":
                return True
    else:
        return False
def q0q1q4(a,i): 
    if(a[i] == "b" or a[i] == "c"):
        return True
        
   
       
def check(qq):
    newqq = qq
    while type(newqq) != str:
        newqq = str(input("Escolha uma string"))
    
    states = 0    
    terminal = True

    if q0q1q2q3(newqq,states) == True:
        states = 3
        if(len(newqq)) == 3:
            return True
        else:
            if q0q1q4(newqq,states) == True:
                while states < len(newqq)-1:
                    states += 1
                    if newqq[states] != "b" and newqq[states] != "c":
                        #print("aq")
                        return False
            else:
                return False           
    else:
        pass
    
    if q0q1q4(newqq,states) == True:
        while newqq[states] == "b" or newqq[states] == "c":
            states += 1
        if q0q1q2q3(newqq,states) == True:
            return True
        else:
            return False
    else:
        return False
    
  #  if q0q1q2q3(newqq,states) == True:
   #     return False
  #  else:
   #     return True

print(check("abababab"))