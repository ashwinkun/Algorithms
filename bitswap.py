def bitswap(num,i,j):
	if (num>>i)&1 != (num>>j)&1:
		print (num ^ ((1<<i)|(1<<j)))
	print num

bitswap(12,1,2)