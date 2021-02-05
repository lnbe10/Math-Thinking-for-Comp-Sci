

def extended_gcd(a,b):
	#assert a >= b and b >= 0 and a + b > 0;
	at = max(a,b);
	bt = min(a,b);
	a = at;
	b = bt;
	if b == 0:
		d ,x ,y = a, 1, 0
	else:
		(d, p, q) = extended_gcd(b, a % b);
		x = q;
		y = p - q * (a // b);
	assert a % d == 0 and b % d == 0;
	assert d == a * x + b * y;
	#print('gcd({}, {}) = {}'.format(a,b,d));
	return(d, x, y);


