def c(f):
 l=[*map(lambda m:[*map(int,''.join([c if 47<ord(c)<58else' 'for c in m]).split())][1:],f)];q,v=[0],{0}
 while q:
  p=q.pop()
  for r in l[p]:
   if{r}-v:v|={r};q+=l[p]
 print(len(v))