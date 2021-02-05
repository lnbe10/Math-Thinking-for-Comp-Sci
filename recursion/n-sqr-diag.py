# Can we fill a NxN Square with D
# diagonals that don't touch each other?

# -1 = unassigned
#  0 = no diagonal
#  1 = /
#  2 = \

# I'll store the info in a 2D-array, starting unassigned

N = 5;
D = 16;


# Can't table's

# element in (i,j) == /, 1
#      j-1  j    j+1
# i-1       2    1
# i    2    /    2
# i+1  1    2


# element in (i,j) == \, 2
#      j-1  j    j+1
# i-1  2    1
# i    1    \    1
# i+1       1    2

def can_put(a, i, j, k):
	print('problema',a)
	print(i,j)


	if k == 0:
		return True;

	if i==0 and j==0:
		return True;

	if i==0 and j!=0:
		if k == 1:
			return a[i][j-1] != 2;
		if k == 2:
			return a[i][j-1] != 1;
	
	if i!=0 and j==0:
		if k == 1:
			return (a[i-1][j] != 2 and a[i-1][j+1] != 1);
		if k == 2:
			return a[i-1][j] != 1

	if i!=0 and j!=0 and j!=N:
		if k == 1:
			c1 = a[i-1][j  ] != 2;
			c2 = a[i-1][j+1] != 1;
			c3 = a[i  ][j-1] != 2;
			return c1 and c2 and c3;
		if k == 2:
			c1 = a[i-1][j-1] != 2;
			c2 = a[i-1][j  ] != 1;
			c3 = a[i  ][j-1] != 1;
			return c1 and c2 and c3;

	if i!=0 and j==N:
		if k == 1:
			c1 = a[i-1][j  ] != 2;
			c3 = a[i  ][j-1] != 2;
			return c1 and c3;
		if k == 2:
			c1 = a[i-1][j-1] != 2;
			c2 = a[i-1][j  ] != 1;
			c3 = a[i  ][j-1] != 1;
			return c1 and c2 and c3;





def extend(a, N):
	if sum(len(row) for row in a) == N*N:
		#print(a);
		return;


	i = len(a)-1;
	j = len(a[i])-1;
	print(a, i, j)	
	if j == N-1:
		ni, nj = i+1, 0;
	else:
		ni, nj = i, j+1;

	for k in [0,1,2]:
		a[ni].append(k);
		if can_put(a,ni,nj, k):
			extend(a,N);
		a[i].pop()


extend([[-1]],N);