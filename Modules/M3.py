#Khyathi Cheedalla
#20186037
#----------------------------------------
def parse_grid(grid):
    values = dict((s, digits) for s in squares)
    # print(values)
    for s,d in grid_values(grid).items():
        
        if d in digits and not assign(values, s, d):
            # print(d)
            return False ## (Fail if we can't assign d to square s.)
    return values

def solve(grid): return search(parse_grid(grid))

def search(values):
    "Using depth-first search and propagation, try all possible values."
    #print(values)
    if values is False:
        return False
    if all(len(values[s]) == 1 for s in squares):
        return values
    ## Chose the square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    print(n)
    print(s)
    print(values[s])
    return some(search(assign(values.copy(), s, d)) for d in values[s])

def some(seq):
    for e in seq:
        if e:
            return e
    return False

def display(values):
    "Display these values as a 2-D grid."
    width = 1+max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        #print (''.join(values[r+c].center(width)+('|' if c in '36' else '')  for c in cols))
        if r in 'CF': print (line)
    print()

def grid_values(grid):
    "Convert grid into a dict of {square: char} with '0' or '.' for empties."
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))

def assign(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected."""
    # print("values,s,d values in assign function")
    # print(values)
    # print(s)
    # print(d)
    other_values = values[s].replace(d, '')
    # print("other_values--> "+ other_values)
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def eliminate(values, s, d):
    """Eliminate d from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected."""
    # print("values got in--->  ")
    # print(values)
    # print("s value--->  " + s)
    # print("d value --->  " + d)
    if d not in values[s]:
        # print("came here")
        # print("values")
        return values ## Already eliminated
    
    values[s] = values[s].replace(d,'')
    # print(values[s])
    ## (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
    if len(values[s]) == 0:
        return False ## Contradiction: removed last value
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    ## (2) If a unit u is reduced to only one place for a value d, then put it there.
    for u in units[s]:
        # print("u places---> ")
        # print(u)
        dplaces = [s for s in u if d in values[s]]
        # print("dplaces --> anta")
        # print(dplaces)
        if len(dplaces) == 0:
            return False ## Contradiction: no place for this value
        elif len(dplaces) == 1:
            # d can only be in one place in unit; assign it there
            if not assign(values, dplaces[0], d):
                return False
    return values

def cross(A, B):
    "cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
    [cross(r, cols) for r in rows] +
    [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
# print(unitlist)
units = dict((s,[u for u in unitlist if s in u]) for s in squares)
# print(units)
peers = dict((s, set(sum(units[s],[])) - set([s])) for s in squares)
# print(peers)

grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
grid1 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
grid3 = '....6....59.....82....8....45........3........6..3.54...325..6...................'

print(display(solve(grid3)))