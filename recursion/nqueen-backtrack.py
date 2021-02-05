# Queen's problem:
# Can we put N Queen's that doesn't attack each
# other in a NxN (square) table ?


# i'll do a 1D-array implementation, so
# the index is the row, and the number is the col

# perm index:  0 1 2 3 4 5 6 7 (col)
# perm[index]: 0 2 4 6 5 1 7 3 (row)

# equivalent table
#           0 1 2 3 4 5 6 7
#        0  x 0 0 0 0 0 0 0
#        1  0 0 0 0 0 x 0 0
#        2  0 x 0 0 0 0 0 x
#        3  0 0 0 0 0 0 0 0
#        4  0 0 x 0 0 0 0 0
#        5  0 0 0 0 x 0 0 0
#        6  0 0 0 x 0 0 0 0
#        7  0 0 0 0 0 0 x 0




def gen_perm(perm, N):
	if len(perm) == N:
		print(perm);
		return;

	for k in range(N):
		if k not in perm:
			perm.append(k);
			gen_perm(perm,N);
			perm.pop();


#gen_perm([] , 4);

# permutations generate queen's positions that
# have different cols for each row naturally...
# so, we only have to create a function to check
# if the newest element is not in the same
# diagonal as each of the previous ones....

def can_extend_sol(perm):
	i = len(perm) - 1;

	for j in range(i):
		if i - j == abs(perm[i] - perm[j]):
			return False;
	return True;


# If we combine the two functions,
# we can make a backtracking method to, maybe,
# take less steps to solution!
# the idea: if a part of our sulution attempt
# can't follow the rules, we don't need to
# extend it anymore and even check it again!


def extend(perm, N):
	if len(perm) == N:
		print(perm);
		return;

	for k in range(N):
		if k not in perm:
			perm.append(k);

			if can_extend_sol(perm):
				extend(perm, N);

			perm.pop()



extend([], 8);

$4+8+16+18+18+16+8+4alc
