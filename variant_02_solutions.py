"""
LabWork #5: "Functions and task decomposition 
Variant: 2
Student: [Chaika, Illia]
Group: [EIP30(1)]
"""
import math
from typing import Callable


#Function to use for futher iterations
def phi(x:float)-> float:
    return  x-2.6*(math.log(x)-1/(1+x**2)) 

#Iterator function
def solve_iteration(func: Callable[[float],float], x0: float, prec:float)-> dict:

    """Will return dictionary of such kind:
      {"xk":float, "n_iter":int, "l_iter":list, "q": float, "status":str}
      "q" is a calculated coefficient of convergeance (based on last 10 results if possible)"""
    
    limita=1300 
    #Fail switch for when iterations don't converge
    #limita means maximum number of iterations

    xk=x0
    n_iter=0
    l_iter=[xk]

    #iterator cycle
    while  abs(xk-(xk:=func(xk)))>prec:
        n_iter+=1
        l_iter+=[xk]

        #For when n_iter exceeds maximum amount of iterations
        if n_iter>limita:

            print("Exceeded maximum iteration step")

            n_q=12 if len(l_iter)>10 else len(l_iter) 
            #checks if there are enough elements for full q calculation

            q=sum(abs(l_iter[-i]-l_iter[-i-1])/(abs(l_iter[-i-1]-l_iter[-i-2])) 
            for i in range(1,n_q-1) if abs(l_iter[i+1]-l_iter[i])!=0)/(n_q-2) if n_q>=3 else 1
            #if it is not possible to calculate "q" it defaults to 1.0

            print(f"Mean coefficient of convergeance={q}")

            status="Failed convergeance\n Exceeded maximum iteration step"
            break
    else:
        print("Success")

        status="Successful convergeance"

        n_q=12 if len(l_iter)>12 else len(l_iter)

        q=sum(abs(l_iter[-i]-l_iter[-i-1])/(abs(l_iter[-i-1]-l_iter[-i-2]))      
        for i in range(1,n_q-1) if abs(l_iter[i+1]-l_iter[i])!=0)/(n_q-2) if n_q>=3 else 1 

    return {"xk":xk,
            "n_iter":n_iter,
            "l_iter":l_iter, 
            "q": q, 
            "status":status}




if __name__=="__main__":
    a=solve_iteration(phi, 1, 0.0001)
    print(f"xk={a["xk"]}","\n", f"n_iter={a["n_iter"]}","]\n", f"q={a["q"]}")
    print(a["status"])
    print("---------------------------")
    print(a["l_iter"] if len(a["l_iter"])<50 else a["l_iter"][-1:-20:-1])
    print(len(a["l_iter"]),a["n_iter"])



        




