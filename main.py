import json,os,urllib.request as U
V=[0,100,320,330,500,900,0]
TB=["","<<<<>AA2>:7<<<<F>>AHAAFKTTTT<<<<",
"#(--(2<>->AC-<CF->CF-<AC(2<<#(--",
"27777><<7AAA7<AA7>>A7<>A7<<<2777",
"<<<>:<<<:<<<:<<<:<<<:<<<>AAA<<<<",
"277:7<><7>>><<>>:<>>7<>>7<<<277:",
"HMC>HH>>94444//*/**%/**%/**%/**%"]
PS=[[0]*128 for _ in range(15)]
for t in range(1,7):
 for j,s in enumerate(TB[t]):
  r=(j>>2)*16;f=j&3;w=(ord(s)-(62 if t==6 else 60))*2+V[t]
  for q in(r+f,r+7-f):PS[t][q]=w;PS[t+8][q^112]=-w
ND=[-33,-31,-18,-14,14,18,31,33];BD=[-17,-15,15,17];RD=[-16,-1,1,16];KD=sorted(set(BD+RD));DL=[0,0,ND,BD,RD,KD,KD]
CM={0:13,7:14,4:12,112:7,119:11,116:3}
B=[0]*128;K=[0,0];TT={};HC={};A=0
sd=ct=ep=sc=nd=BM=0;LIM=45e3
def Gn(cp):
 ms=[];ap=ms.append;c=sd
 for i in range(128):
  p=B[i]
  if not p or p>>3!=c:continue
  t=p&7
  if t==1:
   d=16-32*c;r=i>>4;pr=6-5*c
   for o in(d-1,d+1):
    j=i+o
    if j&0x88:continue
    q=B[j]
    if q and q>>3!=c:
     if r==pr:
      for w in(5,4,3,2):ap(i|j<<7|w<<14)
     else:ap(i|j<<7)
    elif j==ep:ap(i|j<<7)
   j=i+d
   if not B[j]:
    if r==pr:
     for w in(5,4,3,2):ap(i|j<<7|w<<14)
    elif not cp:
     ap(i|j<<7)
     if r==1+5*c and not B[i+2*d]:ap(i|(i+2*d)<<7)
  else:
   for o in DL[t]:
    j=i+o
    while not j&0x88:
     q=B[j]
     if q:
      if q>>3!=c:ap(i|j<<7)
      break
     if not cp:ap(i|j<<7)
     if t in(2,6):break
     j+=o
   if t==6 and not cp and i==(4 if c==0 else 116):
    for sg,bt in((1,1),(-1,2))if c==0 else((1,4),(-1,8)):
     if ct&bt and not B[i+sg]and not B[i+2*sg]and(sg>0 or not B[i-3])and i not in A and i+sg not in A:ap(i|(i+2*sg)<<7)
 return ms
def mk(m):
 global sd,ct,ep,sc
 f=m&127;t=(m>>7)&127;pr=m>>14;p=B[f];v=B[t];c=sd
 st=(B[:],ct,ep,sc,K[:]);ep=-1
 if (p&7)==1 and t==st[2] and not v and (f&7)!=(t&7):
  y=t-16 if c==0 else t+16;sc-=PS[B[y]][y];B[y]=0
 elif v:sc-=PS[v][t]
 B[f]=0;B[t]=p;sc+=PS[p][t]-PS[p][f]
 if pr:
  w=pr|(c<<3);B[t]=w;sc+=PS[w][t]-PS[p][t]
 elif (p&7)==1 and abs(t-f)==32:ep=(f+t)//2
 if (p&7)==6:
  K[c]=t
  if abs(t-f)==2:
   rf,rt=(t+1,t-1)if t>f else(t-2,t+1);r=B[rf];B[rt]=r;B[rf]=0;sc+=PS[r][rt]-PS[r][rf]
 ct&=CM.get(f,15)&CM.get(t,15);sd^=1
 return st
def um(st):
 global sd,ct,ep,sc
 B[:]=st[0];ct,ep,sc=st[1],st[2],st[3];K[:]=st[4];sd^=1
def S(d,a,b,ply):
 global nd,BM,sd,A
 nd+=1
 if nd>LIM:raise ValueError
 k=bytes(B)+bytes((sd,ct,ep+1))
 if ply and HC.get(k):return 0
 HC[k]=HC.get(k,0)+1
 sd^=1;A={(m>>7)&127 for m in Gn(0)};sd^=1
 ic=K[sd]in A
 if ic:d+=1
 qs=d<=0;tm=0
 if qs and not ic:
  ev=sc*(1-2*sd)
  if ev>=b:HC[k]-=1;return ev
  best=ev;a=max(a,ev);lm=Gn(1)
 else:
  best=-2e5;lm=Gn(0)
 for m in lm:
  if (B[(m>>7)&127]&7)==6:HC[k]-=1;return 2e5-ply
 if not qs:
  e=TT.get(k)
  if e:
   tm=e[2]
   if ply and e[0]>=d and(e[3]==0 or(e[3]==1 and e[1]>=b)or(e[3]==2 and e[1]<=a)):HC[k]-=1;return e[1]
 lm.sort(key=lambda m:9e4 if m==tm else V[v&7]*16-(B[m&127]&7)if(v:=B[(m>>7)&127])else V[m>>14]*16 if m>>14 else 0,reverse=True)
 bm=0;a0=a
 for m in lm:
  u=mk(m);s=-S(d-1,-b,-a,ply+1);um(u)
  if s>best:best=s;bm=m
  if s>a:a=s
  if a>=b:break
 if not bm:r=-1e5+ply if ic else best if qs else 0
 else:
  if best<-1.5e5:best=-1e5+ply if ic else 0
  if not qs:
   TT[k]=(d,best,bm,0 if a0<best<b else 1 if best>=b else 2)
   if ply==0:BM=bm
  r=best
 HC[k]-=1
 return r
def Uc(m):
 f=m&127;t=(m>>7)&127;pr=m>>14;return '%c%d%c%d'%(97+(f&7),(f>>4)+1,97+(t&7),(t>>4)+1)+('nbrq'[pr-2]if pr else '')
def Po(p,b):return json.load(U.urlopen(U.Request(os.getenv('MAKEFUN_ENV_URL')+p,data=json.dumps(b).encode())))
while 1:
 g=Po('/game',{})
 if g['status']=='done':break
 if g['status']!='your_move':continue
 B[:]=[0]*128;bk=[4,2,3,5,6,3,2,4];sc=0
 for f in range(8):B[f]=bk[f];B[16+f]=1;B[96+f]=9;B[112+f]=bk[f]+8
 K[0]=4;K[1]=116;sd=0;ct=15;ep=-1;A=set();TT={};HC={};nd=0;BM=0
 for x in g['moves']:mk({Uc(y):y for y in Gn(0)}[x]);k=bytes(B)+bytes((sd,ct,ep+1));HC[k]=HC.get(k,0)+1
 try:
  d=1
  while d<80:S(d,-2e5,2e5,0);d+=1
 except:pass
 w=Uc(BM)
 if w not in g['legal_moves']:w=g['legal_moves'][0]
 Po('/move',{'game':g['game'],'move':w})
