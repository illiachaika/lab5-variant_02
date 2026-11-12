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
    while  abs(xk-(xk:=func(xk)))>prec*(1-0.6)/0.6: 
        #In this scenario derivative is positive, so correction factor was introduced
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

           

            print(f"Mean coefficient of convergeance={q}")

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
        res.write(f"|Degree of iteration|   {" "*((Long_N-15)//2)}X_N Value{" "*((Long_N-15)//2+(Long_N-15)%2)}   |\n")
        #Based on how long is our Long_N builds a table so it would be able to contain it
        #Also this command keeps "X_N Value"          
        
        #res.write( f"|{" "*12}{1}{" "*6}|{" "*4}{1:.6f}{" "*3}|\n") (redument command for setting things up)
        
        #Iterations list turned into fine table
        for i, x_n in enumerate(d_result["l_iter"], start=1):
            l1=len(f"{i}")
            l2=len(f"{x_n:.6f}")
            res.write( f"|{" "*(0)}{i}{" "*(18-(l1-1))}|")

            #There are some reduments like *(0). It was used to try to center a number.
            #Even though attempts to center were successful the result wasn't satisfactory

            res.write(f"{" "*(0)}{x_n:.6f}{" "*(15-l2 if Long_N<15 else Long_N-l2)}|\n")

            #(l1-1)+(l1-1)//2 (redument that was used for centring)




if __name__=="__main__":
    a=solve_iteration(phi, 13, 0.0001)
    print(f"xk={a["xk"]}","\n", f"n_iter={a["n_iter"]}","]\n", f"q={a["q"]}")
    print(a["status"])
    print("---------------------------")
    print(a["l_iter"] if len(a["l_iter"])<50 else a["l_iter"][-1:-20:-1])
    print(len(a["l_iter"]),a["n_iter"])
    save_results_to_file(a)