# Check if strings are permutaiton of each other. Can add extra to check if lengths are the same.
def CheckPermutation(s,t):
	for i in s:
		if t.find(i)== -1 :
			return False
		else:
			t = t.replace(i,'!',1)
	for i in t:
		if i!="!":
			return False
	return True


s = "ABCDEFGGGG"
t = "BCDFAGGG"
#print(CheckPermutation(s,t))

#Replace spaces
def ReplaceSpaces(s):
	s = s.split(" ")
	t=""
	t=t+s[0]
	for i in range(1,len(s)):
		t = t+ "%20" +s[i]
	return t

#print(ReplaceSpaces("You are an idiot"))

#OneAway
#Assume s is larger than t so only need to take care of replace and remove
def OneAway(s,t):
	edits = 0
	if len(s)>len(t)+1:
		return False
	j=0
	if len(s)==len(t):
		for i in range(len(s)):
			if s[i] == t[i]:
				continue
		else:
			edits = edits+1
			if edits >1:
				return False
		return True
	else:
		for i in range(len(s)):
			if s[i] == t[i-j]:
				continue
			else:
				edits = edits+1
				if edits >1:
					return False
				j = 1
		return True

#print(OneAway("pale","bale"))

#String Compression

def ContinuousOccurence(s,index):
	ctr = 0
	for i in range(index,len(s)):
		#print s[i]
		if s[i] == s[index]:
			ctr = ctr+1
		else:
			return ctr
	return ctr


def StringComp(s):
	n = len(s)
	i = 0
	ctr = 0
	j = 0
	time = 0
	T = n
	while j <  T:
		#print(s)
		ctr = ContinuousOccurence(s,2*time)
		time = time+1
		s = s[:j+1] + str(ctr) + s[j+ctr:]
		j = 2*time
		T = T - ctr+2
	return s

#print(StringComp("ABBDDDDCCCEESSSSSS"))

#check palindrome
def palindrom(a):
	a = sorted(a)
	n = len(a)
	ctr = 0
	if n%2!= 0:
		for i in range(1,n-1):
			if a[i]!= a[i+1] and a[i]!=a[i-1]:
				a = a[:i]+a[i+1:]
				break
				
	for i in range(n/2):
		if a[2*i] != a[2*i + 1]:
			return False

	return True

#print(palindrom("abcdefcba"))

#Rotate Matrix
def Rotate(M,N):
	if N%2==0:
		T = N/2
	else:
		T = N/2+1
	for i in range(N/2):
		for j in range(T):
			temp = M[i][j]
			M[i][j] = M[N-1-j][i]
			M[N-1-j][i] = M[N-1-i][N-1-j]
			M[N-1-i][N-1-j] = M[j][N-1-i]
			M[j][N-1-i] = temp 
	return M
M = [[1,3,5,2],[2,4,6,9],[3,7,9,1],[5,6,7,8]]
#print(Rotate(M,4))





