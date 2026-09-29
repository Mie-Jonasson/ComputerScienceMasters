"""Find real x,y satisfying x+y >= 3 and x-y <= 1.
    Ref: Introduction to Neural Network Verification by Aws Albarghouthi
    https://verifieddeeplearning.com/nnv_book.pdf page: 74
"""

from fractions import Fraction

# %% 
def build_constraints():
    inf = float("inf")
    rows = {
        "s": {"x": 1, "y": 1},
        "t": {"x": 1, "y": -1},
    }
    bounds = {
        "x": (-inf, inf),
        "y": (-inf, inf),
        "s": (3, inf), # s >= 3 encodes x + y >= 3.
        "t": (-inf, 1), # t <= 1 encodes x - y <= 1.
    }
    return rows, bounds


# %% 
def pivot(rows, basic, variable):
    # TO-DO: implement the pivot
    raise NotImplementedError("TO-DO 2: implement pivot")


# %% 
def simplex(rows, bounds):
    rows = {
        basic: {name: Fraction(c) for name, c in row.items()}
        for basic, row in rows.items()
    }
    values = {name: Fraction(0) for name in bounds}
    # TO-DO: implement the simplex repair loop

    raise NotImplementedError("TO-DO 3: implement simplex")


# %% Run the example
if __name__ == "__main__":
    rows, bounds = build_constraints()
    solution = simplex(rows, bounds)

    if solution is None:
        print("UNSAT")
    else:
        x, y = solution["x"], solution["y"]
        assert x + y >= 3 and x - y <= 1, "Check the original inequalities."
        print("SAT: x =", x, "y =", y)
