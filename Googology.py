from time import sleep
from console import clear
def step(data,sweep=True,wait=0):
	if sweep: clear()
	print(data)
	if wait: sleep(wait)
	else: input()
#the length difference from factoring an expression S is (k-1)(n-1)-3.
#k is the number of occurrences of S and n is the length of S


#simplified Ackermann function: ω, 41
s=lambda m,n:n+2if m*n<1else s(m-1,s(m,n-1))


#Ackermann function: ω, 55
Ack=lambda m,n:n+1if m<1else Ack(m-1,1if n<1else Ack(m,n-1))


#Finite Fast-growing hierarchy: ω, 58
def f(a,n):
	if a:
		t=n
		for _ in range(n):t=f(a-1,t)
		return t
	return n+1


#Hyperoperations: ω, 64
H=lambda n,a,b:([b+1,a,0]+[1]*n)[n]if n*b<1else H(n-1,a,H(n,a,b-1))


#Baby hydras: ω, 65
def babyHydra(n):
	H=[n]
	k=0
	while H:
		k+=1
		h=H.pop()
		if h:H+=[h-1]*k
	return k


#Friedmann's vectors: ω, 80
def VR(V):
	k=0
	while sum(V[:-1]):
		i=-2
		while V[i]<1:i-=1
		V[i+1]=sum(V)
		V[i]-=1
		k+=1
	return k


#Laver tables: ??, 145
def q(n):
	m=0
	t=1
	while t<2**n:
		m+=1
		r=range(1,2**m)
		L=[[i]for i in r]+[[0]]
		for S in L[::-1]:
			for i in r:S+=[L[S[-1]][S[0]]]
		while 2**m//t*L[0][:t]!=L[0]:t*=2
	return m


#Super Ackermann function: ω^2, 83
def AA(a,b,c):
	if b:return AA(a,b-1,1 if c<1 else AA(a,b,c-1))
	return c+1 if a<1 else AA(a-1,c,0)


#Chained arrows: ω^2, 111
def C(X):
	if 1in X:X=X[:X.index(1)]
	q=X[-1]
	L=len(X)
	if L>2:X[-2]-=1
	return[q,X[0]**q][L-1]if L<3else C(X[:-2]+[C(X),q-1])


#Taro's multivariable Ackermann function: ω^ω, 115
def Taro(A):
	while any(A[1:]):
		i=1
		while A[i]<1:i+=1
		a=A[0]
		A[i-1]=a if i>1else 1if a<1else Taro([a-1]+A[1:])
		A[i]-=1
	return A[0]+1


#Linear BEAF: ω^ω, 129
def BEAF(A):
	b=A[0]
	if A[1]-1:
		while[a for a in A[2:]if a-1]:
			A[1]-=1
			t=BEAF(A)
			i=1
			while A[i+1]<2:
				A[i]=b
				i+=1
			A[i]=t
			A[i+1]-=1
		return b**A[1]
	return b


#Block subsequence: ω^ω, 255
def n(k):
	def F(s):
		def S(a,b):
			i=0
			l=len(a)
			for s in b:i+=a[i%l]==s
			return i>=l
		c=[s[i:2*i+2]for i in range(len(s)//2)]
		return 1not in[S(c[i],j)for i in range(len(c))for j in c[i+1:]]
	M=lambda l:[[]]if l<1else[m+[i]for i in range(k)for m in M(l-1)]
	L=1
	while 1in[F(s)for s in M(L)]:L+=1
	return L-1


#Tame fusible margins: ε_0, 60
def m1(n):
	m=lambda x:-x if x<0 else m(x-m(x-1))/2
	return int(1/m(n))


#Kirby-Paris hydras: ε_0, 95
def Hydra(n):
	H=list(range(n+1))
	k=0
	while H:
		k+=1
		h=H.pop()
		if h:
			i=-1
			while H[i]>=h:i-=1
			H[i:]*=k+1
	return k


#Beklemishev worms: ε_0, 96
def Worm(n):
	k=1
	w=[n]
	while w:
		k+=1
		h=w.pop()
		if h:
			t=[h-1]
			while w and h<=w[-1]:t=[w.pop()]+t
			w+=t*k
	return k-1


#Goodstein sequences: ε_0, 106
def G(n):
	b=2
	def P(x):
		p=0
		while b*b**p<=x:p+=1
		return 0if x<1else(b+1)**P(p)+P(x-b**p)
	while n:
		n=P(n)-1
		b+=1
	return b-2


#My difference sequences: φ(ω,0), 113
def Wavern(n):
	W=[0,n]
	k=0
	while W:
		k+=1
		h=W.pop()
		if h:
			i=-1
			while W[i]>=h:i-=1
			h-=W[i]+1
			for _ in range(-i*k):W+=[W[i]+h]
	return k


#Medium hydras: Γ_0, 205
def mediumHydra(n):
	w=list(range(n))
	k=0
	while w:
		k+=1
		h=w.pop()
		if h:
			l=len(w)
			i=l-1
			while h<=w[i]:i-=1
			if max(w[i:])<=h:
				L=l-i
				j=i-1
				N=True
				while w[j]>h-2 and N:
					if w[j]<h:
						N=i-j>L or max(w[j:i])>h
						if N:i=j
					j-=1
				if N:i=j+1
			w+=w[i:]*k
	return k


#Super hydras: ψ(Ω_ω), 183
def superHydra(n):
	H=[0,1,n]
	k=0
	while H:
		k+=1
		h=H.pop()
		if h:
			i=-1
			while H[i]>=h:i-=1
			d=h-H[i]
			if d>1:
				j=i
				while not 0<H[i]-H[j]<d:
					i=j
					while H[j]>=H[i]:j-=1
				d=h-H[i]
			for _ in range(-i*k):H+=[H[i]+d-1]
	return k


#Buchholz hydras: ψ(ε_(Ω_ω+1)), 233
def BH(n):
	k=0
	H=[]
	for i in range(n-1):H+=[i<1,i]
	while H:
		k+=1
		d=H.pop()
		u=H.pop()
		if d:
			l=len(H)
			i=l-2
			while not(H[i+1]<d and u<2 or 0<H[i]<u):i-=2
			H+=[[k+2,d],H[i:]*k,[u-1,d]+H[i+2:]+[1,d]][min(2,u)]
			for j in range(l+3,(u>1)*len(H),2):H[j]+=d-H[i+1]
	return k
