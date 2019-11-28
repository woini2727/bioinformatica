import numpy as np

def Ins(x):
  return -2

def Del(x):
  return -2

def Sub(x, y):
  return 2 if x == y else -1

def NWScore(X, Y):
  score = [[0] * (1 + len(Y)) for _ in range(0, len(X) + 1)]
 
  for j in range(1, len(Y) + 1):
    score[0][j] = score[0][j-1] + Ins(Y[j-1])
 
  for i in range(1, len(X) + 1): #init array
      score[i][0] = score[i-1][0] + Del(X[i-1])
      for j in range(1, len(Y) + 1):
        scoreSub = score[i-1][j-1] + Sub(X[i-1], Y[j-1])
        scoreDel = score[i-1][j] + Del(X[i-1])
        scoreIns = score[i][j-1] + Ins(Y[j-1])
        score[i][j] = max(scoreSub, scoreDel, scoreIns)

  return score[-1]

def rev(s):
  return s[::-1]

def Diagonal(n1,n2,pt):
    if(n1 == n2):
        return pt['MATCH']
    else:
        return pt['MISMATCH']

#------------------------------------------------------------  
#This function gets the optional elements of the aligment matrix and returns the elements for the pointers matrix.
def Pointers(di,ho,ve):

    pointer = max(di,ho,ve) #based on python default maximum(return the first element).

    if(di == pointer):
        return 'D'
    elif(ho == pointer):
        return 'H'
    else:
         return 'V'  

def NeedlemanWunsch(s1,s2,match = 1,mismatch = -1, gap = -2):
    penalty = {'MATCH': match, 'MISMATCH': mismatch, 'GAP': gap} #A dictionary for all the penalty valuse.
    n = len(s1) + 1 #The dimension of the matrix columns.
    m = len(s2) + 1 #The dimension of the matrix rows.
    al_mat = np.zeros((m,n),dtype = int) #Initializes the alighment matrix with zeros.
    p_mat = np.zeros((m,n),dtype = str) #Initializes the alighment matrix with zeros.
    #Scans all the first rows element in the matrix and fill it with "gap penalty"
    for i in range(m):
        al_mat[i][0] = penalty['GAP'] * i
        p_mat[i][0] = 'V'
    #Scans all the first columns element in the matrix and fill it with "gap penalty"
    for j in range (n):
        al_mat[0][j] = penalty['GAP'] * j
        p_mat [0][j] = 'H'
    #Fill the matrix with the correct values.

    p_mat [0][0] = 0 #Return the first element of the pointer matrix back to 0.
    for i in range(1,m):
        for j in range(1,n):
            di = al_mat[i-1][j-1] + Diagonal(s1[j-1],s2[i-1],penalty) #The value for match/mismatch -  diagonal.
            ho = al_mat[i][j-1] + penalty['GAP'] #The value for gap - horizontal.(from the left cell)
            ve = al_mat[i-1][j] + penalty['GAP'] #The value for gap - vertical.(from the upper cell)
            al_mat[i][j] = max(di,ho,ve) #Fill the matrix with the maximal value.(based on the python default maximum)
            p_mat[i][j] = Pointers(di,ho,ve)

    ret = []
    for i in range(m):
      ret.append(max([ al_mat[i][j] for j in range(n) ]))

    return ret

def find_max_pos(score1,score2):
    pts = [s1 + s2 for s1, s2 in zip(score1, score2)]
    maximo = max(pts[::-1])
    pos = pts.index(maximo)
    return pos

def Hirschberg(X,Y, ret = []):
  #print(X, Y)
  ret.append((X, Y))

  Z = ""
  W = ""
  if len(X) == 0:
    for y in Y:
      Z += '-'
      W += y
  elif len(Y) == 0:
    for x in X:
      Z += x
      W += '-'
  elif len(X) == 1 or len(Y) == 1:
    Z, W = NeedlemanWunsch(X, Y)
  else:
    xmid = len(X)//2
    Xl = X[:xmid]
    Xr = X[xmid:]

    ScoreL = NWScore(Xl, Y)
    ScoreR = NWScore(rev(Xr), rev(Y))
    ymid = find_max_pos(ScoreL, rev(ScoreR))

    Yl = Y[:ymid]
    Yr = Y[ymid:]

    Z, W = Hirschberg(Xr, Yr, ret)
    z, w = Hirschberg(Xl, Yl, ret)

    if(type(w) == str and type(z) == str):
      return (w, z)
   
    Z += z
    W += w

  return (Z, W)

ret = []
print(Hirschberg("AGTACGCA", "TATGC", ret))
print(ret)

