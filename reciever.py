#reciever code
import sys
import random
def main(gy,mgxy):
    f=open("/home/varun/elgamal/fileb",'w+')
    f1=open("/home/varun/elgamal/filea","r")
    f1.seek(0,2)
    x=0
    gx=genkey(x)
    f1.write(str(x)+" "+str(gx))
    f.seek(0,0)
    f.write(str(x)+" "+str(gx))
    if f.
    m=decrypt(x,gy,mgxy,g)
    
def genkey(x):    
    p=2**63-1
   #p g and gx are public 
    x=random.randint(20,30)
    #x is secret key
    return gx=(g**x)%p
    #gx is public send gx and get gy
def decrypt(x,gy,mgxy,g)
    gxyinvrs=gy**(p-1-x)
    return mgxy*gxyinvrs         

if __name__ == '__main__':
  main()      
