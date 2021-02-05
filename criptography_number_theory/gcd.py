# great common divisor:

#Naive Algo:

def gcd(a,b):
	assert a>=0 and b>=0 and a+b > 0;

	if a == 0  or b == 0:
		return max(a,b);

	for d in range(min(a,b), 0, -1):
		if a % d == 0 and b % d == 0:
			return d;

	return 1


#Euclid's Algo

# C divides A and B if and only if
# A-B and B are divisible by C.

def gcd_1(a,b):
	print('gcd({}, {}) ='.format(a,b));
	assert a>=0 and b>=0 and a+b>0;
	count = 0;
	while a > 0 and b > 0:
		if a >= b:
			a = a % b;
		else:	
			b = b % a;
		count += 1;
	print('gcd({}, {}) = {}'.format(a,b, max(a,b)));
	print('took %d steps' %(count));
	return max(a,b);

#gcd_1(790933790547,1849639579327);
#gcd_1(7909337900547,18496390579327);
#gcd_1(79093337900547,184936390579327);
gcd_1(7909333427900547,18442936390579327);


def gcd_2(a,b):
	at = max(a,b);
	bt = min(a,b);
	a = at;
	b = bt;
	b>0 and a+b>0;
	return gcd_2(b, a%b) if b>0 else a;

#gcd_2(790933790547,1849639579327);
#gcd_2(7909337900547,18496390579327);
#gcd_2(79093337900547,184936390579327);
gcd_2(7909333427900547,18442936390579327);


# if D divides A and B, and D=Ax+By for
# integers x and y, them D = gcd(A,B)

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

#extended_gcd(790933790547, 1849639579327);
#extended_gcd(7909337900547, 18496390579327);
#extended_gcd(79093337900547, 184936390579327);
#extended_gcd(7909333427900547, 18442936390579327);
extended_gcd(790933342790053068487609780482303435463456908647, 1844684786830956038354072340981232936390579327);

# apply on cryptography later :D


# Least Common Multiple


# Lemma: if M = lcm(a,b) them M = a*b/gcd(a,b);

def lcm(a, b):
  assert a > 0 and b > 0
  d, x, y = extended_gcd(a,b);
  return a*b/d;


# a * x + b * y = c

def diophantine(a, b, c):
	assert c % gcd(a, b) == 0
	(d,x,y) = extended_gcd(a,b);
	r = c / d;
	if a > b:
		return (r*x,r*y);
	if a <= b:
		return (r*y, r*x);


# Modular Division:
# a/b mod n -> bx = a mod n;

def divide(a, b, n):
  assert n > 1 and a > 0 and extended_gcd(a, n)[0] == 1
  (t,s) = diophantine(n,a,1);
  # return the number x s.t. x = b / a (mod n) and 0 <= x <= n-1.
  x = (b*s) % n;
  return x;



# find r such r = r1 mod n1 and r = r2 mod n2
# and 0 < r < n1*n2
# n1*x+n2*y = 1
# so, n1*x*r2 + n2*y*r1 = r

def ChineseRemainderTheorem(n1, r1, n2, r2):
  (x, y) = diophantine(n1, n2, 1);
  n = r2*x*n1 + r1*y*n2;
  m = n1*n2;
  r = (n % m + m) % m;
  print(r);
  return r;

ChineseRemainderTheorem(11, 3, 17, 7);
ChineseRemainderTheorem(17,3,101,97);
ChineseRemainderTheorem(17,3,101,58);




# b**(2**(k)) = ? mod m

def FastModular2Exponentiation(b, k, m):
  # your code here
  bi = b;
  for i in range(k):
    bi = (bi**2) % m;
  
  return bi


# b**e = ? mod m
# e = sum[(1,0)*(2**i)]
# b**e = prod[b**(2**i)]
# (prod ri) mod m = prod (ri mod m); 

def FastModularExponentiation(b, e, m):
  # your code here
  bi = 1;
  k = [int(x) for x in bin(e)[2:]];
  k.reverse();
  for i in range(len(k)):
    if k[i] != 0:
      a = FastModular2Exponentiation(b,i,m);
      bi = (a*bi) % m;
  print(bi);
  return bi


FastModularExponentiation(34,60,77)