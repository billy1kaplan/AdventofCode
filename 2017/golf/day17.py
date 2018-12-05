def f(s,b=[0],p=-1,t=2018):
 for i in range(1,t):p=(p+s+1)%i;b.insert(p+1,i)
 return b[(p+2)%t]

def g(s,i=0,p=-1):
 for j in range(1,5*10**7):p=(p+s+1)%j;i=(j,i)[p>0]
 return i