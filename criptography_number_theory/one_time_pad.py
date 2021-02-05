from functools import reduce

def to16(s):
	l = [];
	for ch in s:
		hc = hex(ord(ch)).replace('0x','');
		if len(hc) == 1:
			hc = '0' + hc;
		l.append(hc);

	return reduce(lambda x, y : (x+y), l);

def tostr(s):
	return s and chr(int(s[:2], base = 16)) + tostr(s[2:]) or '';


message = 'hello world'
print('hello world: ', to16(message));
print('reconverter: ', tostr(to16(message)));


def xor(s1, s2):
	res = '';
	for i in range(len(s1)):
		res += format(int(s1[i], 16) ^ int(s2[i], 16), '01x');
	return res;

message = 'secret message';
mess16  = to16(message);
key     = 'top secret key';
key16   = to16(key);
cipher  = xor(mess16,key16);
decipher= xor(cipher, key16);
dec_mess= tostr(decipher);
print("message: ", message );
print("hex    : ", mess16  );
print("key    : ", key     );
print("hex    : ", key16   );
print("cipher : ", cipher  );
print("recover: ", dec_mess);

mess2   = 'anothermessage';
mess216 = to16(mess2);
cipher2 = xor(mess216, key16);

print("xor ciphers : ", xor(cipher, cipher2));
print("xor messages: ", xor(mess16, mess216));



m1 = to16('steal the secret');
m2 = to16('the boy the girl');
k1 = to16('super secret key');
xor_mess = xor(m1, m2);



def guess(substr, xor_mess):
	nice_guess = [];
	mlen = int((len(xor_mess)+1)/2);
	slen = len(substr);
	for pos in range(mlen - slen + 1):
		before_pad = chr(0)*pos;
		after_pad  = chr(0)*(mlen-slen-pos);
		substr_pad  = before_pad + substr + after_pad;
		guess = to16(substr_pad);
		other_mpart = tostr(xor(guess,xor_mess))[pos:(pos+slen)];
		good_guess = True;

		for i in range(len(other_mpart)):
			if not other_mpart[i].isalpha() and not other_mpart[i].isspace():
				good_guess = False;
				break;
		if good_guess:
			nice_guess.append((guess, pos, other_mpart));
	print('\nGood guesses:')
	for guess in nice_guess:
		print("position: %d, one message part: \"%s\", another message part: \"%s\"" % (guess[1], substr, guess[2]) );

guess(" the ", xor_mess);



