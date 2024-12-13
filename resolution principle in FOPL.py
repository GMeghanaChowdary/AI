from sympy import symbols, Not, Or, simplify 
def resolve(clause1, clause2):
    """ Resolve two clauses and return the resulting resolvent. """ 
    resolvent = [] 
    for literal1 in clause1: 
        for literal2 in clause2: 
            if literal1 == Not(literal2) or literal2 == Not(literal1): 
                resolvent.extend([l for l in (clause1 + clause2) if l != literal1 and l !=literal2]) 
    return list(set(resolvent))

def resolution(clauses): 
    """ Apply resolution to a set of clauses until no new clauses can be generated. """ 
    new_clauses = list(clauses) 
    while True: 
        n = len(new_clauses)
        print(new_clauses) 
        print("	") 
        pairs = [(new_clauses[i], new_clauses[j]) for i in range(n) for j in range(i+1, n)] 
        for (clause1, clause2) in pairs: 
            print(clause1) 
            print(clause2) 
            resolvent = resolve(clause1, clause2) 
            print(resolvent) 
            print("	") 
            if not resolvent: 
                # Empty clause found, contradiction reached 
                return True 
            if resolvent not in new_clauses: 
                new_clauses.append(resolvent) 
        if n == len(new_clauses):
            # No new clauses can be generated, exit loop 
            return False

# Example usage:
if __name__ == "__main__":
    
# Example clauses in CNF (Conjunctive Normal Form) 
    clause1 = [symbols('P'), Not(symbols('Q'))]
    clause2 = [Not(symbols('P')), symbols('Q')]
    clause3 = [Not(symbols('P')), Not(symbols('Q'))]

    # List of clauses
    clauses = [clause1, clause2, clause3] 
    result = resolution(clauses)
    if result:
        print("The set of clauses is unsatisfiable (contradiction found).")
    else:
        print("The set of clauses is satisfiable.")
