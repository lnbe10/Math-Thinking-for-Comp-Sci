# 

def ConvertToInt(message_str):
  res = 0
  for i in range(len(message_str)):
    res = res * 256 + ord(message_str[i])
  return res


def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]

#def ConvertToInt(message):
# 	return int("".join(bin(ord(x))[2:] for x in message),2);


# def ConvertToStr(inteiro):
# 	bin_data = bin(inteiro)[2:];
# 	str_data = "";
# 	i=0;
# 	while i < len(bin_data):
# 		if bin_data[i:i+6] == '100000':
# 			str_data = str_data + " ";
# 			i += 6;
# 		else:
# 			temp_data = int(bin_data[i:i + 7], 2);
# 			str_data = str_data + chr(temp_data);
# 			i += 7;
# 	return str_data;


message = "ok boomer"
print(message);
print(ConvertToStr(ConvertToInt(message)));

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


# FME = Fast Modular Exponentiation
def FME(b, e, m):
  # your code here
  bi = 1;
  k = [int(x) for x in bin(e)[2:]];
  k.reverse();
  for i in range(len(k)):
    if k[i] != 0:
      a = FastModular2Exponentiation(b,i,m);
      bi = (a*bi) % m;
  return bi

def GCD(a, b):
  if b == 0:
    return a;
  return GCD(b, a % b);

def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0);
    (x, y) = ExtendedEuclid(b, a % b);
    k = a // b;
    return (y, x - k * y);

def ChineseRemainderTheorem(n1, r1, n2, r2):
  (x, y) = ExtendedEuclid(n1, n2);
  return ((r2 * x * n1 + r1 * y * n2) % (n1 * n2) + (n1 * n2)) % (n1 * n2);

def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b

# Public  Key E -> (n,e)
# Private Key D -> (p,q)

# message = int(message);
# n = p*q
# e <- (p-1)*(q-1)
# cypher = message**e mod n
# message = cypher**d mod n
# e*d = 1 mod (p-1)*(q-1)
# cypher = str(cypher);

def Encrypt(message, modulo, exponent):
  return FME(ConvertToInt(message), exponent, modulo);

def Decrypt(ciphertext, p, q, exponent):
  n = p*q;
  d = InvertModulo(exponent, (p-1)*(q-1));
  return ConvertToStr(FME(ciphertext, d, n));
  

p = 1000000007;
q = 1000000009;
exponent = 23917;
modulo = p * q;
ciphertext = Encrypt("attack", modulo, exponent);
message = Decrypt(ciphertext, p, q, exponent);

# if we know the possible messages that will be sent with the encryption
# keys, we know their results and we can compare the sent message with
# possible encriptions!!

print("Known message guess");

def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
  for pot in potential_messages:
    if ciphertext == Encrypt(pot, modulo, exponent):
      return pot;
  return "don't know";

p = 1000000007;
q = 1000000009;
exponent = 23917;
modulo = p * q;
ciphertext = Encrypt("don't attack", modulo, exponent);
DecipherSimple(ciphertext, modulo, exponent, ["attack", "don't attack", "wait"]);


# if someone generate n = p*q with small p or small q
# we can brute-force search the small_prime and them get
# the private key!!
# some devices have problems in random generation of primes
# that make them spill out same primes multiple times :D
# so one could be unsafe not knowing this .-.

print('Small prime attack')

def DecipherSmallPrime(ciphertext, modulo, exponent):
  for i in range(2,10**6):
  	# with a list of primes it's quickier .-.
    if modulo % i == 0:
      small_prime = i;
      big_prime = modulo // i;
      return Decrypt(ciphertext, small_prime, big_prime, exponent);
  
  return "don't know";
  
modulo = 101 * 18298970732541109011012304219376080251334480295537316123696052970419466495220522723330315111017831737980079504337868198011077274303193766040393009648852841770668239779097280026631944319501437547002412556176186750790476901358334138818777298389724049250700606462316428106882097210008142941838672676714188593227684360287806974345181893018133710957167334490627178666071809992955566020058374505477745993383434501768887090900283569055646901291270870833498474402084748161755197005050874785474707550376333429671113753137201128897550014524209754619355308207537703754006699795711188492048286436285518105948050401762394690148387;
exponent = 239;
ciphertext = Encrypt("attack", modulo, exponent);
DecipherSmallPrime(ciphertext, modulo, exponent);


# with q<p, if p-q is small, we can reduce the search for q
# to a minimal interval and brute-force search q
print('Small difference attack');

def IntSqrt(n):
  low = 1;
  high = n;
  iterations = 0;
  while low < high and iterations < 5000:
    iterations += 1;
    mid = (low + high + 1) // 2;
    if mid * mid <= n:
      low = mid;
    else:
      high = mid - 1;
  return low;


def DecipherSmallDiff(ciphertext, modulo, exponent):
  # n = p*q, p>q
  # q<sqrt(n)<p
  # sqrt(n)-q < p-q = r
  # sqrt(n)-r < q < sqrt(n) 
  r = 5000;
  sn = IntSqrt(modulo);
  for i in range(sn-r,sn+1):
    if modulo % i == 0:
      small_prime = i;
      big_prime = modulo // small_prime;
      return Decrypt(ciphertext, small_prime, big_prime, exponent);
  return ("no results bro");

p = 1000000007;
q = 1000000009;
n = p * q;
e = 239;
ciphertext = Encrypt("attack", n, e);
message = DecipherSmallDiff(ciphertext, n, e);



# insufficient randomness in prime generation can make one of the prime
# factor an easy guess

print('Insufficient randomness attack')

def DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo, second_exponent):
  common_prime = GCD(first_modulo, second_modulo);
  if common_prime > 1:
    q1 = first_modulo // common_prime;
    q2 = second_modulo // common_prime;
    return (Decrypt(first_ciphertext, common_prime, q1, first_exponent), Decrypt(second_ciphertext, common_prime, q2, second_exponent));
  return ("unknown message 1", "unknown message 2");
  
# Example usage with common prime p and different second primes q1 and q2  
p = 101;
q1 = 18298970732541109011012304219376080251334480295537316123696052970419466495220522723330315111017831737980079504337868198011077274303193766040393009648852841770668239779097280026631944319501437547002412556176186750790476901358334138818777298389724049250700606462316428106882097210008142941838672676714188593227684360287806974345181893018133710957167334490627178666071809992955566020058374505477745993383434501768887090900283569055646901291270870833498474402084748161755197005050874785474707550376333429671113753137201128897550014524209754619355308207537703754006699795711188492048286436285518105948050401762394690148387;
q2 = 1000000007;
first_modulo = p * q1;
second_modulo = p * q2;
first_exponent = 239;
second_exponent = 101;
first_ciphertext = Encrypt("attack", first_modulo, first_exponent);
second_ciphertext = Encrypt("caraio burracha", second_modulo, second_exponent);
m = DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo, second_exponent);
for message in m:
	print(message);

# if someone uses the same exponent for the same message to two or more
# people, one can guess the message not knowing the prime factorization
# of the private key!!!!


print('Hastad attack: same message and exponent to various messages')

def DecipherHastad(first_ciphertext, first_modulo, second_ciphertext, second_modulo):
  # c = c1 mod n1, c = c2 mod n2, c = c3 mod n3
  # 0 < c < n1*n2
  # m = m mod n1, m = m mod n2
  # 0 < m² < n1*n2
  # c = m² mod n1*n2 -> c = m²
  c = ChineseRemainderTheorem(first_modulo, first_ciphertext, second_modulo, second_ciphertext)
  m = IntSqrt(c);
  return ConvertToStr(m);
  

p1 = 790383132652258876190399065097;
q1 = 662503581792812531719955475509;
p2 = 656917682542437675078478868539;
q2 = 1263581691331332127259083713503;
n1 = p1 * q1;
n2 = p2 * q2;
ciphertext1 = Encrypt("deu ruim, descobriram a mensagem", n1, 2);
ciphertext2 = Encrypt("deu ruim, descobriram a mensagem", n2, 2);
message = DecipherHastad(ciphertext1, n1, ciphertext2, n2);
print(message);