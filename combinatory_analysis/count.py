# comb, perm

def fun(n):
	count = 0;
	for i in range(n):
	    for j in range(n):
	        for k in range(n):
	            if i < j and j < k:
	                count += 1

	print('for n = %d we have count = %d' %(n,count));
	return


for n in range(3,20):
	fun(n);

fun(1000);