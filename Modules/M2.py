#Khyathi Cheedalla
#Roll Number: 20186037
#--------------------------
def cross(A, B):
    return [a+b for a in A for b in B]
digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = cross(rows, cols)
# print(squares)
unitList = ([cross(rows, c) for c in cols] + [cross(r, cols) for r in rows] + [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
# print(unitList)
units = dict((s, [u for u in unitList if s in u]) for s in squares)
# print(units['A1'])
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in squares)
def parse_grid(grid):
	values = dict((s, digits) for s in squares)
	#print(values)
	for s,d in grid_values(grid).items():
		if d in digits and not assign(values, s, d):
			return False
	return values

def grid_values(grid):
	chars = [c for c in grid if c in digits or c in '0.']
	#print(chars)
	assert len(chars) == 81
	#print(dict(zip(squares, chars)))
	return dict(zip(squares, chars))

def assign(values, s, d):
	# print(values, s, d)
	other_values = values[s].replace(d, '')
	# print(other_values)
	if all(eliminate(values, s, d2) for d2 in other_values):
		return values
	else:
		return False

def eliminate(values, s, d):
	if d not in values[s]:
		return values
	
	values[s] = values[s].replace(d, '')
	if len(values[s]) == 0:
		return False
	elif len(values[s]) == 1:
		d2 = values[s]
		if not all(eliminate(values, s2, d2) for s2 in peers[s]):
			return False
	for u in units[s]:
		dplaces = [s for s in u if d in values[s]]
		if len(dplaces) == 0:
			return False
		elif len(dplaces) == 1:
			if not assign(values, dplaces[0], d):
				return False
	return values
def display(values):
	width = 1+max(len(values[s]) for s in squares)
	line = '+'.join(['-'*(width*3)]*3)
	for r in rows:
		#print(''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in cols))
		if r in 'CF': print(line)
	print()
grid1 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'		
display(parse_grid(grid1))		