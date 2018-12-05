def f(q,z=256):
 s=x=0;*n,=range(z)
 for l in q:n[:l]=n[:l][::-1];x-=l+s;s+=1;exec('n+=n.pop(0),;'*(l+s-1))
 print(n[x%z]*n[-~x%z])