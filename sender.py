import random
import sys
def main(p,g,gx):
    msg='hello'
    m=evaluate(msg)
    y=random.randint(10,20)             #check bounds
    gy=keygen(g,p)
    emsg=encrypt (gy,p,gx,m,y)
#send emsg with gy   
def keygen(g,p):
    return (g**y)%p
def encrypt(gy,p,gx,m,y):
    return (gx**y)%p    
def evaluate(msg):    
    i=0
    m=0
    g=0
    while(i<len(msg)):
        g=ord(msg[i])
        if g in range(ord('A'),ord('Z')):
            m+=(g-ord('A'))*(64**i)
        elif g in range(ord('a'),ord('z')):
            m+=(g-ord('a')+26)*(64**i)
        elif g in range(ord('0'),ord('9')):
            m+=(g-ord('0')+52)*(64**i)
        elif msg[i] =='.':
            m+=62*(64**i)
        elif msg[i] ==',':
            m+=63*(54**i) 
        i=i+1
    return m  
    

if __name__ == '__main__':
  main()      
    
