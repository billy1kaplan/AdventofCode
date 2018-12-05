def f(n,p=[*'abcdefghijklmnop']):
 for m in n.split(','):
  if's'==m[0]:i=-int(m[1:]);p=p[i:]+p[:i]
  else:i,j=map((int,p.index)['x'>m[0]],m[1:].split('/'));p[i],p[j]=p[j],p[i]
 print(''.join(p))