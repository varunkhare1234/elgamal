#reciever code
import sys
import random
def main(gy,mgxy):
    gx=genkey()
    m=decrypt(x,gy,mgxy,g)
    
def genkey():    
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
