def answer(digest):
    # your code here
	prev = 0
	message = []
	for index, num in enumerate(digest):
		if index == 0: # message[-1] = 0
			message.append(step(num,0))
		else:
			message.append(step(num,message[-1]))

	return message
	
def step(digest,prev_m):
    # 129 * message[i] = digest[i] XOR message[i-1]) + k * 256
	k = 0
	while True:
		rem = ((digest ^ prev_m) + k * 256) % 129
		if rem == 0:
			return ((digest ^ prev_m) + k * 256) / 129
		else:
			k = k + 1