import sys
import collections as z
b={}
m=z.defaultdict(lambda:float('inf'))
d=n=x=y=0
t=0
while 1:
 if t:
  x,y,n=b[d]
  t=0
 n=m[x,y]=min(m[x,y],n)
 c=sys.stdin.read(1)
 if c=='$':break
 if c=='(':
  d+=1
  b[d]=x,y,n
 d-=c==')'
 t=c=='|'
 y+={'N':1,'S':-1}.get(c,0)
 x+={'E':1,'W':-1}.get(c,0)
 n+=1
p=print
p(max(m.items(),key=lambda x:x[1])[1])
p(len([k for k,v in m.items() if v>999]))
