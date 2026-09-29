# %% Ref: Introduction to Neural Network Verification by Aws Albarghouthi
# https://verifieddeeplearning.com/nnv_book.pdf page: 60

# TO-DO 1: e is always on; e implies a or b; a and b cannot both be on.
F = None


# %% functions
def simplify(formula, literal): 
    opposite = literal[1:] if literal.startswith("~") else "~" + literal  
    result = []

    raise NotImplementedError("TO-DO: implement deduction")

    return result 


def dpll(formula, model=None):
    model = {} if model is None else model.copy()
    # deduction 
    while True:
        if [] in formula:
            return None

        if not formula:
            return model
        
        raise NotImplementedError("TO-DO: check is any more unit clauses")

        literal = units[0]
        var = literal.removeprefix("~")
        value = not literal.startswith("~")
        
        model[var] = value
        print("BCP:", var, "=", value)
        formula = simplify(formula, literal) # apply assignment
    # search
    var = formula[0][0].removeprefix("~")

    for value in (True, False):
        branch_model = model.copy()
        branch_model[var] = value

        raise NotImplementedError("TO-DO: implement search")

        if result is not None:
            return result
    return None


# %% print solution
solution = dpll(F)

if solution is None:
    print("UNSAT")
else:
    print("SAT:", solution)

# %%
