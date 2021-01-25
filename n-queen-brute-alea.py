# Queen's problem:
# Can we put N Queen's that doesn't attack each
# other in a NxN (square) table ?


# i'll do a 1D-array implementation, so
# the index is the row, and the number is the col

# a index:  0 1 2 3 4 5 6 7 (col)
# a[index]: 0 2 4 6 5 1 7 3 (row)

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

# Each Queen has to be in a different row, so
# we have each values in the list different
# Also, the Queens cannot be in the same diagonal
# so, if 2 Queen's positions are (i1, j1) and
# (i2, j2), we have abs(i1-i2) != abs(j1-j2)

#starting first by implement the 'solution check':

def isSol(a):
	n = len(a);
	for i in range(n):
		for j in range(i+1, n):
			if a[i] == a[j]:
				#print('\nthe %d th element and the %d th element are equal!\n' %(i, j) );
				#print('\nso it\' not a solution!\n');
				return False;
			if abs(j-i) == abs(a[j] - a[i]):
				#print('\nthe queens in (%d, %d) and (%d, %d) are in the same diagonal!\n' %(i, a[i], j, a[j]) );
				#print('\nso it\' not a solution!\n');
				return False;
	#print('is a solution!');
	return True;

sol5 = [0,3,1,4,2]; # that's a solution for 5x5 table .-.
#isSol(sol5); # right!


# now we can check if any array is a solution, we can iterate over them!
# to gain a little bit of computational time, it's important to remember
# that the queen's rows and cols should be a permutational group!!!!!!!!
# so we don't have any element twice in the 1D-array, wich takes us to
# a brute force N! search... I'm not good at all yet, so I don't know if we can cut
# down this O(time) .-. with some good algo...

# this is a random finder .-. not good at all!
import random as rd

def Founder(N, iters):
	base = [n for n in range(0,N)]; #[0,1,...,N-1] we have N element's there!
	i = 1;

	while i < iters:
		b = base.copy();
		val = [];
		for i in range(N-1):
			if len(b) > 1:
				a = rd.randint(0, len(b)-1);
				val.append(b[a]);
				b.remove(b[a]);
			if len(b) == 1:
				val.append(b[0])
				b.remove(b[0])	
		if isSol(val) == True:
			print('solution found at iteration %d!\n\n%s\n\n' %(i, val));
			i = 10001;
			return val;
		else:
			i += 1;

Founder(5,10000);
Founder(8,10000);

