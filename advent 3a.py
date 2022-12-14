fr = open("advent 3a txt.txt","r")
num_words=0
a=0
zoz=[]
abeceda=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
for row in fr:
    for letter in row:
        num_words += 1
    itemtype=num_words/2
    for letter in row:
        a+=1
        zoz.append(letter)
        if a>itemtype-1:
            if letter in zoz:
                
