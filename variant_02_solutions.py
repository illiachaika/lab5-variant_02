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
    return  x-1*(math.log(x)-1/(1+x**2)) 

#Iterator function
def solve_iteration(func: Callable[[float],float], x0: float, prec:float)-> dict:

    """Will return dictionary of such kind:
      {"xk":float, "n_iter":int, "l_iter":list, "q": float, "status":str}
      "q" is a calculated coefficient of convergeance (based on last 10 results if possible)"""
    
    limita=10**6
    #Fail switch for when iterations don't converge
    #limita means maximum number of iterations

    xk=x0
    n_iter=0
    l_iter=[xk]

    #iterator cycle
    while  abs(xk-(xk:=func(xk)))>prec*(1-0.8)/0.8: 
        #In this scenario derivative is mainly positive, so correction factor was introduced
        #Mind you, this correction factor could be not enough for all x0 but at least 
        #it does its job where you would expect it to.

        n_iter+=1
        l_iter+=[xk]

        #For when n_iter exceeds maximum amount of iterations
        if n_iter>limita:

            print("Exceeded maximum iteration step")

 #Calculates coefficient of convergeance if it is possilbe else defaults it to 1.0

            n_q=12 if len(l_iter)>11 else len(l_iter) #checks if there are enough elements for full q calculation
            
            q_l=[abs(l_iter[-i]-l_iter[-i-1])/(abs(l_iter[-i-1]-l_iter[-i-2])) 
            for i in range(1,n_q-1) 
            if abs(l_iter[-i-1]-l_iter[-i-2])!=0] if n_q>=3 else [1]

            q=sum(q_l)/len(q_l)

            status="Failed convergeance\n Exceeded maximum iteration step"
            break
    else:
        print("Success")

        status="Successful convergeance"

#Same piece of code for calculating q
        n_q=12 if len(l_iter)>11 else len(l_iter) 

        q_l=[abs(l_iter[-i]-l_iter[-i-1])/(abs(l_iter[-i-1]-l_iter[-i-2]))
        for i in range(1,n_q-1) 
        if abs(l_iter[-i-1]-l_iter[-i-2])!=0] if n_q>=3 else [1]

        q=sum(q_l)/len(q_l)

    """Thinking retrospectively It was worth to create a special function to calculate q.
     Because this is barely readable for no good reason"""
    print(f"Mean coefficient of convergeance={q}")
    return {"xk":xk,
            "n_iter":n_iter,
            "l_iter":l_iter, 
            "q": q, 
            "status":status}
def save_results_to_file(d_result:dict):

    with open("results_variant_02.txt", "w", encoding="utf-8") as res:

        Long_N=max(len(f"{i:.6f}") for i in d_result["l_iter"]) #Checks how long is the longest number

        res.write("Calculation result:\n")
        res.write(f"Root: {d_result["xk"]:.6f}\n")
        res.write(f"|Degree of iteration|   {" "*((Long_N-15)//2)}X_N Value{" "*((Long_N-15)//2+(Long_N-15)%2)}   $")
        #Based on how long is our Long_N builds a table so it would be able to contain it
        #Also this command keeps "X_N Value" centered         
        #Iterations list turned into fine table
        for i, x_n in enumerate(d_result["l_iter"], start=1):
            res.write("\n")
            l1=len(f"{i}")
            l2=len(f"{x_n:.6f}")

            res.write( f"|{i}{" "*(18-(l1-1))}|")
            res.write(f"{x_n:.6f}{" "*(15-l2 if Long_N<15 else Long_N-l2)}{"$" if i%2==0 else "|"}")
            #All of that to make "perfect table"


if __name__=="__main__":
    print("Method of simple iterations")
    x0=...
    preci=...
    while x0==...:
        
        x0=input("Enter a number as a starting point for iterations:_")
        try:    
            x0=float(x0)
        except ValueError:
            x0=...
            print("Try again")
    print("Enter needed precision\n" \
        "For example 0.0001 should return result actual root+-0.0001")
    while preci==...:
        preci=input("Enter there:_")
        try:
            preci=float(preci)
        except ValueError:
            print("Try again")
            preci=...
    Result_D=solve_iteration(phi,x0,preci)
    print(f'Root:{Result_D["xk"]:.6f}')
    print(f'Number of iterations{Result_D["n_iter"]}')
    save_results_to_file(Result_D)
    print("Full iteration report was recorded into results_variant_02.txt")
    print(Result_D["status"])