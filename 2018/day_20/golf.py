import sys
b={}
m={}
d=n=x=y=t=0
while 1:
 if t:x,y,n,t=b[d]
 n=m[x,y]=min(m.get((x,y),9e9),n);c=sys.stdin.read(1)
 if c=='$':break
 if c=='(':d+=1;b[d]=x,y,n,0
 d-=c==')';t=c=='|';y+={'N':1,'S':-1}.get(c,0);x+={'E':1,'W':-1}.get(c,0);n+=1
p=print
v=m.values()
p(max(v))
p(sum(x>999 for x in v))
