import json,os,urllib.request as U
V=[0,100,320,330,500,900,0]
PS=[[0]*128 for _ in range(15)]
for p in range(1,15):
 t=p&7
 if t>6:continue
 for r in range(8):
  for f in range(8):
   s=r*16+f;rm=r if p<8 else 7-r
   if t==1:q=(6-rm)*6
   elif t==6:q=2*rm-2
   else:q=14-(abs(2*f-7)+abs(2*r-7))
   PS[p][s]=V[t]+q if p<8 else -V[t]-q
B=[0]*128;K=[0,0];sd=ct=ep=sc=nd=0;TT={};BM=0
CM={112:13,119:14,116:12,0:7,7:11,4:3}
ND=[-33,-31,-18,-14,14,18,31,33];KD=[-17,-16,-15,-1,1,15,16,17];BD=[-17,-15,15,17];RD=[-16,-1,1,16]
LIM=40000
def FT(m):return m&127,(m>>7)&127,m>>14
def A(x,by):
 for o in(15,17):
  y=x-o if by else x+o
  if not y&0x88 and B[y]==1|(by<<3):return 1
 for ds,n in((ND,2),(KD,6)):
  for o in ds:
   y=x+o
   if not y&0x88 and B[y]==n|(by<<3):return 1
 for i2,o in enumerate(KD):
  ts=(3,5)if i2 in(0,2,5,7)else(4,5)
  y=x+o
  while not y&0x88:
   q=B[y]
   if q:
    if q>>3==by and(q&7)in ts:return 1
    break
   y+=o
 return 0
def PM(ap,i,j):
 for pr in(5,4,3,2):ap(i|j<<7|pr<<14)
def Gn(cp):
 ms=[];ap=ms.append;c=sd
 for i in range(128):
  if i&0x88:continue
  p=B[i]
  if not p or p>>3!=c:continue
  t=p&7
  if t==1:
   d=-16+32*c;r7=1+5*c;st=6-5*c
   for o in(d-1,d+1):
    j=i+o
    if j&0x88:continue
    q=B[j]
    if q and q>>3!=c:
     if(i>>4)==r7:PM(ap,i,j)
     else:ap(i|j<<7)
    elif j==ep:ap(i|j<<7)
   j=i+d
   if not B[j]:
    if(i>>4)==r7:PM(ap,i,j)
    elif not cp:
     ap(i|j<<7)
     if(i>>4)==st and not B[i+2*d]:ap(i|(i+2*d)<<7)
  else:
   D=ND if t==2 else BD if t==3 else RD if t==4 else KD
   for o in D:
    j=i+o
    while not j&0x88:
     q=B[j]
     if q:
      if q>>3!=c:ap(i|j<<7)
      break
     if not cp:ap(i|j<<7)
     if t in(2,6):break
     j+=o
   if t==6 and not cp and i==(116 if c==0 else 4):
    for bt,sg in((1,1),(2,-1))if c==0 else((4,1),(8,-1)):
     if ct&bt and all(not B[i+k]for k in(sg,2*sg))and(sg>0 or not B[i-3])and all(not A(i+k,c^1)for k in(0,sg,2*sg)):ap(i|(i+2*sg)<<7)
 return ms
def mk(m):
 global sd,ct,ep,sc
 st=(B[:],ct,ep,sc,K[0],K[1])
 f,t,pr=FT(m);p=B[f];v=B[t];c=sd;ep=-1
 if(p&7)==1 and t==st[2] and not v and(f&7)!=(t&7):
  y=t+16-32*c;sc-=PS[B[y]][y];B[y]=0
 elif v:sc-=PS[v][t]
 B[f]=0;B[t]=p;sc+=PS[p][t]-PS[p][f]
 if(p&7)==1:
  if pr:
   w=pr|(c<<3);B[t]=w;sc+=PS[w][t]-PS[p][t]
  elif abs(t-f)==32:ep=(f+t)//2
 elif(p&7)==6:
  K[c]=t
  if abs(t-f)==2:
   rf,rt=(t+1,t-1)if t>f else(t-2,t+1);r=B[rf];B[rt]=r;B[rf]=0;sc+=PS[r][rt]-PS[r][rf]
 ct&=CM.get(f,15)&CM.get(t,15);sd^=1
 return st
def um(st):
 global sd,ct,ep,sc
 B[:]=st[0];ct,ep,sc,K[0],K[1]=st[1],st[2],st[3],st[4],st[5];sd^=1
def Sr(d,a,b,ply):
 global nd,BM
 ic=A(K[sd],sd^1);qs=d<=0
 if qs:
  if not ic:
   s=sc if sd==0 else -sc
   if s>=b:return s
   if s>a:a=s
 else:
  k=bytes(B)+bytes((sd,ct));e=TT.get(k)
  if e and ply and e[0]>=d:return e[1]
 nd+=1
 if nd>LIM:raise Exception
 ms=Gn(1 if qs and not ic else 0);ms.sort(key=lambda m:V[B[m&127]&7]-10*V[B[(m>>7)&127]&7]if B[(m>>7)&127]else 0);bst=-10**9;bm=0
 for m in ms:
  st=mk(m)
  if A(K[sd^1],sd):um(st);continue
  s=-Sr(d-1,-b,-a,ply+1);um(st)
  if s>bst:bst=s;bm=m
  if s>a:a=s
  if a>=b:break
 if qs:return(bst if bst>-10**9 else -100000+ply)if ic else a
 if not bm:return -100000+ply if ic else 0
 TT[k]=(d,bst)
 if ply==0:BM=bm
 return bst
def Rs():
 global sd,ct,ep,sc
 B[:]=[0]*128;sc=0
 for f,w in enumerate((12,10,11,13,14,11,10,12)):
  for s,p in((f,w),(16+f,9),(96+f,1),(112+f,w-8)):
   B[s]=p;sc+=PS[p][s]
 K[0]=116;K[1]=4;sd=0;ct=15;ep=-1
def Uc(m):
 f,t,pr=FT(m);s='%c%d%c%d'%(97+(f&7),8-(f>>4),97+(t&7),8-(t>>4))
 if pr:s+='nbrq'[pr-2]
 return s
def Po(p,b):
 q=U.Request(os.environ['MAKEFUN_ENV_URL']+p,data=json.dumps(b).encode())
 return json.load(U.urlopen(q))
if __name__=='__main__':
 while 1:
  g=Po('/game',{})
  if g['status']=='done':break
  if g['status']=='over':continue
  Rs();TT.clear()
  for u in g['moves']:mk({Uc(m):m for m in Gn(0)}[u])
  nd=0
  try:
   for d in range(1,64):Sr(d,-10**9,10**9,0)
  except Exception:pass
  w=Uc(BM)
  if w not in g['legal_moves']:w=g['legal_moves'][0]
  Po('/move',{'game':g['game'],'move':w})
