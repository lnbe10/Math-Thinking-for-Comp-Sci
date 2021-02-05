# element in (i,j) == /, 1
#      j-1    j    j+1
# i-1         2     1
# i     2     /    



# element in (i,j) == \, 2
#      j-1   j    j+1
# i-1   2    1
# i     1    \    



N = 5;
D = 16;
a = [[-1 for i in range(N+2)] for i in range(N+2)];

def can_put(a, i, j):


	if a[i][j] == 0:
		if countX(a,0) <16:
			return True
		return False

	if i==0 and j==0:
		return True;

	if a[i][j] == 1:
		c1 = a[i-1][j  ] != 2;
		c2 = a[i-1][j+1] != 1;
		c3 = a[i  ][j-1] != 2;
		return c1 and c2 and c3;

	if a[i][j] == 2:
		c1 = a[i-1][j-1] != 2;
		c2 = a[i-1][j  ] != 1;
		c3 = a[i  ][j-1] != 1;
		return c1 and c2 and c3;

def countX(lst, x): 
    count = 0
    for ele in lst: 
        if (ele == x): 
            count = count + 1
    return count


def extend(a, N, i, j):
	
	if i == N and j == N:
		for row in a:
			print(row[1:len(a[0])-2],'\n');
		return;

	if j == N:
		ni, nj = i+1, 1;
	else:
		ni, nj = i, j+1;
	print(ni,nj)
	for k in [0,1,2]:
		a[i][j] = k;
		if can_put(a,i,j):
			extend(a,N,ni,nj);
		a[i].pop()

extend(a,N,1,1)