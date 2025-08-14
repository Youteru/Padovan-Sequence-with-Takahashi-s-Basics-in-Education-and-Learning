#O(logN)
#参考文献　https://github.com/E869120/math-algorithm-book/blob/main/codes/python/Code_4_07_1.py
from copy import deepcopy
import math

MOD = 1000000000

# 3×3 行列 A, B の積をMODで割った余りを返す関数
def Mmultiply(A, B):
	global MOD
	C = [ [ 0, 0 ,0], [ 0, 0 ,0],[0,0,0] ]
	for i in range(3):
		for j in range(3):
			for k in range(3):
				C[i][j] += A[i][k] * B[k][j]
				C[i][j] %= MOD
	return C

# A の n 乗を返す関数
def Mpower(A, n):
	P = deepcopy(A)
	Q = [ [ 0, 0,0 ], [ 0, 0,0 ] ,[0,0,0]]
	flag = False
	for i in range(math.floor(math.log2(n))+2):
		if (n & (1 << i)) != 0:
			if flag == False:
				Q = deepcopy(P)
				flag = True
			else:
				Q = deepcopy(Mmultiply(Q, P))
		P = deepcopy(Mmultiply(P, P))
	return Q
# 3×3 行列 A, B の積をMODで割った余りを返す関数
def multiply(A, B) :
	C = [ [ 0, 0 ,0], [ 0, 0 ,0],[0,0,0] ]
	for i in range(3):
		for j in range(3):
			for k in range(3):
				C[i][j] += A[i][k] * B[k][j]
	return C

# A の n 乗を返す関数
def power(A, n):
	P = deepcopy(A)
	Q = [ [ 0, 0,0 ], [ 0, 0,0 ] ,[0,0,0]]
	flag = False
	for i in range(math.floor(math.log2(n))+1):
		if (n & (1 << i)) != 0:
			if flag == False:
				Q = deepcopy(P)
				flag = True
			else:
				Q = deepcopy(multiply(Q, P))
		P = deepcopy(multiply(P, P))
	return Q
#N番目のパドヴァン数列を求めます。-70428<=N<=35211
def padovan(N) :
    if N>-5 :
        A = [ [ 0,1,0], [ 0,0,1] ,[1,1,0]]
        B = power(A, N +5)
        # A**N=[[P(N-5),P(n-3),P(n-4)],[P(N-4),P(n-2),P(n-3)],[P(N-3),P(n-1),P(n-2)]
        return B[0][0]
    elif N<-5 :
        A = [ [ -1,0,1], [ 1,0,0] ,[0,1,0]]
        B = power(A, -N -5)
        return B[0][0] 
    else :
        return 1
#N番目のパドヴァン数列をMODで割った余りを求めます。
def Mpadovan(N) :
    if N>-5 :
        A = [ [ 0,1,0], [ 0,0,1] ,[1,1,0]]
        B = Mpower(A, N +5)
        # A**N=[[P(N-5),P(n-3),P(n-4)],[P(N-4),P(n-2),P(n-3)],[P(N-3),P(n-1),P(n-2)]
        return B[0][0]
    elif N<-5 :
        A = [ [ -1,0,1], [ 1,0,0] ,[0,1,0]]
        B = Mpower(A, -N -5)
        return B[0][0]
    else :
        return 1

N=int(input())
print(Mpadovan(N))

    
