from console import clear

#355
def Naga(n):
	H=[1,2,4,8]
	k=0 #changing k and H temporarily
	while H:
		#clear();
		print(H)
		A=[H[:]]
		i=-1
		while A[-1][-1]>1:
			j=-1
			p=A[-1][j]
			B=[]
			for l in range(len(H)):
				m=-l-1
				B=[0]+B
				a=A[-1][m]
				if 0<a<p:
					B[j]=p-a
					if j==-1:i=m
					j=m
					p=a
			A+=[B]
			print(B)
		#input()
		k+=1
		D=[a[-1]-a[i]-1 for a in A[:-1]]
		h=H.pop()
		if h>1:
			print(D);input()
			A[1].pop()
			i+=1
			for _ in range(k):
				C=H[i:]
				for j in range(len(C)):
					if (_ or j) and A[1][i:][j]:
						for m in range(len(D)-1):D[m]+=D[m+1]
					C[j]+=D[0]
				H+=C
	return k

Naga(2)
